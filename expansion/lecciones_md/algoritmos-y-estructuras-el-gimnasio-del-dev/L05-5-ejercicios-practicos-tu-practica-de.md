# 5. Ejercicios prácticos: tu práctica de juicio

> 📚 Curso: **Algoritmos y Estructuras — El Gimnasio del Dev** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
ENTRENAMIENTO REAL: 4 EJERCICIOS CLÁSICOS RESUELTOS MENTALMENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
E1 — PARÉNTESIS BALANCEADOS (stack)
  def balanceado(s):
      pila, parejas = [], {")": "(", "]": "[", "}": "{"}
      for c in s:
          if c in "([{": pila.append(c)
          elif c in ")]}":
              if not pila or pila.pop() != parejas[c]: return False
      return not pila
E2 — FRECUENCIA DE LETRA MÁXIMA (dict/contador)
  from collections import Counter
  Counter("banana").most_common(1)    → [('a', 3)]
E3 — TWO SUM (dict = evitar O(n²))
  def two_sum(nums, target):
      vistos = {}
      for i, n in enumerate(nums):
          if target - n in vistos: return [vistos[target - n], i]
          vistos[n] = i
E4 — INVERTIR LISTA O(n) SIN AYUDAS (dos punteros)
  def invertir(a):
      izq, der = 0, len(a) - 1
      while izq < der:
          a[izq], a[der] = a[der], a[izq]
          izq += 1; der -= 1

MÉTODO DE PRÁCTICA: escríbelos desde 0 sin mirar → testéalos con bordes (vacío, 1, todos iguales) → explica la complejidad en voz alta. 3 por semana = entrevistas dominadas en 3 meses.
```

---

## 📝 Quiz de la lección

### 1. Two Sum con diccionario es O(n) porque...
- A) más RAM
- B) un solo paso por datos + lookup O(1) del complemento ya visto
- C) es corto
- D) no es
### 2. Dos punteros (izq/der) hacia el centro resuelven elegantemente...
- A) Nada
- B) Invertir in-place, palíndromos, búsqueda en ordenados: patrón O(n) universal
- C) Bases de datos
- D) Regex

---

## 🔑 Respuestas y explicaciones

**1.** ✅ un solo paso por datos + lookup O(1) del complemento ya visto — Map de vistos → cada elemento se revisa UNA vez; la fuerza bruta anidada era O(n²).
**2.** ✅ Invertir in-place, palíndromos, búsqueda en ordenados: patrón O(n) universal — Pattern reconocible: dos variables convergiendo por extremos aparecen en decenas de problemas.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
