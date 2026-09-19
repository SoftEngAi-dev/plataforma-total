#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""🌱 EXPANSOR DE CONTENIDO — Plataforma Total
Genera el ecosistema de material de estudio (3.499 archivos) derivado AUTOMÁTICAMENTE
de los 41 cursos / 241 lecciones / 482 quizzes de la app.

  expansion/
  ├── lecciones_md/      241  (cada lección exportada a Markdown con su quiz)
  ├── quizzes_html/      241  (quiz interactivo offline por lección, autocorrección)
  ├── flashcards/        482  (una tarjeta JSON por pregunta: frente/reversa/explicación)
  ├── ejercicios/        241  (ejercicio práctico guiado por lección, con lenguaje correcto)
  ├── resumenes/         241  (cheatsheet por lección: idea central + autoexamen)
  ├── glosario/          241  (términos clave → definición, extraídos de los quizzes)
  ├── errores_comunes/   241  (confusiones típicas por lección, de las opciones falsas)
  ├── ai_prompts/        241  (5 prompts listos para profundizar cada lección con IA)
  ├── tests/             241  (quiz en JSON máquina por lección, para auto-graders)
  ├── proyectos/         246  (6 guías de proyecto por curso, centradas en lecciones ancla)
  ├── roadmap/            41  (hoja de ruta printable por curso, con checklist)
  ├── plan_diario/       364  (plan día a día: año completo de estudio, 52 semanas)
  ├── retos_diarios/     365  (un reto diario que rota por todas las lecciones)
  ├── pomodoro_semanas/   52  (hoja de planificación semanal con pomodoros 🍅)
  ├── entrevistas/        41  (banco de preguntas de entrevista técnica por curso)
  ├── resumen_curso/      41  (cheatsheet maestro consolidado por curso)
  └── mapas_mentales/     41  (mapa mental en texto: jerarquía de conceptos)

Uso:  python3 expandir_contenido.py          (regenera todo, idempotente)
"""
import sys, json, datetime, unicodedata, re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import main  # fuente única de verdad: CURSOS y QUIZZES de la app

CURSOS, QUIZZES = main.CURSOS, main.QUIZZES
ROOT = Path(__file__).parent / "expansion"
HOY = datetime.date.today()
ESCRITOS = 0


def slug(texto, maxima=60):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^A-Za-z0-9]+", "-", t.strip().lower()).strip("-") or "sin-nombre"
    return t[:maxima].strip("-")


def w(ruta, contenido):
    global ESCRITOS
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(contenido, encoding="utf-8")
    ESCRITOS += 1


LANG = [
    ("python", "python"), ("pandas", "python"), ("machine", "python"),
    ("postgresql", "sql"), ("sql", "sql"),
    ("javascript", "javascript"), ("node", "javascript"), ("react", "jsx"),
    ("typescript", "typescript"), ("angular", "typescript"), ("svelte", "svelte"),
    ("html", "html"), ("css", "css"),
    ("java", "java"), ("spring", "java"), ("php", "php"), ("laravel", "php"),
    ("ruby", "ruby"), ("rails", "ruby"), ("go —", "go"), ("rust", "rust"),
    (".net", "csharp"), ("c#", "csharp"), ("c++", "cpp"), ("c y", "c"),
    ("kotlin", "kotlin"), ("swift", "swift"), ("flutter", "dart"),
    ("docker", "dockerfile"), ("git", "bash"), ("ci/cd", "bash"),
    ("linux", "bash"), ("terminal", "bash"), ("servidor", "bash"),
    ("devops", "yaml"), ("r —", "r"), ("r y", "r"),
]
EXT = {"python": "py", "javascript": "js", "typescript": "ts", "jsx": "jsx", "sql": "sql",
       "html": "html", "css": "css", "java": "java", "php": "php", "ruby": "rb",
       "go": "go", "rust": "rs", "csharp": "cs", "cpp": "cpp", "c": "c",
       "kotlin": "kt", "swift": "swift", "dart": "dart", "r": "r",
       "dockerfile": "Dockerfile", "bash": "sh", "yaml": "yml", "svelte": "svelte", "text": "txt"}


def lenguaje(curso):
    c = curso.lower()
    for clave, lang in LANG:
        if clave in c:
            return lang
    return "text"


def quiz_leccion(curso, idx):
    return QUIZZES.get(curso, {}).get(idx, [])


def f_leccion_md(curso, idx, lec, quiz):
    qs = ""
    for i, q in enumerate(quiz, 1):
        qs += f"\n### {i}. {q['p']}\n" + "\n".join(
            f"- {['A','B','C','D','E','F'][j]}) {o}" for j, o in enumerate(q["ops"]))
    resp = ""
    for i, q in enumerate(quiz, 1):
        resp += f"\n**{i}.** ✅ {q['ops'][q['ok']]} — {q['exp']}"
    return f"""# {lec['titulo']}

