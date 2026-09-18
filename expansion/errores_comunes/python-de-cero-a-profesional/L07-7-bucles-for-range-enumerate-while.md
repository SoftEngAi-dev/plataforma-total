# ⚠️ Errores comunes — 7. Bucles: for, range, enumerate, while

> Python — De Cero a Profesional · Lección 7 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué aporta enumerate frente a range(len(lista))?» lo fácil es confundirse. **Verdad**: Índice y elemento a la vez, legible y sin errores de off-by-one. enumerate es el idioma correcto; range(len()) es el acento extranjero.
- ❌ «Más velocidad» → Frente a «¿Qué aporta enumerate frente a range(len(lista))?» lo fácil es confundirse. **Verdad**: Índice y elemento a la vez, legible y sin errores de off-by-one. enumerate es el idioma correcto; range(len()) es el acento extranjero.
- ❌ «2..9» → Frente a «range(2, 10, 2) genera...» lo fácil es confundirse. **Verdad**: 2, 4, 6, 8. range(inicio, fin, paso) — fin SIEMPRE excluido.
- ❌ «2, 4, 6, 8, 10» → Frente a «range(2, 10, 2) genera...» lo fácil es confundirse. **Verdad**: 2, 4, 6, 8. range(inicio, fin, paso) — fin SIEMPRE excluido.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
