# ⚠️ Errores comunes — 2. Optionals: adiós al error del billón de dólares

> Swift — El Camino de Apple · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Repite» → Frente a «¿Qué hace guard let x = y else { return }?» lo fácil es confundirse. **Verdad**: Si y es nil, sale de la función ya; si no, x queda disponible desempaquetada para el resto. Guard clause: los casos raros se despachan arriba y el código queda plano y claro.
- ❌ «Un bucle» → Frente a «¿Qué hace guard let x = y else { return }?» lo fácil es confundirse. **Verdad**: Si y es nil, sale de la función ya; si no, x queda disponible desempaquetada para el resto. Guard clause: los casos raros se despachan arriba y el código queda plano y claro.
- ❌ «Es lento» → Frente a «¿Por qué se considera peligroso el force unwrap (!) ?» lo fácil es confundirse. **Verdad**: Si el valor es nil, la app CRASHEA en runtime: evitas el mecanismo que te protege. El '!' es jurarle al compilador 'está ahí': cuando mientes, paga la app.
- ❌ «No compila» → Frente a «¿Por qué se considera peligroso el force unwrap (!) ?» lo fácil es confundirse. **Verdad**: Si el valor es nil, la app CRASHEA en runtime: evitas el mecanismo que te protege. El '!' es jurarle al compilador 'está ahí': cuando mientes, paga la app.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