> 📚 Curso: **{curso}** · Lección {idx + 1} de {len(CURSOS[curso])}
> 🗓 Exportado: {HOY:%d/%m/%Y} desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```{lenguaje(curso)}
{lec['contenido']}
```

---

## 📝 Quiz de la lección
{qs}

---

## 🔑 Respuestas y explicaciones
{resp}

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
"""


def f_quiz_html(curso, idx, lec, quiz):
    data = json.dumps(quiz, ensure_ascii=False)
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quiz — {lec['titulo']}</title>
<style>
body{{font-family:system-ui,sans-serif;max-width:680px;margin:2rem auto;padding:0 1rem;background:#0d1117;color:#e6edf3}}
.op{{display:block;width:100%;margin:.4rem 0;padding:.8rem;text-align:left;border:1px solid #30363d;border-radius:8px;background:#161b22;color:#e6edf3;cursor:pointer;font-size:1rem}}
.op:hover{{border-color:#58a6ff}} .bien{{background:#1a7f37;border-color:#2ea043}} .mal{{background:#8c2f39;border-color:#cf6679}}
.exp{{background:#161b22;border-left:3px solid #58a6ff;padding:.6rem;border-radius:0 8px 8px 0;margin:.6rem 0;display:none}}
.boton{{padding:.7rem 1.4rem;border-radius:8px;border:0;background:#238636;color:#fff;font-size:1rem;cursor:pointer}}
small{{color:#8b949e}}
</style></head><body>
<small>📚 {curso} · Lección {idx + 1}/{len(CURSOS[curso])} · Quiz offline · {HOY:%d/%m/%Y}</small>
<h1>📝 {lec['titulo']}</h1>
<div id="app"></div>
<script>
const Q = {data};
let i = 0, puntos = 0, respondida = false;
const app = document.getElementById('app');
function pintar() {{
  if (i >= Q.length) {{
    app.innerHTML = `<h2>🏁 ${{puntos}}/${{Q.length}} (${{Math.round(puntos/Q.length*100)}}%)</h2>
      <p>${{puntos === Q.length ? '🏆 ¡Perfecto! Marca la lección con ✅ en la app.' : '🔁 Repasa y reintenta hasta el 100%.'}}</p>
      <button class="boton" onclick="i=0;puntos=0;pintar()">Reintentar quiz</button>`;
    return;
  }}
  const q = Q[i]; respondida = false;
  app.innerHTML = `<h3>Pregunta ${{i+1}} de ${{Q.length}}</h3><p>${{q.p}}</p>` +
    q.ops.map((o, j) => `<button class="op" id="op${{j}}" onclick="elegir(${{j}})">${{o}}</button>`).join('') +
    `<div class="exp" id="exp"><b>💡</b> ${{q.exp}}</div>`;
}}
function elegir(j) {{
  if (respondida) return; respondida = true;
  const q = Q[i];
  document.getElementById('op' + j).className = 'op ' + (j === q.ok ? 'bien' : 'mal');
  if (j === q.ok) puntos++; else document.getElementById('op' + q.ok).classList.add('bien');
  document.getElementById('exp').style.display = 'block';
  app.innerHTML += `<br><button class="boton" onclick="i++;pintar()">Siguiente ➜</button>`;
}}
pintar();
</script></body></html>"""


