# 📕 Resumen maestro — 🔥 SvelteKit & Svelte 5 — Apps Completas

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Svelte 5 con runas: reactividad sin Virtual DOM
 Svelte COMPILA sus componentes a JavaScript quirúrgico: no hay Virtual DOM en runtime, por eso es tan rápido y liviano. En Svelte 5 la reactividad se declara con RUNAS:     <scrip…

## 2. 2. SvelteKit: rutas +page y datos con load
 SvelteKit es el framework full-stack de Svelte. Rutas por archivos en src/routes:     src/routes/+page.svelte          → /     src/routes/sobre/+page.svelte    → /sobre     src/ro…

## 3. 3. Form actions: el regreso glorioso del <form>
 SvelteKit abraza la plataforma web: los formularios clásicos funcionan SIN JavaScript y con JS se comportan como SPA (enhancement progresivo).      <!-- +page.svelte -->     <form…

## 4. 4. Endpoints +server.js, adapters y despliegue
 APIs con endpoints de archivo:     // src/routes/api/tareas/+server.js     import { json } from "@sveltejs/kit";     export async function GET() {       return json([{ id: 1, text…

---
✅ 4 lecciones · 📝 8 preguntas de repaso en quizzes_html/ · tests/