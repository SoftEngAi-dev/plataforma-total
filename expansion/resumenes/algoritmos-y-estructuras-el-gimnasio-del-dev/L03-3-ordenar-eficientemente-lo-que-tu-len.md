# ⚡ Cheatsheet — 3. Ordenar eficientemente: lo que tu lenguaje hace por ti

> Algoritmos y Estructuras — El Gimnasio del Dev · Lección 3 · 18/09/2026

## 💡 Idea central
SORT: POR QUÉ NINGUN PRO ESCRIBE EL SUYO (PERO SABE QUÉ PASA ABAJO)

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué complejidad garantiza un sort moderno (Timsort/Timsort-like)?** → O(n log n) en el peor caso, con adaptación en datos casi ordenados _(Por eso los algoritmos de librería estándar superan siempre al casero.)_
- **¿Cómo ordenar por edad descendente y desempatar por nombre?** → sorted(personas, key=lambda p: (-p.edad, p.nombre)) con tupla ascendente/descendente del mismo sort _(Tuplas en key: orden multi-nivel en UNA Llamada, elegante y estable.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
