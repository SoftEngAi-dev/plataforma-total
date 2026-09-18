# 2. SvelteKit: rutas +page y datos con load

> 📚 Curso: **🔥 SvelteKit & Svelte 5 — Apps Completas** · Lección 2 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```svelte

SvelteKit es el framework full-stack de Svelte. Rutas por archivos en
src/routes:
    src/routes/+page.svelte          → /
    src/routes/sobre/+page.svelte    → /sobre
    src/routes/blog/[slug]/+page.svelte → /blog/cualquiera
    +layout.svelte → envoltura compartida (con <slot /> o {@render children()})

DATOS con load (antes de renderizar):
    // src/routes/blog/[slug]/+page.js
    export async function load({ params, fetch }) {
      const res = await fetch(`/api/posts/${params.slug}`);
      return { post: await res.json() };
    }
    <!-- +page.svelte -->
    <script> let { data } = $props(); </script>
    <h1>{data.post.titulo}</h1>

load universal (+page.js) corre en servidor la 1ª vez y en el cliente al
navegar; +page.server.js SOLO en servidor (para secretos/DB). Streaming
con promises, forms con actions (siguiente lección) y endpoints API con
+server.js. SSR + hidratación + navegación cliente, todo de serie.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué archivo dentro de src/routes/blog crea la ruta /blog?
- A) +page.svelte
- B) index.html
- C) routes.js
- D) blog.svelte
### 2. ¿Cuándo se ejecuta la función load universal de +page.js?
- A) En la primera carga en el servidor y después en el cliente al navegar
- B) Solo en build
- C) Nunca en el servidor
- D) Solo en tests

---

## 🔑 Respuestas y explicaciones

**1.** ✅ +page.svelte — La convención de SvelteKit: +page.svelte marca la página; los directorios definen el path.
**2.** ✅ En la primera carga en el servidor y después en el cliente al navegar — Es universal: SSR primero, y hidratación cliente en las navegaciones siguientes (con fetch especial).

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
