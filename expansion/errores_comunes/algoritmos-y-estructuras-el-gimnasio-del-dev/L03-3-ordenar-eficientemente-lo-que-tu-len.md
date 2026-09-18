# ⚠️ Errores comunes — 3. Ordenar eficientemente: lo que tu lenguaje hace por ti

> Algoritmos y Estructuras — El Gimnasio del Dev · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «O(n²)» → Frente a «¿Qué complejidad garantiza un sort moderno (Timsort/Timsort-like)?» lo fácil es confundirse. **Verdad**: O(n log n) en el peor caso, con adaptación en datos casi ordenados. Por eso los algoritmos de librería estándar superan siempre al casero.
- ❌ «O(n)» → Frente a «¿Qué complejidad garantiza un sort moderno (Timsort/Timsort-like)?» lo fácil es confundirse. **Verdad**: O(n log n) en el peor caso, con adaptación en datos casi ordenados. Por eso los algoritmos de librería estándar superan siempre al casero.
- ❌ «2 sorts» → Frente a «¿Cómo ordenar por edad descendente y desempatar por nombre?» lo fácil es confundirse. **Verdad**: sorted(personas, key=lambda p: (-p.edad, p.nombre)) con tupla ascendente/descendente del mismo sort. Tuplas en key: orden multi-nivel en UNA Llamada, elegante y estable.
- ❌ «No se puede» → Frente a «¿Cómo ordenar por edad descendente y desempatar por nombre?» lo fácil es confundirse. **Verdad**: sorted(personas, key=lambda p: (-p.edad, p.nombre)) con tupla ascendente/descendente del mismo sort. Tuplas en key: orden multi-nivel en UNA Llamada, elegante y estable.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
