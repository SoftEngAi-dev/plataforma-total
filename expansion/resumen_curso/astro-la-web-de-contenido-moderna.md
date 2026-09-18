# 📕 Resumen maestro — 🚀 Astro — La Web de Contenido Moderna

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Islas: HTML primero, cero JS por defecto
 Astro es el framework para sitios de contenido (blogs, docs, marketing, portafolios) que envía CERO JavaScript por defecto: cada página .astro compila a HTML estático puro. Result…

## 2. 2. Componentes Astro: props, slots y estilos con scope
 Los componentes .astro (en src/components) son piezas reutilizables que se renderizan SIEMPRE en build/servidor: no se hidratan, no envían JS.      ---  // src/components/Tarjeta.…

## 3. 3. Rutas por archivo, dinámicas y layouts
 El sistema de rutas de Astro es el sistema de archivos de src/pages:     src/pages/index.astro      →  /     src/pages/sobre-mi.astro   →  /sobre-mi     src/pages/blog/index.astro…

## 4. 4. Content Collections: Markdown con tipos
 La forma profesional de gestionar contenido en Astro: CONTENT COLLECTIONS.  1. Crea src/content/blog/mi-post.md con frontmatter:     ---     title: "Hola mundo"     fecha: 2026-01…

## 5. 5. Hidratación con client:* y despliegue
 Las directivas client controlan CUÁNDO se hidrata cada isla:     <Contador client:load />      → al cargar la página     <Contador client:visible />   → cuando entra en pantalla (…

---
✅ 5 lecciones · 📝 10 preguntas de repaso en quizzes_html/ · tests/