def f_flashcard(curso, idx, num_q, q):
    return json.dumps({
        "tarjeta": f"{slug(curso, 30)}-L{idx + 1:02d}-Q{num_q:02d}",
        "curso": curso, "leccion": idx + 1,
        "frente": q["p"], "reversa": q["ops"][q["ok"]],
        "explicacion": q["exp"],
        "algoritmo": "repaso espaciado: 1d, 3d, 7d, 21d",
        "generada": HOY.isoformat(),
    }, ensure_ascii=False, indent=2)


def f_ejercicio(curso, idx, lec):
    lang = lenguaje(curso)
    tema = lec['titulo'].split('. ', 1)[-1]
    return f"""# 🛠 Ejercicio práctico — {lec['titulo']}

> 📚 {curso} · Lección {idx + 1} · 🍅 1-2 pomodoros · Método: aprender construyendo

## 🎯 Objetivo
Construir un ejemplo REAL y ejecutable que demuestre que puedes usar:
**{tema}** — sin copiar y pegar de la lección.

## 📋 Pasos
1. **Recuerda**: cierra la lección e intenta escribir la idea central en una frase.
2. **Construye**: crea un archivo nuevo (`ejercicio.{EXT.get(lang, 'txt')}`) y escribe el código desde cero.
3. **Prueba**: ejecútalo. Si falla, depura leyendo el error — eso también es aprender.
4. **Rompe**: introduce un error a propósito y observa qué pasa.
5. **Reconstruye**: borra el archivo y rehazlo sin mirar. Si no puedes → relee y repite.

```{lang}
# Plantilla de inicio (borra este comentario y escribe tu propio código)
# Tema: {lec['titulo']}
```

## ✅ Criterio de éxito
- [ ] El código funciona sin errores
- [ ] Puedo explicar cada línea en voz alta
- [ ] Pasé el quiz de la lección con 100% (🏆)
- [ ] Guardé el archivo en mi carpeta de proyectos
"""


def f_resumen(curso, idx, lec, quiz):
    idea = lec["contenido"].split("\n", 1)[0][:300]
    autoexamen = "\n".join(f"- **{q['p']}** → {q['ops'][q['ok']]} _({q['exp']})_" for q in quiz)
    return f"""# ⚡ Cheatsheet — {lec['titulo']}

> {curso} · Lección {idx + 1} · {HOY:%d/%m/%Y}

## 💡 Idea central
{idea}

## 🧠 Autoexamen (tápate la respuesta)
{autoexamen}

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
"""


def f_glosario(curso, idx, lec, quiz):
    entradas, vistos = [], set()
    for q in quiz:
        term = q["ops"][q["ok"]].strip()
        if term.lower() not in vistos:
            vistos.add(term.lower())
            entradas.append(f"- **{term}** — {q['exp']}")
    if not entradas:
        entradas.append(f"- **{lec['titulo']}** — concepto central de esta lección; explícalo con tus palabras.")
    return f"""# 📖 Glosario — {lec['titulo']}

> {curso} · Lección {idx + 1} · Términos que debes poder definir sin mirar

{chr(10).join(entradas)}

✍️ Ejercicio: añade debajo TU propia definición de cada término.
"""


def f_errores(curso, idx, lec, quiz):
    items = []
    for q in quiz:
        erradas = [o for j, o in enumerate(q["ops"]) if j != q["ok"]][:2]
        for o in erradas:
            items.append(f"- ❌ «{o}» → Frente a «{q['p']}» lo fácil es confundirse. **Verdad**: {q['ops'][q['ok']]}. {q['exp']}")
    if not items:
        items.append("- Error n.º 1: leer sin practicar. Abre el editor y escribe código.")
    return f"""# ⚠️ Errores comunes — {lec['titulo']}

> {curso} · Lección {idx + 1} · Aprender de los errores (propios y ajenos)

{chr(10).join(items)}

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
"""


