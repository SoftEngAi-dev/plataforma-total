# ⚠️ Errores comunes — 4. Corrutinas: asincronía sin dolor

> Kotlin — Android y Más Allá · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «La hace más lenta» → Frente a «¿Qué hace suspend en una función?» lo fácil es confundirse. **Verdad**: Puede pausar su ejecución sin bloquear el hilo y reanudar luego. suspend + delay = esperar sin congelar: la base de toda app Android moderna.
- ❌ «La hace pública» → Frente a «¿Qué hace suspend en una función?» lo fácil es confundirse. **Verdad**: Puede pausar su ejecución sin bloquear el hilo y reanudar luego. suspend + delay = esperar sin congelar: la base de toda app Android moderna.
- ❌ «Porque sí» → Frente a «¿Por qué lifecycleScope en Android?» lo fácil es confundirse. **Verdad**: Las corrutinas de UI se cancelan solas al destruirse la pantalla: sin fugas de memoria ni crashes. Scope atado al ciclo de vida = gestión de concurrencia automática y segura.
- ❌ «Es más rápido» → Frente a «¿Por qué lifecycleScope en Android?» lo fácil es confundirse. **Verdad**: Las corrutinas de UI se cancelan solas al destruirse la pantalla: sin fugas de memoria ni crashes. Scope atado al ciclo de vida = gestión de concurrencia automática y segura.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
