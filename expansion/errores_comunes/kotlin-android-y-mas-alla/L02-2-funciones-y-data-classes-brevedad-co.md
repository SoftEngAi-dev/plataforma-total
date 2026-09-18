# ⚠️ Errores comunes — 2. Funciones y data classes: brevedad con tipos

> Kotlin — Android y Más Allá · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Solo getters» → Frente a «¿Qué genera automáticamente una data class?» lo fácil es confundirse. **Verdad**: equals(), hashCode(), toString(), copy() y componentN() — todo el boilerplate de datos. Una línea reemplaza 50 de Java: define campos y listo.
- ❌ «SQL» → Frente a «¿Qué genera automáticamente una data class?» lo fácil es confundirse. **Verdad**: equals(), hashCode(), toString(), copy() y componentN() — todo el boilerplate de datos. Una línea reemplaza 50 de Java: define campos y listo.
- ❌ «Un error» → Frente a «En listOf(1,2,3).map { it * 2 }, ¿qué es 'it'?» lo fácil es confundirse. **Verdad**: El parámetro implícito de la lambda cuando hay uno solo. Lambdas de un parámetro pueden usar 'it' sin declararlo — típico estilo Kotlin.
- ❌ «Un global» → Frente a «En listOf(1,2,3).map { it * 2 }, ¿qué es 'it'?» lo fácil es confundirse. **Verdad**: El parámetro implícito de la lambda cuando hay uno solo. Lambdas de un parámetro pueden usar 'it' sin declararlo — típico estilo Kotlin.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
