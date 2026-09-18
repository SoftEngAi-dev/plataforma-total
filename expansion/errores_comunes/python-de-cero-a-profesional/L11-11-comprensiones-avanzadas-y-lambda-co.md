# ⚠️ Errores comunes — 11. Comprensiones avanzadas y lambda: código que se lee

> Python — De Cero a Profesional · Lección 11 · Aprender de los errores (propios y ajenos)

- ❌ «Loops normales» → Frente a «all() y any() con generador hacen...» lo fácil es confundirse. **Verdad**: Lógica declarativa: ¿todos/alguno cumplen? — sin bucles explícitos. all(x > 0 for x in nums) se lee como español: todos mayores a cero.
- ❌ «Suma de listas» → Frente a «all() y any() con generador hacen...» lo fácil es confundirse. **Verdad**: Lógica declarativa: ¿todos/alguno cumplen? — sin bucles explícitos. all(x > 0 for x in nums) se lee como español: todos mayores a cero.
- ❌ «Siempre» → Frente a «¿Cuándo usar lambda?» lo fácil es confundirse. **Verdad**: Funciones de una expresión triviales pasadas a key= y similares; en todo otro caso, def. Si necesita nombre para entenderse, ese nombre es su def.
- ❌ «Nunca» → Frente a «¿Cuándo usar lambda?» lo fácil es confundirse. **Verdad**: Funciones de una expresión triviales pasadas a key= y similares; en todo otro caso, def. Si necesita nombre para entenderse, ese nombre es su def.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
