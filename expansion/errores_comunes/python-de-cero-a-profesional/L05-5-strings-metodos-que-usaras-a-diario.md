# ⚠️ Errores comunes — 5. Strings: métodos que usarás a diario

> Python — De Cero a Profesional · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «"a-b-c"» → Frente a «'a-b-c'.split('-') devuelve...» lo fácil es confundirse. **Verdad**: ['a', 'b', 'c']. split corta en lista; el inverso es '-'.join(lista).
- ❌ «('a','b','c')» → Frente a «'a-b-c'.split('-') devuelve...» lo fácil es confundirse. **Verdad**: ['a', 'b', 'c']. split corta en lista; el inverso es '-'.join(lista).
- ❌ «Porque strip falla sin ella» → Frente a «¿Por qué debes reasignar texto = texto.strip()?» lo fácil es confundirse. **Verdad**: Los strings son inmutables: strip devuelve uno nuevo. Métodos de str NUNCA modifican el original.
- ❌ «Por velocidad» → Frente a «¿Por qué debes reasignar texto = texto.strip()?» lo fácil es confundirse. **Verdad**: Los strings son inmutables: strip devuelve uno nuevo. Métodos de str NUNCA modifican el original.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
