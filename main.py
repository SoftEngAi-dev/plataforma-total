# -*- coding: utf-8 -*-
"""🎓 PLATAFORMA TOTAL v3.0 — Escuela local de programación con IA.
41 cursos · 243 lecciones · 486 quizzes · Buscador · Pomodoro · Racha 🔥
Certificados 🎓 · Chat IA con memoria · 100% offline (Ollama opcional)."""
import os, sys, json, threading, subprocess, shutil, webbrowser, datetime, platform, hashlib, random
from pathlib import Path
import customtkinter as ctk
from tkinter import messagebox, filedialog, simpledialog
try:
    import requests
except ImportError:
    requests = None
try:
    import psutil
except ImportError:
    psutil = None

BASE = Path(__file__).parent.resolve()
sys.path.insert(0, str(BASE))

# ─── CONTENIDO: 41 cursos / 243 lecciones / 486 quizzes ───
import contenido_a, contenido_b, contenido_c, contenido_d, contenido_e
_LECCIONES = {}
for _mod in (contenido_a, contenido_b, contenido_c, contenido_d, contenido_e):
    _LECCIONES.update(_mod.CURSOS_MOD)
CURSOS = {c: [{"titulo": t, "contenido": cc} for (t, cc, q) in lec] for c, lec in _LECCIONES.items()}
QUIZZES = {c: {i: [{"p": p, "ops": list(ops), "ok": ok, "exp": exp} for (p, ops, ok, exp) in lec[i][2]]
               for i in range(len(lec))} for c, lec in _LECCIONES.items()}

HOME = Path(os.path.expanduser("~"))
APP_DIR = HOME / "PlataformaTotal"
DATA_DIR = APP_DIR / "datos"
DB_PATH = DATA_DIR / "plataforma.db"

# ══════════════ ESCANEO DEL SISTEMA ══════════════
def scan_system():
    """Crea ~/PlataformaTotal, detecta SO/herramientas/Ollama. Siempre funciona."""
    paths = {"base": APP_DIR, "config": APP_DIR / "config", "datos": DATA_DIR,
             "proyectos": APP_DIR / "proyectos", "ejemplos": APP_DIR / "ejemplos"}
    for p in paths.values():
        Path(p).mkdir(parents=True, exist_ok=True)
    sis = platform.system()
    open_cmd = "start" if sis == "Windows" else ("open" if sis == "Darwin" else "xdg-open")
    tools = {t: bool(shutil.which(t)) for t in ["python3", "python", "git", "node", "docker", "ollama", "code"]}
    modelo_ollama = None
    if tools["ollama"] and requests:
        try:
            r = requests.get("http://localhost:11434/api/tags", timeout=2)
            modelos = [m["name"] for m in r.json().get("models", [])]
            modelo_ollama = modelos[0] if modelos else None
        except Exception:
            pass
    extras = [f"{t} ✓" for t in ["git", "node", "docker", "ollama", "code"] if tools[t]]
    if extras:
        modo = "Modo Total"
    elif any([tools.get("python3"), tools.get("python")]):
        modo = "Modo Esencial"
    else:
        modo = "Modo Aprendiz"
    ai = f"Ollama ({modelo_ollama})" if modelo_ollama else "Cerebro IA offline"
    sistema = {"os": sis, "paths": paths, "open_cmd": open_cmd, "tools": tools,
               "modelo_ollama": modelo_ollama, "modo": modo, "ai_backend": ai}
    try:
        (paths["config"] / "settings.json").write_text(
            json.dumps({k: (str(v) if isinstance(v, Path) else v) for k, v in sistema.items() if k != "paths"},
                       indent=2), encoding="utf-8")
    except Exception:
        pass
    return sistema

CFG = scan_system()

# ══════════════ BASE DE DATOS (SQLite) ══════════════
def _con():
    import sqlite3
    return sqlite3.connect(DB_PATH)

def init_db():
    con = _con(); cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS progreso(curso TEXT, leccion INTEGER, fecha TEXT, PRIMARY KEY(curso, leccion))")
    cur.execute("CREATE TABLE IF NOT EXISTS quiz_scores(curso TEXT, leccion INTEGER, mejor INTEGER, total INTEGER, fecha TEXT, PRIMARY KEY(curso, leccion))")
    cur.execute("CREATE TABLE IF NOT EXISTS chats(id INTEGER PRIMARY KEY AUTOINCREMENT, rol TEXT, mensaje TEXT, fecha TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS pomodoros(id INTEGER PRIMARY KEY AUTOINCREMENT, fecha TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS actividad_dias(fecha TEXT PRIMARY KEY)")
    cur.execute("CREATE TABLE IF NOT EXISTS certificados(id INTEGER PRIMARY KEY AUTOINCREMENT, curso TEXT, alumno TEXT, codigo TEXT, fecha TEXT)")
    con.commit(); con.close()

init_db()  # tablas garantizadas incluso si solo se importa el módulo

def db_marcar_actividad():
    con = _con()
    con.execute("INSERT OR IGNORE INTO actividad_dias VALUES (?)", (datetime.date.today().strftime("%Y-%m-%d"),))
    con.commit(); con.close()

