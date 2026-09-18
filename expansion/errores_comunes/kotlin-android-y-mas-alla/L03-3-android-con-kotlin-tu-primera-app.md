# ⚠️ Errores comunes — 3. Android con Kotlin: tu primera app

> Kotlin — Android y Más Allá · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Crea un botón» → Frente a «¿Qué hace findViewById<Button>(R.id.miBoton)?» lo fácil es confundirse. **Verdad**: Conecta el código Kotlin con la vista definida en el XML por su id. El puente código↔layout clásico; con Jetpack Compose ya no se necesita.
- ❌ «Borra la vista» → Frente a «¿Qué hace findViewById<Button>(R.id.miBoton)?» lo fácil es confundirse. **Verdad**: Conecta el código Kotlin con la vista definida en el XML por su id. El puente código↔layout clásico; con Jetpack Compose ya no se necesita.
- ❌ «Otro lenguaje» → Frente a «¿Qué es Jetpack Compose?» lo fácil es confundirse. **Verdad**: UI declarativa de Android: describes la interfaz con funciones Kotlin y el estado la redibuja. Mismo paradigma que React/Flutter: UI = f(estado) también en Android nativo.
- ❌ «Un emulador» → Frente a «¿Qué es Jetpack Compose?» lo fácil es confundirse. **Verdad**: UI declarativa de Android: describes la interfaz con funciones Kotlin y el estado la redibuja. Mismo paradigma que React/Flutter: UI = f(estado) también en Android nativo.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
