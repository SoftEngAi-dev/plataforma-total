# 11. Comprensiones avanzadas y lambda: código que se lee

> 📚 Curso: **Python — De Cero a Profesional** · Lección 11 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
AZÚCAR PITÓNICO DE VERDAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPREHENSIONS CON FILTRO DOBLE Y DICCIONARIOS
  resultado = {n: "par" if n % 2 == 0 else "impar" for n in range(6)}
  listas  = [[1,2],[3,4]]
  plana   = [x for sub in listas for x in sub]     → [1,2,3,4]

LAMBDA (funciones mini de UNA expresión: solo cuando claramente hace más legible)
  doble = lambda x: x * 2
  sorted(palabras, key=lambda p: len(p))           # ordenar por largo
  max(alumnos, key=lambda a: a["edad"])             # el mayor

FUNCS QUE SUSTITUYEN lambdas (stdlib siempre gana)
  from operator import itemgetter
  sorted(alumnos, key=itemgetter("edad"))           # mejor
  sum() · any() · all() · zip() · map()/filter() (pero las comprehensions ganan)

ANY/ALL — lógica declarativa:
  all(u["activo"] for u in usuarios)     # ¿todos activos?
  any("@" in e for e in emails)          # ¿alguno tiene @?

ZIP — recorrer en paralelo:
  for nombre, nota in zip(nombres, notas): ...
```

---

## 📝 Quiz de la lección

### 1. all() y any() con generador hacen...
- A) Loops normales
- B) Lógica declarativa: ¿todos/alguno cumplen? — sin bucles explícitos
- C) Suma de listas
- D) Nada útil
### 2. ¿Cuándo usar lambda?
- A) Siempre
- B) Funciones de una expresión triviales pasadas a key= y similares; en todo otro caso, def
- C) Nunca
- D) En clases

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Lógica declarativa: ¿todos/alguno cumplen? — sin bucles explícitos — all(x > 0 for x in nums) se lee como español: todos mayores a cero.
**2.** ✅ Funciones de una expresión triviales pasadas a key= y similares; en todo otro caso, def — Si necesita nombre para entenderse, ese nombre es su def.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
