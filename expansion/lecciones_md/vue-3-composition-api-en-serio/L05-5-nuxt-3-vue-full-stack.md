# 5. Nuxt 3: Vue full-stack

> 📚 Curso: **💚 Vue 3 — Composition API en Serio** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

Nuxt convierte Vue en un framework full-stack de producción:

  pages/               → rutas automáticas (pages/index.vue → /)
  server/api/hola.ts   → endpoint Node: export default defineEventHandler(
                           () => ({ msg: "hola" }))  → /api/hola
  components/          → auto-import: no escribes ni un import
  composables/, utils/ → auto-import también

Datos universales (SSR + hidratación sin doble fetch):
    const { data, pending, error } =
      await useFetch("/api/tareas", { key: "tareas" });

Modos por proyecto o por ruta: SSR por defecto, SSG con nuxi generate,
SPA si quieres, e ISLAS de componentes (experimental). El servidor Nitro
despliega igual en Node, Vercel, Netlify, Cloudflare Workers o Deno.

Meta-framework moderno: app.vue como raíz, <NuxtPage /> como outlet,
useSeoMeta() para SEO, middleware de rutas (definePageMeta({ middleware:
"auth" })) para proteger páginas.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué carpeta de Nuxt genera las rutas automáticamente?
- A) routes/
- B) pages/
- C) views/
- D) public/
### 2. ¿Dónde defines endpoints de backend en Nuxt 3?
- A) en server/api/
- B) en la carpeta pages/
- C) en un Express aparte obligatorio
- D) en nuxt.config solo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ pages/ — Cada .vue dentro de pages/ se convierte en ruta sin configurar ningún router.
**2.** ✅ en server/api/ — server/api/*.ts son endpoints Node del mismo proyecto, con despliegue integrado vía Nitro.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
