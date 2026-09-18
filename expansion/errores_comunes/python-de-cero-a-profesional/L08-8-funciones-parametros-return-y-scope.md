# ⚠️ Errores comunes — 8. Funciones: parámetros, return y scope

> Python — De Cero a Profesional · Lección 8 · Aprender de los errores (propios y ajenos)

- ❌ «Le gusta a Python» → Frente a «def f(a, b=2): — ¿por qué el default va al final?» lo fácil es confundirse. **Verdad**: Los posicionales deben venir primero para no ambiguar la llamada. f(5) debe ser claro: a=5. Con default primero sería ambiguo.
- ❌ «Velocidad» → Frente a «def f(a, b=2): — ¿por qué el default va al final?» lo fácil es confundirse. **Verdad**: Los posicionales deben venir primero para no ambiguar la llamada. f(5) debe ser claro: a=5. Con default primero sería ambiguo.
- ❌ «0» → Frente a «Sin return, una función Python devuelve...» lo fácil es confundirse. **Verdad**: None (¡cuidado al encadenar!). Caso clásico: olvidas return y luego el resultado es None donde no esperas.
- ❌ «cadena vacía» → Frente a «Sin return, una función Python devuelve...» lo fácil es confundirse. **Verdad**: None (¡cuidado al encadenar!). Caso clásico: olvidas return y luego el resultado es None donde no esperas.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
