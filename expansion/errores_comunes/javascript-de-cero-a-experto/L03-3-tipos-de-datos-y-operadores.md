# ⚠️ Errores comunes — 3. Tipos de datos y operadores

> JavaScript — De Cero a Experto · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Es más rápido» → Frente a «¿Por qué usar === y no ==?» lo fácil es confundirse. **Verdad**: == convierte tipos automáticamente y genera bugs sutiles; === compara valor y tipo. "5" == 5 da true; con === da false. Predicibilidad > comodidad.
- ❌ «Por estilo» → Frente a «¿Por qué usar === y no ==?» lo fácil es confundirse. **Verdad**: == convierte tipos automáticamente y genera bugs sutiles; === compara valor y tipo. "5" == 5 da true; con === da false. Predicibilidad > comodidad.
- ❌ «0» → Frente a «¿Qué valor representa la ausencia intencional?» lo fácil es confundirse. **Verdad**: null. null = 'vacío a propósito'; undefined = 'aún no se le asignó nada'.
- ❌ «''» → Frente a «¿Qué valor representa la ausencia intencional?» lo fácil es confundirse. **Verdad**: null. null = 'vacío a propósito'; undefined = 'aún no se le asignó nada'.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
