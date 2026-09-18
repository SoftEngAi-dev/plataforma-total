# ⚠️ Errores comunes — 4. Strings: la caja de herramientas del texto

> JavaScript — De Cero a Experto · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Un string común» → Frente a «¿Qué es una plantilla literal?» lo fácil es confundirse. **Verdad**: Backticks con ${} para interpolar variables/expresiones. `Hola ${nombre}` — la forma moderna de construir texto dinámico.
- ❌ «Una función» → Frente a «¿Qué es una plantilla literal?» lo fácil es confundirse. **Verdad**: Backticks con ${} para interpolar variables/expresiones. `Hola ${nombre}` — la forma moderna de construir texto dinámico.
- ❌ «"HOLA"» → Frente a «Tras let s="hola"; s.toUpperCase(); ¿qué vale s?» lo fácil es confundirse. **Verdad**: "hola" — los strings son inmutables. toUpperCase devuelve un NUEVO string; s no cambia salvo que lo reasignes.
- ❌ «Error» → Frente a «Tras let s="hola"; s.toUpperCase(); ¿qué vale s?» lo fácil es confundirse. **Verdad**: "hola" — los strings son inmutables. toUpperCase devuelve un NUEVO string; s no cambia salvo que lo reasignes.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
