# ⚠️ Errores comunes — 1. Utility-first: pensar en clases pequeñas

> 🎨 Tailwind CSS — Diseño a Velocidad · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Escribir todo el CSS a mano con !important» → Frente a «¿Qué es el enfoque utility-first de Tailwind?» lo fácil es confundirse. **Verdad**: Componer el diseño con muchas clases de un solo propósito en el HTML. Muchas utilidades pequeñas y predecibles que se combinan: el diseño vive junto al marcado.
- ❌ «Usar solo CSS-in-JS» → Frente a «¿Qué es el enfoque utility-first de Tailwind?» lo fácil es confundirse. **Verdad**: Componer el diseño con muchas clases de un solo propósito en el HTML. Muchas utilidades pequeñas y predecibles que se combinan: el diseño vive junto al marcado.
- ❌ «Porque se borra todo el CSS» → Frente a «¿Por qué el CSS final en producción con Tailwind es pequeño?» lo fácil es confundirse. **Verdad**: Porque solo se generan las clases que realmente usas. El compilador detecta las clases presentes en tus archivos y emite únicamente esas reglas.
- ❌ «Porque se usa el CDN» → Frente a «¿Por qué el CSS final en producción con Tailwind es pequeño?» lo fácil es confundirse. **Verdad**: Porque solo se generan las clases que realmente usas. El compilador detecta las clases presentes en tus archivos y emite únicamente esas reglas.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
