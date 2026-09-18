# 14. Librería estándar: 10 joyas incluidas

> 📚 Curso: **Python — De Cero a Profesional** · Lección 14 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
LA STDLIB: BATERÍAS INCLUIDAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  import datetime
  hoy = datetime.date.today() · datetime.datetime.now() · (fecha - otra).days

  import random
  random.choice(lista) · random.randint(1, 6) · random.shuffle(lista) · random.sample(lista, 3)

  import json     ·  import re (regex)   ·  import os (sistema)   ·  sys (argumentos: sys.argv)

  from pathlib import Path                    # rutas MODERNAS (reemplaza os.path)
  Path.home() / "proyectos" / "notas.txt"; p.read_text(); p.exists(); p.glob("*.py")

  import requests? (externa la única: pip install requests) — http GET en una línea.

  from collections import Counter, defaultdict
  Counter("banana")                      → cuenta letras automáticamente
  defaultdict(list)                      → dict con default lista (sin KeyError)

  import statistics; statistics.mean(numeros)
  import subprocess; subprocess.run(["ls"])

REGLA DEL PROFESIONAL: antes de escribir código, busca si stdlib ya lo hace. 9 de cada 10 veces sí.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué aporta Path de pathlib frente a strings de rutas?
- A) Solo estética
- B) Rutas portables Windows/Linux con operadores / y métodos read_text/exists
- C) Velocidad
- D) Compresión
### 2. Counter('banana') devuelve...
- A) Una lista
- B) {'a': 3, 'n': 2, 'b': 1} — conteo automático
- C) 'bn'
- D) Error

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Rutas portables Windows/Linux con operadores / y métodos read_text/exists — p = Path.home() / 'x' funciona igual en todos los SO — el estándar moderno de Python.
**2.** ✅ {'a': 3, 'n': 2, 'b': 1} — conteo automático — collections.Counter = histograma listo con una línea.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
