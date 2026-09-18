# ⚠️ Errores comunes — 2. Layout: flexbox, grid y responsive móvil primero

> 🎨 Tailwind CSS — Diseño a Velocidad · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «3 columnas solo en móvil» → Frente a «¿Qué significa la clase md:grid-cols-3?» lo fácil es confundirse. **Verdad**: 3 columnas a partir del breakpoint md (768px) hacia arriba. Tailwind es mobile-first: el base es móvil y los prefijos md:/lg: aplican hacia arriba.
- ❌ «3 filas» → Frente a «¿Qué significa la clase md:grid-cols-3?» lo fácil es confundirse. **Verdad**: 3 columnas a partir del breakpoint md (768px) hacia arriba. Tailwind es mobile-first: el base es móvil y los prefijos md:/lg: aplican hacia arriba.
- ❌ «con text-center» → Frente a «¿Cómo centras horizontalmente un contenedor con ancho máximo?» lo fácil es confundirse. **Verdad**: con la clase mx-auto (más max-w-* o container). mx-auto reparte el margen lateral; text-center solo alinea texto en línea.
- ❌ «con float:center» → Frente a «¿Cómo centras horizontalmente un contenedor con ancho máximo?» lo fácil es confundirse. **Verdad**: con la clase mx-auto (más max-w-* o container). mx-auto reparte el margen lateral; text-center solo alinea texto en línea.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
