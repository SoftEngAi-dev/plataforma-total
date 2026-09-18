# ⚠️ Errores comunes — 5. Proyecto: suite de tests real para tu calculadora/app

> Testing — Programar con Red de Seguridad · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Código-test» → Frente a «¿Cuál secuencia TDD correcta?» lo fácil es confundirse. **Verdad**: 🔴 test que falla → 🟢 código mínimo que pase → 🔵 refactor mejorando sin romper el verde. Primero el contrato del comportamiento (test), después el código que lo cumple.
- ❌ «Test después solo» → Frente a «¿Cuál secuencia TDD correcta?» lo fácil es confundirse. **Verdad**: 🔴 test que falla → 🟢 código mínimo que pase → 🔵 refactor mejorando sin romper el verde. Primero el contrato del comportamiento (test), después el código que lo cumple.
- ❌ «feliz nomás» → Frente a «restar(-2, -3) == 1 es un test de...» lo fácil es confundirse. **Verdad**: CASO BORDE (números negativos): los pros testean fronteras, no solo caminos felices. Los bugs viven en los bordes: tu suite debe patrullarlos siempre.
- ❌ «error» → Frente a «restar(-2, -3) == 1 es un test de...» lo fácil es confundirse. **Verdad**: CASO BORDE (números negativos): los pros testean fronteras, no solo caminos felices. Los bugs viven en los bordes: tu suite debe patrullarlos siempre.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
