# ⚠️ Errores comunes — 2. Widgets: TODO es un widget

> Flutter — Apps Hermosas con Una Sola Base · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Un error» → Frente a «¿Qué es un StatelessWidget?» lo fácil es confundirse. **Verdad**: Un widget sin estado propio: se dibuja igual salvo que su PADRE le pase datos nuevos. La mayoría de la UI: describe, no cambia. Lo con estado es StatefulWidget.
- ❌ «Un widget con tabs» → Frente a «¿Qué es un StatelessWidget?» lo fácil es confundirse. **Verdad**: Un widget sin estado propio: se dibuja igual salvo que su PADRE le pase datos nuevos. La mayoría de la UI: describe, no cambia. Lo con estado es StatefulWidget.
- ❌ «Tabla» → Frente a «¿Qué hace Column(children: [...])?» lo fácil es confundirse. **Verdad**: Apila widgets verticalmente (Row es horizontal). Layouts de una dimensión; con Expanded/flex dentro controlas el reparto.
- ❌ «CSV» → Frente a «¿Qué hace Column(children: [...])?» lo fácil es confundirse. **Verdad**: Apila widgets verticalmente (Row es horizontal). Layouts de una dimensión; con Expanded/flex dentro controlas el reparto.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
