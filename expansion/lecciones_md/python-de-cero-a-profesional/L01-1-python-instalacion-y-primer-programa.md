# 1. Python: instalación y primer programa

> 📚 Curso: **Python — De Cero a Profesional** · Lección 1 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
PYTHON: LEGIBLE > TODO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Instalación: python.org (marca "Add to PATH" en Windows) o sudo apt install python3.

  python3 --version
  python3 hola.py      # ejecutar
  python3              # modo interactivo (REPL) — experimenta aquí

HOLA MUNDO COMPLETO
  nombre = input("¿Tu nombre? ")       # input siempre devuelve str
  print(f"¡Hola, {nombre}!")           # f-strings: interpolación moderna

  edad = int(input("¿Edad? "))         # convertir antes de operar
  print(f"En 10 años: {edad + 10}")

FILOSOFÍA (aparece en todo): indentación = bloques de código (4 espacios, no llaves)
  if edad >= 18:
      print("mayor")          # el sangrado ES la estructura

  print() salida · input() entrada · # comentario · f"" interpolación moderna ❤

REPL para probar ideas al instante; archivos .py para guardar historias.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué delimita los bloques de código en Python?
- A) Llaves { }
- B) La indentación (sangría) de 4 espacios
- C) begin/end
- D) Punto y coma
### 2. input() devuelve siempre...
- A) int
- B) float
- C) str (hay que convertir con int()/float() para calcular)
- D) bool

---

## 🔑 Respuestas y explicaciones

**1.** ✅ La indentación (sangría) de 4 espacios — La sangría forzada hace el código universalmente legible — la idea nuclear de Python.
**2.** ✅ str (hay que convertir con int()/float() para calcular) — Fuente clásica de bugs principiantes: '5' + '5' = '55'. Convierte.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
