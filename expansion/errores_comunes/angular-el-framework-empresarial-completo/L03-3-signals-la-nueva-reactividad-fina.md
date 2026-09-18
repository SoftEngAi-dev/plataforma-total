# ⚠️ Errores comunes — 3. Signals: la nueva reactividad fina

> Angular — El Framework Empresarial Completo · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Ninguno» → Frente a «¿Qué problema resuelven los signals respecto a Zone.js?» lo fácil es confundirse. **Verdad**: Detección de cambios quirúrgica: solo se actualiza lo que usa el signal, sin escanear toda la app. Rendimiento por reacción fina: ganancia real en apps grandes y código más claro.
- ❌ «Sintaxis corta» → Frente a «¿Qué problema resuelven los signals respecto a Zone.js?» lo fácil es confundirse. **Verdad**: Detección de cambios quirúrgica: solo se actualiza lo que usa el signal, sin escanear toda la app. Rendimiento por reacción fina: ganancia real en apps grandes y código más claro.
- ❌ «una función async» → Frente a «Un computed() es...» lo fácil es confundirse. **Verdad**: Un valor DERIVADO de signals que se recalcula automáticamente cuando cambian sus dependencias. Estado derivado sin lógica manual: defines la relación, Angular mantiene el valor fresco.
- ❌ «Un servicio» → Frente a «Un computed() es...» lo fácil es confundirse. **Verdad**: Un valor DERIVADO de signals que se recalcula automáticamente cuando cambian sus dependencias. Estado derivado sin lógica manual: defines la relación, Angular mantiene el valor fresco.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
