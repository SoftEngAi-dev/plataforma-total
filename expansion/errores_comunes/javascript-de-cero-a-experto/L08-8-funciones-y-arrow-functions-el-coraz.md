# ⚠️ Errores comunes — 8. Funciones y arrow functions: el corazón de JS

> JavaScript — De Cero a Experto · Lección 8 · Aprender de los errores (propios y ajenos)

- ❌ «null» → Frente a «¿Qué devuelve una función sin return?» lo fácil es confundirse. **Verdad**: undefined. Sin return explícito, toda función JS devuelve undefined.
- ❌ «0» → Frente a «¿Qué devuelve una función sin return?» lo fácil es confundirse. **Verdad**: undefined. Sin return explícito, toda función JS devuelve undefined.
- ❌ «Es más lenta» → Frente a «¿Qué diferencia clave tiene una arrow function?» lo fácil es confundirse. **Verdad**: No tiene su propio this: usa el del contexto que la rodea. Crucial en callbacks y objetos: la arrow no 'secuestra' el this como hace function.
- ❌ «No acepta parámetros» → Frente a «¿Qué diferencia clave tiene una arrow function?» lo fácil es confundirse. **Verdad**: No tiene su propio this: usa el del contexto que la rodea. Crucial en callbacks y objetos: la arrow no 'secuestra' el this como hace function.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
