# ⚠️ Errores comunes — 4. Personalizar el tema, @apply y valores arbitrarios

> 🎨 Tailwind CSS — Diseño a Velocidad · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «En un XML» → Frente a «En Tailwind v4, ¿dónde defines colores de marca personalizados?» lo fácil es confundirse. **Verdad**: En el bloque @theme de tu archivo CSS. @theme genera tokens (p. ej. --color-marca) que se convierten en clases como bg-marca automáticamente.
- ❌ «En el HTML» → Frente a «En Tailwind v4, ¿dónde defines colores de marca personalizados?» lo fácil es confundirse. **Verdad**: En el bloque @theme de tu archivo CSS. @theme genera tokens (p. ej. --color-marca) que se convierten en clases como bg-marca automáticamente.
- ❌ «Importar fuentes» → Frente a «¿Para qué sirve @apply?» lo fácil es confundirse. **Verdad**: Reutilizar un conjunto de utilidades dentro de una clase propia. @apply incrusta utilidades en .mi-clase (útil para patrones repetidos), aunque los componentes suelen abstraer mejor.
- ❌ «Hacer responsive» → Frente a «¿Para qué sirve @apply?» lo fácil es confundirse. **Verdad**: Reutilizar un conjunto de utilidades dentro de una clase propia. @apply incrusta utilidades en .mi-clase (útil para patrones repetidos), aunque los componentes suelen abstraer mejor.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
