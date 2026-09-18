# 2. Tipos, variables y f-strings

> 📚 Curso: **Python — De Cero a Profesional** · Lección 2 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
LOS TIPOS DE BASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  edad = 36                  # int
  precio = 19.99             # float
  nombre = "Ada"             # str
  activo = True              # bool (¡mayúscula!)
  nada = None                # NoneType: ausencia (el null de Python)
  type(edad)                 → <class 'int'>   (pregunta su tipo)

CONVERTIR
  int("42") → 42 · float("3.14") · str(42) · bool(0) → False
  FALSY: 0, 0.0, "", [], {}, None, False

F-STRINGS: LA FORMA (desde Python 3.6)
  print(f"Me llamo {nombre} y tengo {edad} años")
  print(f"{precio:.2f}")          → 19.99 (formatos!)
  print(f"{edad * 2}")            → incluso expresiones dentro

OPERADORES: + - * / //  %  **   
  7 // 2 → 3 (entero) · 7 % 2 → 1 (residuo) · 2 ** 10 → 1024

PIP para librerías externas; para TODO lo demás, la standard library trae: math, random, datetime, json, re, os...
```

---

## 📝 Quiz de la lección

### 1. ¿Qué imprime 7 % 2?
- A) 3
- B) 0
- C) 1
- D) 3.5
### 2. ¿Qué permite la f-string?
- A) Solo texto
- B) Interpolar variables y expresiones con formato: f'{precio:.2f}'
- C) Solo variables
- D) Solo sumas

---

## 🔑 Respuestas y explicaciones

**1.** ✅ 1 — % es residuo: 7 = 2×3 + 1.
**2.** ✅ Interpolar variables y expresiones con formato: f'{precio:.2f}' — Las f-strings combinadas con especificadores de formato son el estándar moderno.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