def db_racha():
    con = _con()
    dias = {r[0] for r in con.execute("SELECT fecha FROM actividad_dias").fetchall()}
    con.close()
    hoy = datetime.date.today()
    hoy_s = hoy.strftime("%Y-%m-%d"); ayer_s = (hoy - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    if hoy_s not in dias and ayer_s not in dias:
        return 0
    d = hoy if hoy_s in dias else hoy - datetime.timedelta(days=1)
    n = 0
    while d.strftime("%Y-%m-%d") in dias:
        n += 1; d -= datetime.timedelta(days=1)
    return n

def db_save_progress(curso, leccion):
    db_marcar_actividad()
    con = _con(); cur = con.cursor()
    cur.execute("INSERT OR IGNORE INTO progreso VALUES (?,?,?)", (curso, leccion, datetime.datetime.now().isoformat()))
    con.commit(); con.close()

def db_lecciones_hechas(curso):
    con = _con(); cur = con.cursor()
    cur.execute("SELECT leccion FROM progreso WHERE curso=?", (curso,))
    r = {row[0] for row in cur.fetchall()}; con.close(); return r

def db_progreso_total():
    con = _con(); cur = con.cursor()
    cur.execute("SELECT count(*) FROM progreso"); n = cur.fetchone()[0]; con.close(); return n

def db_save_quiz(curso, leccion, puntaje, total):
    db_marcar_actividad()
    con = _con(); cur = con.cursor()
    cur.execute("SELECT mejor FROM quiz_scores WHERE curso=? AND leccion=?", (curso, leccion))
    row = cur.fetchone()
    mejor = max(row[0], puntaje) if row else puntaje
    cur.execute("INSERT OR REPLACE INTO quiz_scores VALUES (?,?,?,?,?)",
                (curso, leccion, mejor, total, datetime.datetime.now().isoformat()))
    con.commit(); con.close(); return mejor

def db_quiz_mejor(curso, leccion):
    con = _con(); cur = con.cursor()
    cur.execute("SELECT mejor, total FROM quiz_scores WHERE curso=? AND leccion=?", (curso, leccion))
    r = cur.fetchone(); con.close(); return r

def db_quiz_stats():
    con = _con(); cur = con.cursor()
    cur.execute("SELECT count(*), sum(CASE WHEN mejor = total THEN 1 ELSE 0 END) FROM quiz_scores")
    r = cur.fetchone(); con.close()
    return r[0] or 0, r[1] or 0

def db_save_chat(rol, mensaje):
    con = _con()
    con.execute("INSERT INTO chats(rol, mensaje, fecha) VALUES (?,?,?)", (rol, mensaje, datetime.datetime.now().isoformat()))
    con.commit(); con.close()

def db_load_chats(limite=60):
    con = _con(); cur = con.cursor()
    cur.execute("SELECT rol, mensaje FROM chats ORDER BY id DESC LIMIT ?", (limite,))
    r = cur.fetchall(); con.close(); return r[::-1]

def db_clear_chats():
    con = _con(); con.execute("DELETE FROM chats"); con.commit(); con.close()

def db_save_pomodoro():
    db_marcar_actividad()
    con = _con(); con.execute("INSERT INTO pomodoros(fecha) VALUES (?)", (datetime.datetime.now().isoformat(),))
    con.commit(); con.close()

def db_pomodoros_hoy():
    hoy = datetime.date.today().strftime("%Y-%m-%d")
    con = _con(); cur = con.cursor()
    cur.execute("SELECT count(*) FROM pomodoros WHERE fecha LIKE ?", (hoy + "%",))
    n = cur.fetchone()[0]; con.close(); return n

def db_curso_detalle(curso):
    total = len(CURSOS[curso])
    faltan_lec = total - len(db_lecciones_hechas(curso))
    con = _con(); cur = con.cursor()
    faltan_quiz = 0
    for idx in range(total):
        if QUIZZES.get(curso, {}).get(idx):
            r = cur.execute("SELECT mejor, total FROM quiz_scores WHERE curso=? AND leccion=?", (curso, idx)).fetchone()
            if not r or r[0] < r[1]:
                faltan_quiz += 1
    con.close()
    if faltan_lec or faltan_quiz:
        partes = []
        if faltan_lec:
            partes.append(f"{faltan_lec} lección(es) sin completar")
        if faltan_quiz:
            partes.append(f"{faltan_quiz} quiz(zes) sin 100%")
        return False, " y ".join(partes)
    return True, "¡Curso dominado al 100%!"

def db_guardar_certificado(curso, alumno, codigo):
    con = _con()
    con.execute("INSERT INTO certificados(curso, alumno, codigo, fecha) VALUES (?,?,?,?)",
                (curso, alumno, codigo, datetime.datetime.now().isoformat()))
    con.commit(); con.close()

def db_certificados():
    con = _con(); cur = con.cursor()
    cur.execute("SELECT curso, alumno, codigo, fecha FROM certificados ORDER BY id DESC")
    r = cur.fetchall(); con.close(); return r

# ══════════════ MOTOR IA (Ollama o cerebro offline) ══════════════
PROMPT_RAPIDO = (
    "Eres la IA de Plataforma Total, una escuela local de programación. Responde SIEMPRE en español, "
    "corto (máx 6 líneas), práctico y con mini-ejemplos de código cuando aplique. Sin humo.")

def run_ollama(prompt, modelo=None, timeout=90):
    """Consulta Ollama local. Devuelve texto o None si no está disponible."""
    modelo = modelo or CFG["modelo_ollama"]
    if not modelo or not requests:
        return None
    try:
        r = requests.post("http://localhost:11434/api/generate",
                          json={"model": modelo, "prompt": prompt, "stream": False},
                          timeout=timeout)
        return r.json().get("response", "").strip() or None
    except Exception:
        return None

def cerebro_offline(msg):
    """Respuestas de respaldo 100% offline para el chat."""
    m = msg.lower()
    if any(k in m for k in ["error", "falla", "traceback", "exception", "bug"]):
        return ("🛠 Depuración express:\n1) Lee el ÚLTIMO mensaje de error completo.\n2) Imprime/pinta variables justo antes del fallo.\n"
                "3) Reproduce el error en un ejemplo mínimo.\n4) Péguelo aquí: te explico causa y fix.")
    if "qué hago hoy" in m or "que hago hoy" in m or "estudio" in m:
        return recomendar_estudio()
    if "quiz" in m:
        return ("📝 Genera quizzes automáticos en 📚 Aprender → botón 📝 Quiz (cada lección incluye el suyo).\n"
                "Con Ollama activo, 🤖 Quiz con IA crea preguntas extra de la lección abierta.")
    if any(k in m for k in ["python", "java", "javascript", "código", "codigo"]):
        return ("🧑‍💻 Poco contexto aún, pero receta universal:\n"
                "```\n# 1. Escribe qué debe hacer en una frase\n# 2. Descompónla en 3 pasos\n# 3. Tu primera versión solo funciona, no impresiona\n# 4. Refactoriza DESPUÉS de que pase los tests\n```\n"
                "Si tienes Ollama (ollama run llama3.1:8b) te respondo con más profundidad.")
    return ("🤖 Modo offline: pregúntame sobre errores, qué estudiar hoy, quizzes, proyectos o cómo instalar Ollama.\n"
            "Para conversación completa: `ollama pull llama3.1:8b && ollama serve` y reinicia la app.")

def recomendar_estudio():
    """🧭 Recomendador: qué estudiar hoy, basado en tu progreso real."""
    total_q, perfectos = db_quiz_stats()
    pendientes_quiz = total_q - perfectos
    lineas = ["🧭 **¿QUÉ ESTUDIAR HOY?** (recomendador local)\n"]
    if pendientes_quiz:
        lineas.append(f"🏵 Prioridad 1: tienes {pendientes_quiz} quiz(zes) a menos del 100%. Reintentarlos vale mais que lecciones nuevas.")
    siguiente = None
    for curso in CURSOS:
        hechas = db_lecciones_hechas(curso)
        if len(hechas) < len(CURSOS[curso]) and hechas:
            idx = min(i for i in range(len(CURSOS[curso])) if i not in hechas)
            siguiente = (curso, CURSOS[curso][idx]["titulo"]); break
    if siguiente:
        lineas.append(f"📚 Prioridad 2: continúa «{siguiente[0]}» con «{siguiente[1]}».")
    else:
        for curso in CURSOS:
            if not db_lecciones_hechas(curso):
                lineas.append(f"🌱 Prioridad 2: empieza el curso «{curso}». Nadie llega sin empezar."); break
    lineas.append(f"🍅 Prioridad 3: mínimo 2 pomodoros hoy (van {db_pomodoros_hoy()}). Racha actual: 🔥 {db_racha()} día(s).")
    return "\n".join(lineas)

# ══════════════ PLANTILLAS ══════════════
HTML_CERTIFICADO = """<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<title>Certificado — Plataforma Total</title>
<style>
 body{font-family:Georgia,serif;background:#0d1117;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;padding:20px}
 .cert{background:#fffdf5;color:#1a1a2e;max-width:860px;padding:56px 70px;border:14px double #b8860b;text-align:center;box-shadow:0 0 60px #000}
 h1{font-size:30px;margin:10px 0;color:#9a7209;letter-spacing:4px}
 .curso{font-size:22px;font-weight:bold;margin:16px auto;max-width:640px}
 .alumno{font-size:36px;font-family:'Brush Script MT',cursive;margin:12px 0;border-bottom:1px solid #999;display:inline-block;padding:0 44px 8px}
 .det{color:#555;font-size:14px;margin-top:20px;line-height:1.7}
 .codigo{font-family:monospace;background:#f0ead0;padding:8px 16px;display:inline-block;margin-top:18px;border-radius:6px;letter-spacing:2px}
 .logo{font-size:46px}
 .firma{margin-top:36px;display:flex;justify-content:space-around;color:#444;font-size:13px}
 .org{font-size:12px;letter-spacing:5px;color:#888}
 @media print{body{background:#fff;padding:0}.cert{box-shadow:none;max-width:100%}}
</style></head><body>
<div class="cert">
 <div class="logo">🎓</div>
 <div class="org">PLATAFORMA TOTAL · ESCUELA LOCAL · 100% OFFLINE</div>
 <h1>CERTIFICADO DE FINALIZACIÓN</h1>
 <p>Se certifica orgullosamente que</p>
 <div class="alumno">{alumno}</div>
 <p>ha completado con excelencia el curso</p>
 <div class="curso">«{curso}»</div>
 <p class="det">✅ {lecciones} lecciones completadas &nbsp;·&nbsp; 🏆 {quizzes} preguntas de evaluación aprobadas al 100%<br>
 Metodología: aprender construyendo — proyectos reales verificables<br>
 Emitido el {fecha}</p>
 <div class="firma"><span>____________________<br>Plataforma Total</span><span>____________________<br>El Estudiante</span></div>
 <div class="codigo">VERIFICACIÓN: {codigo}</div>
</div></body></html>"""

DOCS = {"Python": "https://docs.python.org/es/3/", "JavaScript (MDN)": "https://developer.mozilla.org/es/",
        "React": "https://es.react.dev/", "Django": "https://docs.djangoproject.com/",
        "PostgreSQL": "https://www.postgresql.org/docs/", "Docker": "https://docs.docker.com/",
        "Git": "https://git-scm.com/docs", "Ollama": "https://ollama.com/library",
        "Roadmaps": "https://roadmap.sh/", "TypeScript": "https://www.typescriptlang.org/docs/"}

EJEMPLOS = {
    "hola_mundo.py": "# Ejecuta: python hola_mundo.py\nnombre = input('¿Tu nombre? ')\nprint(f'Hola {nombre}, ¡bienvenido a Plataforma Total!')",
    "http_server.py": "# python http_server.py → http://localhost:8000\nimport http.server, socketserver\nwith socketserver.TCPServer(('', 8000), http.server.SimpleHTTPRequestHandler) as h:\n    print('Sirviendo en :8000'); h.serve_forever()",
    "cuenta_regresiva.py": "import time\nfor i in range(5, 0, -1):\n    print(i); time.sleep(1)\nprint('🚀 ¡Despegue!')",
    "index.html": "<!DOCTYPE html><html lang=es><meta charset=utf-8><title>Mi web</title>\n<h1 style='color:#6f42c1'>Hola desde Plataforma Total</h1><p>Abre este archivo en tu navegador.</p>",
    "app.js": "// Ejecuta: node app.js\nconst sumar = (a, b) => a + b;\nconsole.log('2 + 3 =', sumar(2, 3));",
    "consulta.sql": "-- Ejecuta en psql / cualquier cliente SQL\nSELECT 'Hola, SQL' AS saludo;",
}
PROYECTOS_IDEAS = [
    ("Personal", "🗂 Gestor de tareas CLI", "CLI en Python: añadir/listar/completar tareas guardadas en JSON/SQLite."),
    ("Web", "🌐 Portafolio personal", "HTML+CSS responsive con tus proyectos, sin frameworks."),
    ("Web", "⏲ Timer Pomodoro web", "JS puro: intervalos, sonido, historial en localStorage."),
    ("Datos", "📊 Analizador de CSV", "Lee un CSV y muestra totales/promedios y un top-N."),
    ("Backend", "🌦 API del tiempo (mock)", "Express o FastAPI: 3 endpoints + tests básicos."),
    ("Juegos", "🎮 Adivina el número", "Consola: números aleatorios, intentos, récord."),
]

# ══════════════ APP PRINCIPAL ══════════════
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        try:  # 🖼️ icono de ventana/barra de tareas (empaquetado con --add-data)
            from tkinter import PhotoImage
            _base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
            _ico = os.path.join(_base, "assets", "icono.png")
            if os.path.exists(_ico):
                self._imagen_icono = PhotoImage(file=_ico)
                self.iconphoto(True, self._imagen_icono)
        except Exception:
            pass
        self.title(f"Plataforma Total — {CFG['modo']} · {CFG['ai_backend']}")
        self.geometry("1400x900")
        ctk.set_appearance_mode("dark")
        init_db()
        self.leccion_actual = 0
        self.busqueda = ctk.StringVar()
        self.pomo = {"rest": 25 * 60, "activo": False, "fase": "trabajo"}
        self.quiz = {"activo": False, "preguntas": [], "idx": 0, "puntos": 0, "curso": None, "leccion": 0}
        self.build_sidebar()
        self.main = ctk.CTkFrame(self); self.main.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        self.show("🏠 Inicio")

    # ── sidebar ──
    def build_sidebar(self):
        sb = ctk.CTkFrame(self, width=210); sb.pack(side="left", fill="y", padx=5, pady=5); sb.pack_propagate(False)
        ctk.CTkLabel(sb, text="🎓 PLATAFORMA TOTAL", font=("Arial", 16, "bold")).pack(pady=(15, 2))
        ctk.CTkLabel(sb, text=CFG["modo"], font=("Arial", 10), text_color="gray").pack()
        self.nav = {}
        for t in ["🏠 Inicio", "📚 Aprender", "🤖 IA Chat", "🚀 Proyectos", "💻 Terminal", "🛠 Herramientas", "📖 Docs", "📝 Ejemplos"]:
            b = ctk.CTkButton(sb, text=t, anchor="w", command=lambda x=t: self.show(x))
            b.pack(fill="x", padx=10, pady=3); self.nav[t] = b
        # 🍅 panel Pomodoro
        pf = ctk.CTkFrame(sb, fg_color="#1d1633"); pf.pack(fill="x", padx=10, pady=15)
        self.pomo_fase = ctk.CTkLabel(pf, text="🍅 Enfoque 25m", font=("Arial", 11, "bold")); self.pomo_fase.pack(pady=(8, 0))
        self.pomo_lbl = ctk.CTkLabel(pf, text="25:00", font=("Arial", 22, "bold")); self.pomo_lbl.pack()
        fila = ctk.CTkFrame(pf, fg_color="transparent"); fila.pack()
        self.pomo_btn = ctk.CTkButton(fila, text="▶", width=44, command=self.pomo_toggle); self.pomo_btn.pack(side="left", padx=3, pady=4)
        ctk.CTkButton(fila, text="↺", width=44, fg_color="gray", command=self.pomo_reset).pack(side="left", padx=3, pady=4)
        self.pomo_hoy = ctk.CTkLabel(pf, text=f"Hoy: {'🍅' * min(db_pomodoros_hoy(), 8) or '—'} ({db_pomodoros_hoy()})", font=("Arial", 10)); self.pomo_hoy.pack(pady=(0, 8))
        ctk.CTkLabel(sb, text="v3.0 · 100% local", font=("Arial", 9), text_color="gray").pack(side="bottom", pady=8)

    def show(self, tab):
        for w in self.main.winfo_children():
            w.destroy()
        builders = {"🏠 Inicio": self.build_inicio, "📚 Aprender": self.build_aprender, "🤖 IA Chat": self.build_ia,
                    "🚀 Proyectos": self.build_proyectos, "💻 Terminal": self.build_terminal,
                    "🛠 Herramientas": self.build_herramientas, "📖 Docs": self.build_docs, "📝 Ejemplos": self.build_ejemplos}
        builders[tab](self.main)

    # ── 🏠 INICIO ──
    def build_inicio(self, f):
        ctk.CTkLabel(f, text="🏠 Panel de Control", font=("Arial", 24, "bold")).pack(pady=10)
        cards = ctk.CTkFrame(f); cards.pack(fill="x", padx=10)
        hechas = db_progreso_total(); total_lecciones = sum(len(v) for v in CURSOS.values())
        q_hechos, q_perfectos = db_quiz_stats(); racha = db_racha()
        for titulo, valor in [("Lecciones ✅", f"{hechas}/{total_lecciones}"), ("Quizzes 🏆", f"{q_perfectos} de {q_hechos}"),
                              ("🔥 Racha", f"{racha} día{'s' if racha != 1 else ''}"), ("🎓 Certificados", str(len(db_certificados()))),
                              ("Proyectos", str(len(list(CFG["paths"]["proyectos"].glob('*'))))), ("Modo IA", CFG["ai_backend"])]:
            c = ctk.CTkFrame(cards); c.pack(side="left", expand=True, fill="both", padx=4, pady=6)
            ctk.CTkLabel(c, text=valor, font=("Arial", 16, "bold")).pack(pady=(12, 2))
            ctk.CTkLabel(c, text=titulo, font=("Arial", 10), text_color="gray").pack(pady=(0, 10))
        body = ctk.CTkTextbox(f, wrap="word", font=("Arial", 13)); body.pack(fill="both", expand=True, padx=10, pady=8)
        body.insert("end", self.info_sistema() + "\n" + recomendar_estudio())
        body.configure(state="disabled")
        bar = ctk.CTkFrame(f); bar.pack(pady=6)
        ctk.CTkButton(bar, text="🧭 ¿Qué estudio hoy? (IA)", fg_color="#6f42c1", command=self.recomendar_con_ia).pack(side="left", padx=6)
        ctk.CTkButton(bar, text="🔄 Refrescar", fg_color="gray", command=lambda: self.show("🏠 Inicio")).pack(side="left", padx=6)

    def info_sistema(self):
        t = CFG["tools"]
        lineas = [f"💻 SO: {CFG['os']} · {CFG['modo']}", f"🤖 IA: {CFG['ai_backend']}"]
        if psutil:
            lineas.append(f"🧠 RAM: {psutil.virtual_memory().available // 2**20} MB libres · CPUs: {psutil.cpu_count()}")
        lineas.append("🧰 Detectado: " + (" | ".join(k for k, v in t.items() if v) if any(t.values()) else "solo Python empaquetado"))
        if not t["ollama"]:
            lineas.append("💡 Para IA conversacional: instala Ollama (ollama.com) → `ollama pull llama3.1:8b` → `ollama serve` y reiníciame.")
        lineas.append(f"📂 Tu base local: {CFG['paths']['base']}")
        return "\n".join(lineas) + "\n"

    def recomendar_con_ia(self):
        prompt = PROMPT_RAPIDO + "\n\n" + recomendar_estudio() + "\n\nMejóralo en 2 consejos adicionales."
        respuesta = run_ollama(prompt)
        if respuesta:
            messagebox.showinfo("🧭 Tu plan de hoy (IA)", respuesta)
        else:
            messagebox.showinfo("🧭 Tu plan de hoy", recomendar_estudio())

    # ── 📚 APRENDER ──
    def build_aprender(self, f):
        top = ctk.CTkFrame(f); top.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(top, text="Curso:").pack(side="left", padx=6)
        self.curso_var = ctk.StringVar(value=list(CURSOS.keys())[0])
        ctk.CTkOptionMenu(top, variable=self.curso_var, values=list(CURSOS.keys()), width=420,
                          command=lambda _: self.cargar_lecciones()).pack(side="left", padx=6)
        ctk.CTkEntry(top, textvariable=self.busqueda, placeholder_text="🔍 buscar en todas las lecciones…", width=300).pack(side="right", padx=6)
        cuerpo = ctk.CTkFrame(f); cuerpo.pack(fill="both", expand=True, padx=10, pady=5)
        self.lista = ctk.CTkScrollableFrame(cuerpo, width=330); self.lista.pack(side="left", fill="y", padx=(0, 8))
        right = ctk.CTkFrame(cuerpo); right.pack(side="left", fill="both", expand=True)
        self.leccion_title = ctk.CTkLabel(right, text="", font=("Arial", 16, "bold"), wraplength=760); self.leccion_title.pack(pady=6)
        self.cuerpo_txt = ctk.CTkTextbox(right, wrap="word", font=("Consolas", 13)); self.cuerpo_txt.pack(fill="both", expand=True, padx=10)
        bar = ctk.CTkFrame(right); bar.pack(pady=6)
        ctk.CTkButton(bar, text="✅ Completada", command=self.completar_leccion).pack(side="left", padx=5)
        self.quiz_btn = ctk.CTkButton(bar, text="📝 Quiz", fg_color="#6f42c1", command=self.iniciar_quiz)
        self.quiz_btn.pack(side="left", padx=5)
        ctk.CTkButton(bar, text="🤖 Quiz con IA", fg_color="#0e7490", command=self.quiz_con_ia).pack(side="left", padx=5)
        ctk.CTkButton(bar, text="🎓 Certificado", fg_color="#b8860b", command=self.generar_certificado).pack(side="left", padx=5)
        prow = ctk.CTkFrame(right, fg_color="transparent"); prow.pack(fill="x", padx=15, pady=(2, 0))
        self.curso_prog_lbl = ctk.CTkLabel(prow, text="Curso: 0/0", text_color="gray", font=("Arial", 11)); self.curso_prog_lbl.pack(side="left")
        self.curso_prog = ctk.CTkProgressBar(prow); self.curso_prog.pack(side="left", expand=True, fill="x", padx=10); self.curso_prog.set(0)
        self.quiz_score_lbl = ctk.CTkLabel(right, text="", text_color="gray"); self.quiz_score_lbl.pack()
        self.busqueda.trace_add("write", lambda *a: self.cargar_lecciones())
        self.bind("<Escape>", lambda e: self.busqueda.set(""))
        if self.quiz["activo"]:
            self.mostrar_pregunta()
        else:
            self.cargar_lecciones()

    def resultados_busqueda(self):
        q = self.busqueda.get().strip().lower()
        if len(q) < 2:
            return []
        out = []
        for curso, lecciones in CURSOS.items():
            for i, lec in enumerate(lecciones):
                if q in lec["titulo"].lower() or q in lec["contenido"].lower():
                    out.append((curso, i, lec))
        return out[:40]

    def cargar_lecciones(self):
        curso = self.curso_var.get()
        if not curso:
            return
        for w in self.lista.winfo_children():
            w.destroy()
        res = self.resultados_busqueda()
        if res:
            for c, i, lec in res:
                ctk.CTkButton(self.lista, text=f"[{c[:16]}…] {lec['titulo']}", anchor="w",
                              command=lambda cc=c, ii=i: (self.curso_var.set(cc), self.busqueda.set(""), self.ver_leccion(ii))).pack(fill="x", pady=2)
            return
        hechas = db_lecciones_hechas(curso)
        for i, lec in enumerate(CURSOS[curso]):
            marca = ""
            if i in hechas:
                marca = " ✅"
            if QUIZZES.get(curso, {}).get(i):
                marca += " 📝"
                r = db_quiz_mejor(curso, i)
                if r and r[0] == r[1]:
                    marca += " 🏆"
            ctk.CTkButton(self.lista, text=f"{lec['titulo']}{marca}", anchor="w",
                          command=lambda idx=i: self.ver_leccion(idx)).pack(fill="x", pady=2)
        self.actualizar_progreso_curso()
        self.ver_leccion(0)

    def ver_leccion(self, idx):
        curso = self.curso_var.get()
        self.leccion_actual = idx
        lec = CURSOS[curso][idx]
        self.leccion_title.configure(text=lec["titulo"])
        self.cuerpo_txt.configure(state="normal"); self.cuerpo_txt.delete("0.0", "end")
        self.cuerpo_txt.insert("0.0", lec["contenido"]); self.cuerpo_txt.configure(state="disabled")
        quiz = QUIZZES.get(curso, {}).get(idx, [])
        r = db_quiz_mejor(curso, idx)
        if r:
            estado = f" (mejor: {r[0]}/{r[1]}{' 🏆' if r[0] == r[1] else ''})"
        else:
            estado = " (sin jugar)"
        self.quiz_btn.configure(text=f"📝 Quiz ({len(quiz)}){estado}" if quiz else "📝 Quiz")
        self.quiz_score_lbl.configure(text="")

    def completar_leccion(self):
        db_save_progress(self.curso_var.get(), self.leccion_actual)
        self.actualizar_progreso_curso()
        self.cargar_lecciones_sin_reset()
        messagebox.showinfo("Progreso", "Lección guardada en SQLite ✅")

    def actualizar_progreso_curso(self):
        curso = self.curso_var.get()
        total = len(CURSOS[curso]); hechas = len(db_lecciones_hechas(curso))
        self.curso_prog.set(hechas / total if total else 0)
        self.curso_prog_lbl.configure(text=f"Curso: {hechas}/{total} ✅")

    def cargar_lecciones_sin_reset(self):
        actual = self.leccion_actual
        guard = self.busqueda.get(); self.busqueda.set("")
        self.cargar_lecciones()
        self.ver_leccion(actual)

    # quizzes
    def iniciar_quiz(self):
        curso = self.curso_var.get(); idx = self.leccion_actual
        quiz = QUIZZES.get(curso, {}).get(idx, [])
        if not quiz:
            messagebox.showinfo("Quiz", "Esta lección no tiene quiz incluido. Usa 🤖 Quiz con IA (requiere Ollama).")
            return
        self.quiz = {"activo": True, "preguntas": quiz, "idx": 0, "puntos": 0, "curso": curso, "leccion": idx}
        self.mostrar_pregunta()

    def quiz_con_ia(self):
        curso = self.curso_var.get(); lec = CURSOS[curso][self.leccion_actual]
        self.quiz_score_lbl.configure(text="🤖 Generando quiz con IA (Ollama)… espera")
        def trabajo():
            prompt = (f"{PROMPT_RAPIDO}\n\nCrea 3 preguntas de opción múltiple sobre esta lección.\n"
                      f"Formato exacto por pregunta:\nP: <pregunta>\nA) <op>\nB) <op>\nC) <op>\nD) <op>\nR: <letra de la correcta>\nX: <explicación 1 línea>\n\n"
                      f"LECCIÓN:\n{lec['contenido'][:2500]}")
            txt = run_ollama(prompt, timeout=120)
            preguntas = self.parsear_quiz_ia(txt) if txt else []
            def aplicar():
                if preguntas:
                    self.quiz = {"activo": True, "preguntas": preguntas, "idx": 0, "puntos": 0,
                                 "curso": "🤖 Quiz IA — " + curso, "leccion": self.leccion_actual}
                    self.mostrar_pregunta()
                else:
                    self.quiz_score_lbl.configure(text="❌ Ollama no disponible o respuesta inválida (¿ollama serve?)")
            self.after(0, aplicar)
        threading.Thread(target=trabajo, daemon=True).start()

    def parsear_quiz_ia(self, txt):
        preguntas = []; p = None
        for linea in (txt or "").splitlines():
            l = linea.strip()
            if l.startswith("P:"):
                if p and p["ops"] and p["ok"] is not None:
                    preguntas.append(p)
                p = {"p": l[2:].strip(), "ops": [], "ok": None, "exp": ""}
            elif p is not None and len(l) > 3 and l[0] in "ABCD" and l[1] == ")":
                p["ops"].append(l[3:].strip())
            elif p is not None and l.startswith("R:"):
                letra = l[2:].strip()[:1].upper()
                if letra in "ABCD":
                    p["ok"] = "ABCD".index(letra)
            elif p is not None and l.startswith("X:"):
                p["exp"] = l[2:].strip()
        if p and p["ops"] and p["ok"] is not None:
            preguntas.append(p)
        return [q for q in preguntas if len(q["ops"]) >= 3][:6]

    def mostrar_pregunta(self):
        if not self.quiz["activo"]:
            return
        if self.quiz["idx"] >= len(self.quiz["preguntas"]):
            self.fin_quiz(); return
        q = self.quiz["preguntas"][self.quiz["idx"]]
        self.leccion_title.configure(text=f"📝 Pregunta {self.quiz['idx'] + 1}/{len(self.quiz['preguntas'])}")
        self.cuerpo_txt.configure(state="normal"); self.cuerpo_txt.delete("0.0", "end")
        self.cuerpo_txt.insert("0.0", q["p"]); self.cuerpo_txt.configure(state="disabled")
        for w in self.lista.winfo_children():
            w.destroy()
        for i, op in enumerate(q["ops"]):
            ctk.CTkButton(self.lista, text=op, anchor="w", fg_color="#333", hover_color="#444",
                          command=lambda j=i: self.responder_quiz(j)).pack(fill="x", pady=4, ipady=4)

    def responder_quiz(self, elegida):
        q = self.quiz["preguntas"][self.quiz["idx"]]
        correcta = elegida == q["ok"]
        if correcta:
            self.quiz["puntos"] += 1
        self.quiz_score_lbl.configure(text=("✅ ¡Correcta! " if correcta else f"❌ Era: {q['ops'][q['ok']]} · ") + q["exp"])
        self.quiz["idx"] += 1
        self.after(900, self.mostrar_pregunta)

    def fin_quiz(self):
        total = len(self.quiz["preguntas"]); puntos = self.quiz["puntos"]
        if self.quiz["curso"] in CURSOS:
            mejor = db_save_quiz(self.quiz["curso"], self.quiz["leccion"], puntos, total)
            msg_db = f" · mejor: {mejor}/{total}"
        else:
            mejor = puntos; msg_db = ""
        self.quiz["activo"] = False
        if puntos == total:
            msg = f"🏆 ¡Perfecto! {puntos}/{total}{msg_db}\nQuiz dominado al 100%."
        else:
            msg = f"Resultado: {puntos}/{total} ({round(puntos * 100 / total)}%){msg_db}\nRepasa la lección y reintenta: la meta es 100%."
        messagebox.showinfo("📝 Resultado del quiz", msg)
        self.cargar_lecciones()

    # certificados
    def generar_certificado(self):
        curso = self.curso_var.get()
        completo, msg = db_curso_detalle(curso)
        if not completo:
            messagebox.showinfo("🎓 Certificado", f"Aún falta para certificar este curso:\n\n• {msg}\n\nCompleta lecciones (✅) y quizzes al 100% (🏆).")
            return
        alumno = simpledialog.askstring("🎓 Certificado", "Nombre completo para el certificado:", parent=self)
        if not alumno:
            return
        alumno = alumno.strip()
        lecciones = len(CURSOS[curso])
        n_quiz = sum(len(QUIZZES.get(curso, {}).get(i, [])) for i in range(lecciones))
        codigo = hashlib.sha256(f"{alumno}|{curso}|{datetime.date.today()}".encode()).hexdigest()[:12].upper()
        carpeta = CFG["paths"]["datos"] / "certificados"; carpeta.mkdir(exist_ok=True)
        ruta = carpeta / f"certificado-{alumno.replace(' ', '_').lower()}.html"
        ruta.write_text(HTML_CERTIFICADO.format(alumno=alumno, curso=curso, lecciones=lecciones, quizzes=n_quiz,
                                                codigo=codigo, fecha=datetime.date.today().strftime("%d/%m/%Y")), encoding="utf-8")
        db_guardar_certificado(curso, alumno, codigo)
        self.open_path(ruta)
        messagebox.showinfo("🎓 ¡Felicitaciones!", f"Certificado emitido:\n{ruta}\n\nCódigo: {codigo}\n(Imprímelo a PDF desde el navegador)")

    # ── 🤖 IA CHAT ──
    def build_ia(self, f):
        top = ctk.CTkFrame(f); top.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(top, text=f"🤖 {CFG['ai_backend']}", font=("Arial", 13, "bold")).pack(side="left", padx=8)
        btn = ctk.CTkButton(top, text="🔄 Detectar Ollama", width=140, fg_color="gray", command=self.ia_rescan); btn.pack(side="left", padx=6)
        self.modelo = ctk.StringVar(value=CFG["modelo_ollama"] or "sin Ollama")
        valores = [CFG["modelo_ollama"]] if CFG["modelo_ollama"] else ["sin Ollama"]
        ctk.CTkOptionMenu(top, variable=self.modelo, values=valores).pack(side="right", padx=6)
        ctk.CTkButton(top, text="🗑 Historial", width=90, fg_color="gray", command=self.limpiar_chat).pack(side="right", padx=6)
        self.chat_box = ctk.CTkTextbox(f, wrap="word", font=("Arial", 13)); self.chat_box.pack(fill="both", expand=True, padx=10, pady=5)
        historial = db_load_chats(60)
        if historial:
            for rol, mensaje in historial:
                self.chat_box.insert("end", f"\n{rol}:\n{mensaje}\n" + "-" * 40 + "\n")
            self.chat_box.insert("end", "\n📜 (historial recuperado de SQLite — continúas donde quedaste)\n")
        else:
            self.chat_box.insert("0.0", "🤖 Hola, soy tu IA Total Local.\nCon Ollama te respondo con tu modelo; sin él, con cerebro offline.\nPídeme errores, código, qué estudiar hoy, quizzes…\n")
        self.chat_box.configure(state="disabled")
        env = ctk.CTkFrame(f); env.pack(fill="x", padx=10, pady=6)
        self.entrada = ctk.CTkEntry(env, placeholder_text="Escribe aquí… (Enter para enviar)"); self.entrada.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self.entrada.bind("<Return>", lambda e: self.enviar_ia())
        ctk.CTkButton(env, text="Enviar ➤", command=self.enviar_ia).pack(side="left")

    def ia_rescan(self):
        global CFG
        CFG = scan_system()
        self.show("🤖 IA Chat")

    def add_chat(self, quien, texto):
        if texto != "pensando...":
            db_save_chat(quien, texto)
        self.chat_box.configure(state="normal"); self.chat_box.insert("end", f"\n{quien}:\n{texto}\n" + "-" * 40 + "\n")
        self.chat_box.see("end"); self.chat_box.configure(state="disabled")

    def limpiar_chat(self):
        db_clear_chats()
        self.chat_box.configure(state="normal"); self.chat_box.delete("0.0", "end")
        self.chat_box.insert("0.0", "🤖 Historial borrado. Empecemos de nuevo.\n"); self.chat_box.configure(state="disabled")

    def enviar_ia(self):
        msg = self.entrada.get().strip()
        if not msg:
            return
        self.entrada.delete(0, "end")
        self.add_chat("🧑 Tú", msg)
        self.add_chat("🤖 IA", "pensando...")
        def trabajo():
            resp = run_ollama(PROMPT_RAPIDO + "\n\nUsuario: " + msg)
            if not resp:
                resp = cerebro_offline(msg)
            def pintar():
                self.chat_box.configure(state="normal")
                contenido = self.chat_box.get("0.0", "end")
                idx = contenido.rfind("pensando...")
                if idx >= 0:
                    self.chat_box.delete(f"{idx}end-1c", "end")
                self.chat_box.insert("end", resp)
                self.chat_box.see("end"); self.chat_box.configure(state="disabled")
                db_save_chat("🤖 IA", resp)
            self.after(0, pintar)
        threading.Thread(target=trabajo, daemon=True).start()

    # ── 🚀 PROYECTOS ──
    def build_proyectos(self, f):
        ctk.CTkLabel(f, text="🚀 Proyectos reales (aprende construyendo)", font=("Arial", 20, "bold")).pack(pady=10)
        grid = ctk.CTkFrame(f); grid.pack(pady=5)
        for i, (tag, titulo, desc) in enumerate(PROYECTOS_IDEAS):
            c = ctk.CTkFrame(grid); c.grid(row=i // 2, column=i % 2, padx=8, pady=8, sticky="n")
            ctk.CTkLabel(c, text=f"{titulo}  <{tag}>", font=("Arial", 13, "bold")).pack(pady=(10, 2), padx=10)
            ctk.CTkLabel(c, text=desc, wraplength=380, justify="left").pack(padx=12)
            ctk.CTkButton(c, text="Crear esqueleto", fg_color="#6f42c1",
                          command=lambda t=titulo, d=desc: self.crear_proyecto(t, d)).pack(pady=10)
        ctk.CTkButton(f, text="📂 Abrir carpeta de proyectos", fg_color="gray",
                      command=lambda: self.open_path(CFG["paths"]["proyectos"])).pack(pady=8)

    def crear_proyecto(self, titulo, desc):
        nombre = "".join(ch if ch.isalnum() else "-" for ch in titulo.lower()).strip("-")
        ruta = CFG["paths"]["proyectos"] / nombre
        ruta.mkdir(exist_ok=True)
        (ruta / "LEEME.md").write_text(f"# {titulo}\n\n{desc}\n\n## Entregables\n- [ ] Funciona\n- [ ] Código comentado\n- [ ] README claro\n", encoding="utf-8")
        (ruta / "main.py").write_text(f"# {titulo}\n# TODO: empieza por lo mínimo que funcione\n", encoding="utf-8")
        self.open_path(ruta)
        messagebox.showinfo("🚀 Proyecto creado", f"Esqueleto listo en:\n{ruta}")

    # ── 💻 TERMINAL ──
    def build_terminal(self, f):
        ctk.CTkLabel(f, text="💻 Terminal aislada (practica comandos aquí)", font=("Arial", 18, "bold")).pack(pady=8)
        self.term_out = ctk.CTkTextbox(f, wrap="word", font=("Consolas", 12)); self.term_out.pack(fill="both", expand=True, padx=10, pady=5)
        self.term_out.insert("0.0", "$ terminal local — los comandos corren en tu PC real. Cuidado con `rm`.\n$ ")
        self.term_out.configure(state="disabled")
        self.term_cmd = ctk.CTkEntry(f, placeholder_text="$ escribe un comando y Enter")
        self.term_cmd.pack(fill="x", padx=10, pady=6); self.term_cmd.bind("<Return>", self.term_run)
        self.term_cwd = str(Path.cwd())

    def term_run(self, event):
        cmd = self.term_cmd.get().strip(); self.term_cmd.delete(0, "end")
        if not cmd:
            return
        if cmd.startswith("cd "):
            destino = (Path(self.term_cwd) / cmd[3:]).resolve()
            self.term_cwd = str(destino) if destino.is_dir() else self.term_cwd
            self.term_print(f"{cmd}\n")
            return
        try:
            r = subprocess.run(cmd, shell=True, cwd=self.term_cwd, capture_output=True, text=True, timeout=20)
            salida = (r.stdout + r.stderr)[:5000]
        except Exception as e:
            salida = f"error: {e}"
        self.term_print(f"{cmd}\n{salida}\n$ ")

    def term_print(self, texto):
        self.term_out.configure(state="normal"); self.term_out.insert("end", texto)
        self.term_out.see("end"); self.term_out.configure(state="disabled")

    # ── 🛠 HERRAMIENTAS ──
    def build_herramientas(self, f):
        ctk.CTkLabel(f, text="🛠 Herramientas del sistema", font=("Arial", 18, "bold")).pack(pady=10)
        grid = ctk.CTkFrame(f); grid.pack(pady=8)
        tools = [("📊 Info del sistema", self.info_sistema), ("🤖 Re-escanear Ollama", lambda: (self.ia_rescan(), "Reescaneado")),
                 ("📂 Abrir base local", lambda: CFG["paths"]["base"]), ("🗄 Abrir datos (DB)", lambda: CFG["paths"]["datos"]),
                 ("🧪 Self-test contenido", self.selftest)]
        for i, (nombre, fn) in enumerate(tools):
            ctk.CTkButton(grid, text=nombre, width=220, command=lambda fnc=fn: self.ejecutar_herramienta(fnc)).grid(row=i, column=0, pady=4)
        self.herr_out = ctk.CTkTextbox(f, height=220, font=("Consolas", 12)); self.herr_out.pack(fill="x", padx=10, pady=8)

    def ejecutar_herramienta(self, fn):
        try:
            res = fn()
            if isinstance(res, Path):
                self.open_path(res); res = f"Abierto: {res}"
            self.herr_out.delete("0.0", "end"); self.herr_out.insert("0.0", str(res))
        except Exception as e:
            self.herr_out.delete("0.0", "end"); self.herr_out.insert("0.0", f"error: {e}")

    def selftest(self):
        total_lec = sum(len(v) for v in CURSOS.values())
        total_q = sum(len(ps) for c in QUIZZES.values() for ps in c.values())
        errores = 0
        for curso, por_idx in QUIZZES.items():
            for idx, preguntas in por_idx.items():
                if idx >= len(CURSOS[curso]):
                    errores += 1
                for q in preguntas:
                    if set(q) != {"p", "ops", "ok", "exp"} or not (0 <= q["ok"] < len(q["ops"])):
                        errores += 1
        return (f"📚 {len(CURSOS)} cursos · {total_lec} lecciones · {total_q} preguntas\n"
                f"Estructura: {'✅ 100% válida' if errores == 0 else f'❌ {errores} errores'}\n"
                f"DB: {DB_PATH} · Racha: 🔥 {db_racha()} días")

    # ── 📖 DOCS ──
    def build_docs(self, f):
        ctk.CTkLabel(f, text="📖 Documentación oficial (se abre en tu navegador)", font=("Arial", 16, "bold")).pack(pady=12)
        for nombre, url in DOCS.items():
            ctk.CTkButton(f, text=f"{nombre}  ↗", anchor="w", width=380,
                          command=lambda u=url: webbrowser.open(u)).pack(pady=3)

    # ── 📝 EJEMPLOS ──
    def build_ejemplos(self, f):
        ctk.CTkLabel(f, text="📝 Ejemplos ejecutables (se copian a tu carpeta ejemplos/)", font=("Arial", 16, "bold")).pack(pady=12)
        grid = ctk.CTkFrame(f); grid.pack(pady=5)
        for i, (nombre, codigo) in enumerate(EJEMPLOS.items()):
            ctk.CTkButton(grid, text=nombre, width=200, command=lambda n=nombre, c=codigo: self.crear_ejemplo(n, c)).grid(row=i // 3, column=i % 3, padx=8, pady=8)
        self.ejemplo_txt = ctk.CTkTextbox(f, font=("Consolas", 12), height=300); self.ejemplo_txt.pack(fill="both", expand=True, padx=10, pady=8)

    def crear_ejemplo(self, nombre, codigo):
        ruta = CFG["paths"]["ejemplos"] / nombre
        ruta.write_text(codigo, encoding="utf-8")
        self.ejemplo_txt.delete("0.0", "end"); self.ejemplo_txt.insert("0.0", f"# Copiado a: {ruta}\n\n{codigo}")

    def open_path(self, path):
        try:
            subprocess.run([CFG["open_cmd"], str(path)], check=False)
        except Exception:
            webbrowser.open(str(path))

    # ── 🍅 POMODORO ──
    def pomo_toggle(self):
        self.pomo["activo"] = not self.pomo["activo"]
        self.pomo_btn.configure(text="⏸" if self.pomo["activo"] else "▶")
        if self.pomo["activo"]:
            self.pomo_tick()

    def pomo_tick(self):
        if not self.pomo["activo"]:
            return
        self.pomo["rest"] -= 1
        self.pomo_actualizar()
        if self.pomo["rest"] <= 0:
            self.pomo_cambiar_fase()
        self.after(1000, self.pomo_tick)

    def pomo_cambiar_fase(self):
        self.bell()
        if self.pomo["fase"] == "trabajo":
            self.pomo["fase"] = "descanso"; self.pomo["rest"] = 5 * 60
            db_save_pomodoro()
            hoy = db_pomodoros_hoy()
            self.pomo_hoy.configure(text=f"Hoy: {'🍅' * min(hoy, 8)} ({hoy})")
            self.pomo_fase.configure(text="☕ Descanso 5m")
        else:
            self.pomo["fase"] = "trabajo"; self.pomo["rest"] = 25 * 60
            self.pomo_fase.configure(text="🍅 Enfoque 25m")
        self.pomo_actualizar()

    def pomo_reset(self):
        self.pomo["activo"] = False
        self.pomo["fase"] = "trabajo"; self.pomo["rest"] = 25 * 60
        self.pomo_btn.configure(text="▶")
        self.pomo_fase.configure(text="🍅 Enfoque 25m")
        self.pomo_actualizar()

    def pomo_actualizar(self):
        m, s = divmod(max(self.pomo["rest"], 0), 60)
        self.pomo_lbl.configure(text=f"{m:02d}:{s:02d}")

# ─── ENTRYPOINT ───
if __name__ == "__main__":
    app = App()
    app.mainloop()
