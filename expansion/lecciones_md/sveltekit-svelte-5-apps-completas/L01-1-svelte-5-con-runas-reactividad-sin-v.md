# 1. Svelte 5 con runas: reactividad sin Virtual DOM

> 📚 Curso: **🔥 SvelteKit & Svelte 5 — Apps Completas** · Lección 1 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```svelte

Svelte COMPILA sus componentes a JavaScript quirúrgico: no hay Virtual
DOM en runtime, por eso es tan rápido y liviano. En Svelte 5 la
reactividad se declara con RUNAS:
    <script>
      let n = $state(0);                 // estado reactivo
      let usuario = $state({ nombre: "Ana" });
      const doble = $derived(n * 2);     // valor derivado
      $effect(() => console.log("n vale", n));  // efectos
      let { titulo = "Sin título" } = $props(); // props
    </script>
    <button onclick={() => n++}>Clicks: {n} (doble: {doble})</button>

    <style> button { color: teal; } </style>

Bloques de plantilla potentes: {#if cond}…{/if}, {#each lista as item
(item.id)}…{/each}, {#await promesa}…{/await}. El CSS es scoped por
defecto. Arrancar: npx sv create. Menos magia, menos código, más render
directo: una de las experiencias de desarrollo mejor valoradas.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo se declara estado reactivo en Svelte 5?
- A) Con la runa $state()
- B) Con setState()
- C) Con data()
- D) Con new Reactive()
### 2. ¿Qué NO utiliza Svelte en tiempo de ejecución?
- A) El Virtual DOM
- B) JavaScript
- C) CSS
- D) HTML

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Con la runa $state() — $state(0) crea una variable reactiva; $derived deriva valores y $effect ejecuta efectos.
**2.** ✅ El Virtual DOM — Svelte compila a actualizaciones quirúrgicas del DOM real: sin VDOM, menos memoria y más velocidad.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
