# 2. Capturar grupos y.los casos reales: validación y extracción

> 📚 Curso: **Expresiones Regulares — El Lenguaje de Patrones** · Lección 2 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
CAPTURAR SUSTANCIAS (LO QUE BUSCAS EXTRAER)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
GRUPOS CON NOMBRES (legibilidad máxima)
  patron = re.compile(r"(?P<usuario>[\w.]+)@(?P<dominio>[\w.]+\.\w+)")
  m = patron.search("mi email es ada@example.com")
  m.group("usuario")   → "ada"   ·   m.group("dominio") → "example.com"

CASOS DE TRABAJO REAL (los que pedirás toda la vida)
1. VALIDAR FORMATO (no quiere decir verdad del email solo forma):
   r"^[\w.-]+@[\w-]+\.[\w.]+$"               → email razonable
   r"^\+?\d{1,4}[\s.-]?\(?\d{2,4}\)?[\s\d.-]{7,}$"  → teléfono laxo
   r"^(?=.*[A-Z])(?=.*\d).{8,}$"              → contraseña con lookahead (mayúscula+número, 8+)
2. EXTRAER: fechas en logs, ids de URLs (r"/users/(\d+)"), precios (r"\$\s?([\d,]+)"),
   IPs (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
3. REEMPLAZAR con grupos: re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\2-\1", fecha)

SCRIPT REAL DIARIO: re.sub sobre un CSV/log gigante te sustituye horas de find-and-replace manual.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace (?P<nombre>...) en Python regex?
- A) Nada especial
- B) Grupo NOMBRADO: extraes por m.group('nombre') en vez de factores posición brittle
- C) Ordena
- D) Exporta
### 2. ¿Qué logra el lookahead (?=.*[A-Z]) en la contraseña?
- A) Neutro
- B) VERIFICA sin consumir: exige que exista una mayúscula en lo que sigue sin avanzar el cursor
- C) Ordena letras
- D) Es bug

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Grupo NOMBRADO: extraes por m.group('nombre') en vez de factores posición brittle — Regex autocomentados: los nombres documentan cada parte que capturas.
**2.** ✅ VERIFICA sin consumir: exige que exista una mayúscula en lo que sigue sin avanzar el cursor — Lookaheads = 'debe cumplirse X adelante': validaciones compuestas sin complicar los grupos.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