def f_ai_prompts(curso, idx, lec):
    tema = lec["titulo"].split(". ", 1)[-1]
    return f"""# 🤖 Prompts para profundizar — {lec['titulo']}

> {curso} · Lección {idx + 1} · Cópialos en tu chat IA (Ollama local o el que uses)

1. **Explica simple**: «Explica {tema} como si tuviera 12 años, con una analogía de la vida real y un ejemplo mínimo.»
2. **Sócrates**: «Hazme 3 preguntas sobre {tema}, una por una, espera mis respuestas y al final dime qué me falta.»
3. **Mini-proyecto**: «Dame un mini-proyecto de 1 hora que use {tema}, con requisitos claros y sin darme el código.»
4. **Code review**: «Actúa como revisor senior: pídeme mi código donde uso {tema} y señala errores y mejoras.»
5. **Comparativa**: «Compara {tema} con 2 alternativas: cuándo usar cada una y errores típicos de cada opción.»
"""


def f_test_json(curso, idx, lec, quiz):
    return json.dumps({
        "curso": curso, "leccion": idx + 1, "titulo": lec["titulo"],
        "total": len(quiz), "aprobado_con": len(quiz),
        "preguntas": quiz, "generado": HOY.isoformat(),
    }, ensure_ascii=False, indent=2)


def f_proyecto(curso, n_ancla, lec_ancla, lec_apoyo):
    return f"""# 🚀 Proyecto {n_ancla}: {lec_ancla['titulo'].split('. ', 1)[-1]}

> 📚 {curso} · Ancla: lección «{lec_ancla['titulo']}» · Apoyo: «{lec_apoyo['titulo']}»
> 🍅 Presupuesto: 4-6 pomodoros · Filosofía: aprender construyendo

## 🎯 Mi reto
Construir un proyecto pequeño pero TERMINADO que use de verdad los dos conceptos ancla.
Debe tener: entrada → procesamiento → salida visible.

## 📦 Entregables
- [ ] Código en `proyectos/{slug(curso)}/proyecto-{n_ancla:02d}/`
- [ ] `LEEME.md` explicando cómo ejecutarlo y qué aprendí
- [ ] 2 errores documentados (error → causa → fix)
- [ ] Screenshot o salida de ejemplo

## 🪜 Ruta sugerida
1. Relee las lecciones ancla y apoyo (10 min, tomando notas).
2. Escribe el README ANTES del código (define qué construyes).
3. Versión mínima funcionando → luego mejora.
4. Pide a la IA local revisión (usa los prompts del módulo ai_prompts/).

## ⏫ Extensión (si quedó fácil)
Añade una función que NO aparezca en las lecciones: búscala en la documentación oficial.
"""


def f_roadmap(curso):
    total = len(CURSOS[curso])
    n_q = sum(len(QUIZZES.get(curso, {}).get(i, [])) for i in range(total))
    checks = "\n".join(f"- [ ] {i + 1}. {CURSOS[curso][i]['titulo']}" for i in range(total))
    return f"""# 🗺 Roadmap — {curso}

> {total} lecciones · {n_q} preguntas de quiz · 6 proyectos guía · Certificado al 100%

## 🎯 Meta
Certificado 🎓 = todas las lecciones ✅ + todos los quizzes 🏆 (al 100%)

## 📚 Checklist de lecciones
{checks}

## 🚀 Proyectos
- [ ] Completar las 6 guías de `proyectos/{slug(curso)}/`

## 🔥 Hábito
- Racha diaria (🔥) · Mínimo 2 🍅/día · Reintentar quizzes hasta 100%
"""


def f_plan_dia(dia, asigna):
    return f"""# 🗓 Día {dia:03d} del plan anual

> Plan: 52 semanas, ~6 días de ritmo + 1 de descanso.
> Regla de oro: mejor 25 minutos diarios 🔥 que 3 horas el domingo.

{asigna}

## 🍅 Pomodoros mínimos: 2
## 📝 Al cerrar el día
- [ ] Marqué qué estudié · quizzes intentados (meta 100%)
- [ ] Racha 🔥 mantenida · Anoté 1 idea nueva en mi bitácora
"""


def f_reto(dia, curso, idx, lec, quiz):
    desafio = quiz[0] if quiz else None
    extra = ""
    if desafio:
        extra = f"""
## 🥊 Desafío exprés (sin mirar)
**{desafio['p']}**

<details><summary>👁 Ver respuesta</summary>

✅ {desafio['ops'][desafio['ok']]} — {desafio['exp']}
</details>
"""
    return f"""# 🥊 Reto del día {dia:03d}

> Hoy tu cerebro ataca: **{lec['titulo']}** ({curso})

1. Explica en voz alta este tema durante 2 minutos, sin notas.
2. Relee la lección solo si el paso 1 trabó.
3. Reescribe desde cero el ejemplo clave de la lección.
{extra}
💰 Vale 1 punto de maestría. Acumula 30 → date un premio real.
"""


