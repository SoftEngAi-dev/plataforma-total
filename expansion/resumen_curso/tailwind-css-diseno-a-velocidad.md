# 📕 Resumen maestro — 🎨 Tailwind CSS — Diseño a Velocidad

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Utility-first: pensar en clases pequeñas
 Tailwind rompe con el CSS tradicional: en vez de inventar clases (.boton-primario con 8 propiedades), COMPONES con utilidades de un solo propósito directamente en el HTML:     <bu…

## 2. 2. Layout: flexbox, grid y responsive móvil primero
 Maquetar con Tailwind es aplicar flexbox/grid por utilidades:     <nav class="flex items-center justify-between gap-4 px-6 py-3">     <section class="grid grid-cols-3 gap-6">     …

## 3. 3. Estados y variantes: hover, dark: y group
 Los pseudo-estados CSS son prefijos:     <button class="bg-indigo-600 hover:bg-indigo-500 active:scale-95                    focus:ring-2 ring-indigo-300 transition">     <input c…

## 4. 4. Personalizar el tema, @apply y valores arbitrarios
 Tu marca, tu tema. En Tailwind v4 personalizas en el propio CSS:     @import "tailwindcss";     @theme {       --color-marca: #7c3aed;       --font-display: "Space Grotesk", sans-…

## 5. 5. Producción: shadcn/ui, accesibilidad y buenas prácticas
 En producción el JIT genera solo lo usado: no hay "purgado" manual que configurar; evita componer nombres de clase en strings dinámicos (`bg-${color}-500` NO se detectará → usa ob…

---
✅ 5 lecciones · 📝 10 preguntas de repaso en quizzes_html/ · tests/