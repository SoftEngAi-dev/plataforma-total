# ⚠️ Errores comunes — 3. CSS: selectores, cascada y el modelo de caja

> HTML y CSS — Diseño Web Total · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «etiqueta (p)» → Frente a «¿Qué selector tiene más especificidad?» lo fácil es confundirse. **Verdad**: id (#principal). id gana sobre clase y etiqueta. Inline style gana sobre todos.
- ❌ «clase (.nota)» → Frente a «¿Qué selector tiene más especificidad?» lo fácil es confundirse. **Verdad**: id (#principal). id gana sobre clase y etiqueta. Inline style gana sobre todos.
- ❌ «Elimina los bordes» → Frente a «¿Qué hace box-sizing: border-box?» lo fácil es confundirse. **Verdad**: width/height incluyen padding y border (lo intuitivo). Sin él, width:100px + padding te da una caja de más de 100px; con él, es exacto.
- ❌ «Añade sombras» → Frente a «¿Qué hace box-sizing: border-box?» lo fácil es confundirse. **Verdad**: width/height incluyen padding y border (lo intuitivo). Sin él, width:100px + padding te da una caja de más de 100px; con él, es exacto.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
