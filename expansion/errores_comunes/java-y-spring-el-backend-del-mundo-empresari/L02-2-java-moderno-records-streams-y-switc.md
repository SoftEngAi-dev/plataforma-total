# ⚠️ Errores comunes — 2. Java moderno: records, streams y switch nuevo

> Java y Spring — El Backend del Mundo Empresarial · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué resuelve Optional<T>?» lo fácil es confundirse. **Verdad**: Representa explícitamente la posible ausencia de valor: obliga a decidir (orElse, ifPresent) en vez de explotar con null. Hacer visible el 'puede faltar' en el TIPO es el antídoto contra NullPointerException.
- ❌ «Async» → Frente a «¿Qué resuelve Optional<T>?» lo fácil es confundirse. **Verdad**: Representa explícitamente la posible ausencia de valor: obliga a decidir (orElse, ifPresent) en vez de explotar con null. Hacer visible el 'puede faltar' en el TIPO es el antídoto contra NullPointerException.
- ❌ «bucles for» → Frente a «streams en Java se parecen a...» lo fácil es confundirse. **Verdad**: map/filter/reduce encadenados estilo funcional como en JS/Python. Operaciones declarativas sobre colecciones — Java moderno abraza lo funcional.
- ❌ «clases» → Frente a «streams en Java se parecen a...» lo fácil es confundirse. **Verdad**: map/filter/reduce encadenados estilo funcional como en JS/Python. Operaciones declarativas sobre colecciones — Java moderno abraza lo funcional.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
