# ⚠️ Errores comunes — 6. Narrowing y utilidades: escribir lógica segura

> TypeScript — JavaScript con Superpoderes y Seguridad · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «Unir objetos con &» → Frente a «¿Qué es una discriminated union?» lo fácil es confundirse. **Verdad**: Una unión donde cada variante tiene una clave literal común (kind) que permite narrowing. El patrón de modelado de estados favorito en TS: cada rama decide la forma disponible.
- ❌ «Una clase abstracta» → Frente a «¿Qué es una discriminated union?» lo fácil es confundirse. **Verdad**: Una unión donde cada variante tiene una clave literal común (kind) que permite narrowing. El patrón de modelado de estados favorito en TS: cada rama decide la forma disponible.
- ❌ «Una comparación» → Frente a «¿Qué significa x is string en un type guard?» lo fácil es confundirse. **Verdad**: Le dice a TS: si esta función devuelve true, trata x como string de ahí en adelante. Los guards personalizados enseñan al compilador a razonar sobre tus datos.
- ❌ «Convierte el tipo» → Frente a «¿Qué significa x is string en un type guard?» lo fácil es confundirse. **Verdad**: Le dice a TS: si esta función devuelve true, trata x como string de ahí en adelante. Los guards personalizados enseñan al compilador a razonar sobre tus datos.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