def f_entrevistas(curso):
    """Banco de preguntas de entrevista: 2 del quiz + genéricas por tema."""
    preguntas_quiz = []
    for i in range(len(CURSOS[curso])):
        for q in quiz_leccion(curso, i):
            preguntas_quiz.append(q)
    intro = random_placeholder(curso)
    lineas = [f"# 🎤 Banco de entrevista — {curso}\n",
              f"> {len(preguntas_quiz)} preguntas esenciales + guía de respuestas las que ya sabes del curso\n"]
    lineas.append("## 🔥 Fundamentales (del contenido del curso)\n")
    for i, q in enumerate(preguntas_quiz, 1):
        lineas.append(f"{i}. **{q['p']}**\n   - {q['ops'][q['ok']]}  _({q['exp']})_\n")
    lineas.append(intro)
    return "\n".join(lineas)


def random_placeholder(curso):
    return f"""## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve {curso.split('—')[0].strip()} y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta {curso.split('—')[0].strip()} con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
"""


def f_resumen_curso(curso):
    """Cheatsheet maestro consolidado del curso: 1 idea por lección."""
    bloques = [f"# 📕 Resumen maestro — {curso}\n",
               "> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.\n"]
    for i, lec in enumerate(CURSOS[curso]):
        idea = lec["contenido"].replace("\n", " ")[:180]
        bloques.append(f"## {i + 1}. {lec['titulo']}\n{idea}…\n")
    preguntas = sum(len(quiz_leccion(curso, i)) for i in range(len(CURSOS[curso])))
    bloques.append(f"---\n✅ {len(CURSOS[curso])} lecciones · 📝 {preguntas} preguntas de repaso en quizzes_html/ · tests/")
    return "\n".join(bloques)


def f_mapa_mental(curso):
    """Mapa mental en texto indentado: jerarquía del conocimiento del curso."""
    partes = [f"# 🧠 Mapa mental — {curso}\n", f"```\n{curso}"]
    for i, lec in enumerate(CURSOS[curso]):
        tema = lec["titulo"].split('. ', 1)[-1]
        horizontal = "├─" if i < len(CURSOS[curso]) - 1 else "└─"
        partes.append(f"{horizontal} {tema}")
        quiz = quiz_leccion(curso, i)
        for q in quiz[:1]:
            partes.append(f"│   └─ 💬 {q['p'][:70]}")
    partes.append("```\n\n🖨 Versión imprimible para tu pared: jerarquía = recorrido visual de memoria.")
    return "\n".join(partes)


def f_pomodoro_sem(sem, lecciones_texto):
    return f"""# 🍅 Plan de la semana {sem:02d} (52)

> Lecciones recomendadas esta semana: {lecciones_texto}

| Día | 🍅 meta | Bloque sugerido | Hecho |
|-----|--------|-----------------|-------|
| Lun | 3 | Lección nueva + quiz | ☐ |
| Mar | 3 | Lección nueva + ejercicio | ☐ |
| Mié | 3 | Lección nueva + quiz | ☐ |
| Jue | 3 | Proyecto del curso | ☐ |
| Vie | 2 | Repaso flashcards + reto | ☐ |
| Sáb | 2 | Quizzes hasta 100% + bitácora | ☐ |
| Dom | 0 | 😴 Descanso | ☐ |

**Meta semanal**: mantener la racha 🔥 los 7 días. Revisa tu racha en 🏠 Inicio de la app.
"""


