# ⚠️ Errores comunes — 8. Transiciones y micro-interacciones

> HTML y CSS — Diseño Web Total · Lección 8 · Aprender de los errores (propios y ajenos)

- ❌ «width y height» → Frente a «¿Qué propiedades se deben animar para rendimiento fluido?» lo fácil es confundirse. **Verdad**: transform y opacity. Solo esas dos no provocan reflow/repaint del layout: la GPU las acelera.
- ❌ «top y left» → Frente a «¿Qué propiedades se deben animar para rendimiento fluido?» lo fácil es confundirse. **Verdad**: transform y opacity. Solo esas dos no provocan reflow/repaint del layout: la GPU las acelera.
- ❌ «2-3 segundos» → Frente a «¿Qué duración se siente natural en micro-interacciones de UI?» lo fácil es confundirse. **Verdad**: 150-300ms. Suficiente para percibirse, corto para no frenar.
- ❌ «Lo máximo posible» → Frente a «¿Qué duración se siente natural en micro-interacciones de UI?» lo fácil es confundirse. **Verdad**: 150-300ms. Suficiente para percibirse, corto para no frenar.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
