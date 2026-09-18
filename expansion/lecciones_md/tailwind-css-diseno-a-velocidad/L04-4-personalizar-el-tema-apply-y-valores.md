# 4. Personalizar el tema, @apply y valores arbitrarios

> 📚 Curso: **🎨 Tailwind CSS — Diseño a Velocidad** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```css

Tu marca, tu tema. En Tailwind v4 personalizas en el propio CSS:
    @import "tailwindcss";
    @theme {
      --color-marca: #7c3aed;
      --font-display: "Space Grotesk", sans-serif;
    }
    → ya existen las clases bg-marca, text-marca, font-display…

(En v3 se hacía en tailwind.config.js con theme.extend.)

Cuando repites MUCHO un combo, extráelo con @apply (con moderación):
    .btn { @apply px-4 py-2 rounded-lg font-semibold transition; }
    .btn-primario { @apply btn bg-indigo-600 text-white hover:bg-indigo-500; }

Valores arbitrarios puntuales con corchetes:
    w-[347px]  grid-cols-[1fr_280px]  text-[15px]  top-[-6px]

Plugins oficiales: @tailwindcss/typography (prose para Markdown),
forms. Regla de buen gusto: primero utilidades; si el HTML se vuelve
ilegible, crea un COMPONENTE (React/Vue/Astro) antes que 30 @apply.
```

---

## 📝 Quiz de la lección

### 1. En Tailwind v4, ¿dónde defines colores de marca personalizados?
- A) En el bloque @theme de tu archivo CSS
- B) En un XML
- C) En el HTML
- D) En package.json
### 2. ¿Para qué sirve @apply?
- A) Reutilizar un conjunto de utilidades dentro de una clase propia
- B) Importar fuentes
- C) Hacer responsive
- D) Generar el build

---

## 🔑 Respuestas y explicaciones

**1.** ✅ En el bloque @theme de tu archivo CSS — @theme genera tokens (p. ej. --color-marca) que se convierten en clases como bg-marca automáticamente.
**2.** ✅ Reutilizar un conjunto de utilidades dentro de una clase propia — @apply incrusta utilidades en .mi-clase (útil para patrones repetidos), aunque los componentes suelen abstraer mejor.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
