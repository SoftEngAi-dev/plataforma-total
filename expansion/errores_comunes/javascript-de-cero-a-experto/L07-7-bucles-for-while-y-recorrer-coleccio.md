# ⚠️ Errores comunes — 7. Bucles: for, while y recorrer colecciones

> JavaScript — De Cero a Experto · Lección 7 · Aprender de los errores (propios y ajenos)

- ❌ «for clásico con índice» → Frente a «¿Cuál es la forma moderna recomendada de recorrer un array?» lo fácil es confundirse. **Verdad**: for...of. for...of es directo y seguro; for...in es para CLAVES de objetos, no arrays.
- ❌ «for...in» → Frente a «¿Cuál es la forma moderna recomendada de recorrer un array?» lo fácil es confundirse. **Verdad**: for...of. for...of es directo y seguro; for...in es para CLAVES de objetos, no arrays.
- ❌ «Rompe el bucle» → Frente a «¿Qué hace continue?» lo fácil es confundirse. **Verdad**: Salta a la siguiente iteración. Omite el resto del bloque en esta vuelta y sigue con la próxima.
- ❌ «Termina la función» → Frente a «¿Qué hace continue?» lo fácil es confundirse. **Verdad**: Salta a la siguiente iteración. Omite el resto del bloque en esta vuelta y sigue con la próxima.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
