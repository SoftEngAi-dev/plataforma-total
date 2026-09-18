# 7. Bucles: for, range, enumerate, while

> 📚 Curso: **Python — De Cero a Profesional** · Lección 7 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
FOR: PRECIOSO EN PYTHON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  for fruta in ["🍎", "🍌", "🥝"]:          # itera directo sobre elementos
      print(fruta)

RANGE (cuentas)
  range(5)         → 0,1,2,3,4
  range(1, 6)      → 1..5
  range(10, 0, -1) → cuenta regresival

ENUMERATE (índice + elemento, EL PYTHONICO)
  for i, nombre in enumerate(nombres): print(i, nombre)

WHILE (condición, no conteo)
  n = 100
  while n > 1:
      n //= 2

CONTROL: break (salir) · continue (siguiente vuelta) · else en bucles (rara útil: si NO hubo break)

COMPREHENSIONS = bucle + transformación + filtro en 1 línea:
  [len(p) for p in palabras if len(p) > 3]

REGLA: si puedes leerlo como frase en español, es pythónico. 'for numero in numeros si es par' → comprehension de ham.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué aporta enumerate frente a range(len(lista))?
- A) Nada
- B) Índice y elemento a la vez, legible y sin errores de off-by-one
- C) Más velocidad
- D) Desempaqueta tuplas
### 2. range(2, 10, 2) genera...
- A) 2..9
- B) 2, 4, 6, 8
- C) 2, 4, 6, 8, 10
- D) Pares hasta 10 inclusive

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Índice y elemento a la vez, legible y sin errores de off-by-one — enumerate es el idioma correcto; range(len()) es el acento extranjero.
**2.** ✅ 2, 4, 6, 8 — range(inicio, fin, paso) — fin SIEMPRE excluido.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
