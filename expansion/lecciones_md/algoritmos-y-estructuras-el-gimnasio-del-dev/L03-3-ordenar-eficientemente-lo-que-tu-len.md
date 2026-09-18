# 3. Ordenar eficientemente: lo que tu lenguaje hace por ti

> 📚 Curso: **Algoritmos y Estructuras — El Gimnasio del Dev** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
SORT: POR QUÉ NINGUN PRO ESCRIBE EL SUYO (PERO SABE QUÉ PASA ABAJO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
sorted(lista) / lista.sort() → Timsort (Python) / variantes: O(n log n) GARANTIZADO, adaptado, estable — siempre gana a escribir uno.

¿CÓMO FUNCIONA UNO RÁPIDO ABSTRACTO? (merge sort en espíritu)
  divide la lista a la mitad recursivamente → ordena cada mitad (listas de 1 siempre ordenadas) → MERGE de dos ordenadas en O(n)
  total: O(n log n) — el límite matemático para ordenamiento por comparación.

  def merge_sort(lista):
      if len(lista) <= 1: return lista
      medio = len(lista) // 2
      izq, der = merge_sort(lista[:medio]), merge_sort(lista[medio:])
      # merge dos listas ordenadas:
      resultado, i, j = [], 0, 0
      while i < len(izq) and j < len(der):
          if izq[i] <= der[j]: resultado.append(izq[i]); i += 1
          else: resultado.append(der[j]); j += 1
      return resultado + izq[i:] + der[j:]

ESTABLE = preserva orden original de elementos iguales (sort por edad luego nombre: estudiantes iguales conservan orden previo).
ORDENAR CON CLAVE (el truco pro): sorted(personas, key=lambda p: (-p.edad, p.nombre)) → por edad DESC luego nombre ASC.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué complejidad garantiza un sort moderno (Timsort/Timsort-like)?
- A) O(n²)
- B) O(n log n) en el peor caso, con adaptación en datos casi ordenados
- C) O(n)
- D) O(1)
### 2. ¿Cómo ordenar por edad descendente y desempatar por nombre?
- A) 2 sorts
- B) sorted(personas, key=lambda p: (-p.edad, p.nombre)) con tupla ascendente/descendente del mismo sort
- C) No se puede
- D) filter

---

## 🔑 Respuestas y explicaciones

**1.** ✅ O(n log n) en el peor caso, con adaptación en datos casi ordenados — Por eso los algoritmos de librería estándar superan siempre al casero.
**2.** ✅ sorted(personas, key=lambda p: (-p.edad, p.nombre)) con tupla ascendente/descendente del mismo sort — Tuplas en key: orden multi-nivel en UNA Llamada, elegante y estable.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
