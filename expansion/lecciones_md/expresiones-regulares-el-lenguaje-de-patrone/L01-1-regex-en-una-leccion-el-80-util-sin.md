# 1. Regex en una lección: el 80% útil sin dolor

> 📚 Curso: **Expresiones Regulares — El Lenguaje de Patrones** · Lección 1 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
REGEX: PATRONES PARA TEXTOS (DIFÍCIL DE LEER, FÁCIL DE APRENDER)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESENCIA (en todos los regex modernos):
  .        cualquier carácter (excepto newline)
  \d       un dígito (0-9) · \w letra/número/_ · \s espacio (y mayúsculas = negación: \D etc.)
  [...]    clase: [aeiou] una de esas · [0-9] · [^abc] no esas · \b límite de palabra
  ^        inicio · $ fin · | alternativa · ( ) grupo

CUANTIFICADORES
  *        0 o más · + 1 o más · ? 0 o 1 (opcional)
  {n}      exactas n · {n,} al menos n · {n,m} entre n y m

EJEMPLOS EN PYTHON (se leen igual en JS/sed/grep)
  import re
  re.findall(r"\d+", "ventas: 3 a 120 y 45")           → ['3', '120', '45']
  re.search(r"\w+@\w+\.\w+", "mi correo es ada@test.com")  → encuentra el email
  re.sub(r"\s+", " ", "texto   con    muchos   espacios")     → normaliza

NOTA CRUCIAL: en Python usa r"..." (raw string: el backslash no se come).
ONLINE para probar: regex101.com (¡EXPLICA tu regex en vivo!): la forma de aprender de verdad.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué captura \d{4}-\d{2}-\d{2}?
- A) Cualquier cosa
- B) Formato fecha aproximado: 4 dígitos-guión-2 dígitos-guión-2 dígitos (2026-09-18)
- C) Emails
- D) Estampillas
### 2. ¿Qué hacen \b y () en regex?
- A) Trivia
- B) \b enmarca palabra completa ('cat' en 'concatenar' NO matchea con \bcat\b); () crea un GRUPO capturable
- C) Solo negación
- D) Comentarios

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Formato fecha aproximado: 4 dígitos-guión-2 dígitos-guión-2 dígitos (2026-09-18) — Las regex describen patrón → los números reales solo ilustran el formato esperado.
**2.** ✅ \b enmarca palabra completa ('cat' en 'concatenar' NO matchea con \bcat\b); () crea un GRUPO capturable — Límites y grupos: de patrones sueltos a coincidencias quirúrjicas.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
