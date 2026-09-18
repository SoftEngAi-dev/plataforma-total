# ⚠️ Errores comunes — 3. Estados y variantes: hover, dark: y group

> 🎨 Tailwind CSS — Diseño a Velocidad · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Con JavaScript obligatorio» → Frente a «¿Cómo haces que un hijo cambie cuando el padre recibe hover?» lo fácil es confundirse. **Verdad**: Con group en el padre y group-hover: en el hijo. group marca el contenedor; group-hover:aplica-estilo solo cuando el grupo está en hover.
- ❌ «Con media queries» → Frente a «¿Cómo haces que un hijo cambie cuando el padre recibe hover?» lo fácil es confundirse. **Verdad**: Con group en el padre y group-hover: en el hijo. group marca el contenedor; group-hover:aplica-estilo solo cuando el grupo está en hover.
- ❌ «Oculta el botón» → Frente a «¿Qué hace la clase transition en un botón?» lo fácil es confundirse. **Verdad**: Anima suavemente los cambios de propiedades (color, escala…) entre estados. transition + duration-* suaviza hover/active/focus sin escribir @keyframes.
- ❌ «Cambia el tipo de letra» → Frente a «¿Qué hace la clase transition en un botón?» lo fácil es confundirse. **Verdad**: Anima suavemente los cambios de propiedades (color, escala…) entre estados. transition + duration-* suaviza hover/active/focus sin escribir @keyframes.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
