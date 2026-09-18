# 3. SvelteKit y proyecto: app completa con rutas

> 📚 Curso: **Svelte y SvelteKit — Menos Código, Mismo Poder** · Lección 3 de 3
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```svelte
SVELTEKIT: LA APP REAL (ROUTING + SSR + FORMULARIOS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  npm create svelte@latest miapp && cd miapp && npm install && npm run dev

ROUTING POR ARCHIVOS (como Next.js)
  src/routes/+page.svelte            → /
  src/routes/acerca/+page.svelte       → /acerca
  src/routes/tareas/[id]/+page.svelte  → /tareas/42  (parámetro dinámico)
  src/routes/tareas/[id]/+page.server.js → datos del servidor para esa ruta (¡SSR!)

LOAD FUNCTIONS: cargar datos ANTES de renderizar (con SEO feliz)
  // +page.server.js
  export async function load({ params }) {
      const post = await db.query("SELECT * FROM posts WHERE id = ?", params.id);
      if (!post) throw error(404);
      return { post };
  }
  // +page.svelte
  <script>export let data;</script>
  <h1>{data.post.titulo}</h1>

FORM ACTIONS: formularios que funcionan SIN JS (progresive enhancement)
  <form method="POST"><input name="titulo"><button>Crear</button></form>
  // +page.server.js
  export const actions = { default: async ({ request }) => {
      const datos = await request.formData();
      await crearTarea(datos.get("titulo"));    // corre en el servidor
  }};

PROYECTO: clona la app de notas: ruta / + form action para crear + load que liste desde SQLite + /nota/[id] para detalle. Deploy gratis con adapter de Vercel/Netlify/Node.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace una función load en +page.server.js?
- A) CSS
- B) Corre en el SERVIDOR antes de renderizar y pasa datos a la página (SSR + SEO + sin flicker)
- C) Es un test
- D) Sirve imágenes
### 2. ¿Qué es progressive enhancement con form actions?
- A) Ajax con JS
- B) El formulario funciona sin JavaScript (POST clásico del servidor, JS solo lo acelera cuando existe)
- C) No funciona sin JS
- D) Un alert

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Corre en el SERVIDOR antes de renderizar y pasa datos a la página (SSR + SEO + sin flicker) — Datos en el server, HTML listo al llegar: la app rápida y el SEO contento.
**2.** ✅ El formulario funciona sin JavaScript (POST clásico del servidor, JS solo lo acelera cuando existe) — Robustez por diseño: tu app no se rompe si falla/red no carga el bundle JS.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
