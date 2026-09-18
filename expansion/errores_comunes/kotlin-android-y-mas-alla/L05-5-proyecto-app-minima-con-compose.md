# ⚠️ Errores comunes — 5. Proyecto: app mínima con Compose

> Kotlin — Android y Más Allá · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué hace remember { mutableStateOf(0) }?» lo fácil es confundirse. **Verdad**: Estado que Compose observa: al cambiarlo, las funciones que lo leen se redibujan solas. El equivalente a useState de React pero nativo Android: UI reactiva real.
- ❌ «Guarda en disco» → Frente a «¿Qué hace remember { mutableStateOf(0) }?» lo fácil es confundirse. **Verdad**: Estado que Compose observa: al cambiarlo, las funciones que lo leen se redibujan solas. El equivalente a useState de React pero nativo Android: UI reactiva real.
- ❌ «Nada crucial» → Frente a «¿Qué difiere Compose de los layouts XML clásicos?» lo fácil es confundirse. **Verdad**: UI como código Kotlin declarativo (funciones + estado) en vez de XML + findViewById imperativo. Menos glue code, mismo paradigma que React/Flutter: el futuro oficial de Android.
- ❌ «Es XML igual» → Frente a «¿Qué difiere Compose de los layouts XML clásicos?» lo fácil es confundirse. **Verdad**: UI como código Kotlin declarativo (funciones + estado) en vez de XML + findViewById imperativo. Menos glue code, mismo paradigma que React/Flutter: el futuro oficial de Android.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