def main_gen():
    cursos = list(CURSOS.keys())
    slugs = {}
    for c in cursos:
        s = slug(c, 44)
        base = s
        n = 2
        while s in slugs.values():
            s = f"{base}-{n}"; n += 1
        slugs[c] = s

    flat = [(c, i, CURSOS[c][i]) for c in cursos for i in range(len(CURSOS[c]))]

    for curso in cursos:
        lecciones = CURSOS[curso]
        for i, lec in enumerate(lecciones):
            quiz = quiz_leccion(curso, i)
            base = f"{slugs[curso]}/L{i + 1:02d}-{slug(lec['titulo'], 38)}"
            w(ROOT / "lecciones_md" / f"{base}.md", f_leccion_md(curso, i, lec, quiz))
            w(ROOT / "quizzes_html" / f"{base}.html", f_quiz_html(curso, i, lec, quiz))
            for nq, q in enumerate(quiz, 1):
                w(ROOT / "flashcards" / slugs[curso] / f"fc-L{i + 1:02d}-Q{nq:02d}.json", f_flashcard(curso, i, nq, q))
            w(ROOT / "ejercicios" / f"{base}.md", f_ejercicio(curso, i, lec))
            w(ROOT / "resumenes" / f"{base}.md", f_resumen(curso, i, lec, quiz))
            w(ROOT / "glosario" / f"{base}.md", f_glosario(curso, i, lec, quiz))
            w(ROOT / "errores_comunes" / f"{base}.md", f_errores(curso, i, lec, quiz))
            w(ROOT / "ai_prompts" / f"{base}.md", f_ai_prompts(curso, i, lec))
            w(ROOT / "tests" / f"{base}.json", f_test_json(curso, i, lec, quiz))

    for curso in cursos:
        total = len(CURSOS[curso])
        for p in range(1, 7):
            i_ancla = (p - 1) * total // 6
            i_apoyo = (i_ancla + 1) % total
            tema = slug(CURSOS[curso][i_ancla]["titulo"].split(". ", 1)[-1], 34)
            w(ROOT / "proyectos" / slugs[curso] / f"proyecto-{p:02d}-{tema}.md",
              f_proyecto(curso, p, CURSOS[curso][i_ancla], CURSOS[curso][i_apoyo]))

    for curso in cursos:
        w(ROOT / "roadmap" / f"{slugs[curso]}.md", f_roadmap(curso))
        w(ROOT / "entrevistas" / f"{slugs[curso]}.md", f_entrevistas(curso))
        w(ROOT / "resumen_curso" / f"{slugs[curso]}.md", f_resumen_curso(curso))
        w(ROOT / "mapas_mentales" / f"{slugs[curso]}.md", f_mapa_mental(curso))

    n = len(flat)
    for d in range(1, 365):
        if d <= n:
            c, i, lec = flat[d - 1]
            asigna = (f"## 📚 Lección del día\n**{lec['titulo']}** — {c}\n\n"
                      f"- [ ] Leer en app (📚 Aprender) · [ ] Ejercicio de `ejercicios/` · [ ] Quiz 📝 hasta 100%\n"
                      f"- [ ] Flashcards del tema en `flashcards/`")
        else:
            rot = flat[(d - 1) % n]
            asigna = (f"## 🔁 Día de consolidación\nNo hay lección nueva: modo proyecto/repaso.\n\n"
                      f"- [ ] Repasa 10 flashcards de cursos terminados\n"
                      f"- [ ] Repite el quiz de «{rot[2]['titulo']}» hasta 100%\n"
                      f"- [ ] Avanza un proyecto de `proyectos/`")
        w(ROOT / "plan_diario" / f"dia-{d:03d}.md", f_plan_dia(d, asigna))

    for d in range(1, 366):
        c, i, lec = flat[(d - 1) % n]
        w(ROOT / "retos_diarios" / f"reto-{d:03d}.md", f_reto(d, c, i, lec, quiz_leccion(c, i)))

    por_sem = max(1, n // 52)
    for s in range(1, 53):
        tramo = flat[(s - 1) * por_sem: s * por_sem]
        texto = (f"{len(tramo)} («{tramo[0][2]['titulo'].split('. ', 1)[0]}» … «{tramo[-1][2]['titulo'].split('. ', 1)[0]}»)"
                 if tramo else "proyectos y consolidación")
        w(ROOT / "pomodoro_semanas" / f"semana-{s:02d}.md", f_pomodoro_sem(s, texto))

    print(f"✅ Expansión generada: {ESCRITOS} archivos en {ROOT}")


if __name__ == "__main__":
    main_gen()
