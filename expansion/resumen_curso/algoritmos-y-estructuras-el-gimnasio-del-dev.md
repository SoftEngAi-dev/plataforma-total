# 📕 Resumen maestro — Algoritmos y Estructuras — El Gimnasio del Dev

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Big O: el idioma de la eficiencia
BIG O: CUÁNTO CRECE EL COSTO CUANDO CRECEN LOS DATOS ━━━━━━━━━━━━━━━━━━━━━━━━━━━ No mide tiempo exacto, mide cómo ESCALA. Lo que importa en el mundo real.  LOS 5 QUE DEBES RECONOCE…

## 2. 2. Buscar: lineal vs binaria + el hash map
EL PROBLEMA MÁS IMPORTANTE: ENCONTRAR RÁPIDO ━━━━━━━━━━━━━━━━━━━━━━━━━━━ BÚSQUEDA LINEAL (naif): recorrer todo: O(n)   def buscar(lista, objetivo):       for i, x in enumerate(list…

## 3. 3. Ordenar eficientemente: lo que tu lenguaje hace por ti
SORT: POR QUÉ NINGUN PRO ESCRIBE EL SUYO (PERO SABE QUÉ PASA ABAJO) ━━━━━━━━━━━━━━━━━━━━━━━━━━━ sorted(lista) / lista.sort() → Timsort (Python) / variantes: O(n log n) GARANTIZADO,…

## 4. 4. Estructuras: pilas, colas y el cuándo elegirlas
ESTRUCTURA CORRECTA = PROBLEMA MEDIO RESUELTO ━━━━━━━━━━━━━━━━━━━━━━━━━━━ STACK (pila, LIFO: último en entrar, primero en salir)   pila = []; pila.append(x) ; pila.pop()   CASOS: u…

## 5. 5. Ejercicios prácticos: tu práctica de juicio
ENTRENAMIENTO REAL: 4 EJERCICIOS CLÁSICOS RESUELTOS MENTALMENTE ━━━━━━━━━━━━━━━━━━━━━━━━━━━ E1 — PARÉNTESIS BALANCEADOS (stack)   def balanceado(s):       pila, parejas = [], {")":…

---
✅ 5 lecciones · 📝 10 preguntas de repaso en quizzes_html/ · tests/