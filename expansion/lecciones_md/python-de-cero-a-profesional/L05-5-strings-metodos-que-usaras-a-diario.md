# 5. Strings: métodos que usarás a diario

> 📚 Curso: **Python — De Cero a Profesional** · Lección 5 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
STRINGS: INMUTABLES Y POTENTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  texto = "Hola Mundo Python"
  texto.lower() · .upper() · .title()         # casos
  texto.strip()                               # "  hola  ".strip() → limpiar edges
  texto.replace("Mundo", "Universo")
  texto.split(" ")       → ["Hola", "Mundo", "Python"]
  "-".join(["a", "b"])   → "a-b"              # une con separador
  texto.startswith("Hola") · .endswith("Python")
  "num" in texto         → False              # contiene
  texto.find("Mundo")    → 5 (-1 si no está)

INMUTABLES: cada método devuelve uno NUEVO:
  texto = texto.lower()      # reasignar si quieres el cambio

FORMATO DE FECHAS Y MILES (f-strings con poder):
  f"{precio:,.2f}"       → 1,234.56
  f"{fraccion:.1%}"      → 22.0%

SLICES también aplican: texto[::-1] invierte; texto[:4] primeros 4.
```

---

## 📝 Quiz de la lección

### 1. 'a-b-c'.split('-') devuelve...
- A) "a-b-c"
- B) ['a', 'b', 'c']
- C) ('a','b','c')
- D) Error
### 2. ¿Por qué debes reasignar texto = texto.strip()?
- A) Porque strip falla sin ella
- B) Los strings son inmutables: strip devuelve uno nuevo
- C) Por velocidad
- D) No hace falta

---

## 🔑 Respuestas y explicaciones

**1.** ✅ ['a', 'b', 'c'] — split corta en lista; el inverso es '-'.join(lista).
**2.** ✅ Los strings son inmutables: strip devuelve uno nuevo — Métodos de str NUNCA modifican el original.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
