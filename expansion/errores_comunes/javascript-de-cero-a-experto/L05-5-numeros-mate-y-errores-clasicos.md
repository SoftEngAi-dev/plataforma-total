# ⚠️ Errores comunes — 5. Números, mate y errores clásicos

> JavaScript — De Cero a Experto · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Bug de JavaScript» → Frente a «¿Por qué 0.1 + 0.2 !== 0.3 en JS (y casi todo lenguaje)?» lo fácil es confundirse. **Verdad**: Representación binaria de punto flotante: 0.1 y 0.2 no son exactos en base 2. Como 1/3 en decimal, algunos decimales son infinitos en binario. Solución: enteros (centavos) o toFixed.
- ❌ «La consola miente» → Frente a «¿Por qué 0.1 + 0.2 !== 0.3 en JS (y casi todo lenguaje)?» lo fácil es confundirse. **Verdad**: Representación binaria de punto flotante: 0.1 y 0.2 no son exactos en base 2. Como 1/3 en decimal, algunos decimales son infinitos en binario. Solución: enteros (centavos) o toFixed.
- ❌ «Math.random(1,6)» → Frente a «¿Cómo generar un entero aleatorio entre 1 y 6?» lo fácil es confundirse. **Verdad**: Math.floor(Math.random() * 6) + 1. random()*6 ∈ [0,6); floor → 0-5; +1 → dado de 1 a 6.
- ❌ «random(6)» → Frente a «¿Cómo generar un entero aleatorio entre 1 y 6?» lo fácil es confundirse. **Verdad**: Math.floor(Math.random() * 6) + 1. random()*6 ∈ [0,6); floor → 0-5; +1 → dado de 1 a 6.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
