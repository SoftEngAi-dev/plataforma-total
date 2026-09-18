# 3. Rutas por archivo, dinámicas y layouts

> 📚 Curso: **🚀 Astro — La Web de Contenido Moderna** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

El sistema de rutas de Astro es el sistema de archivos de src/pages:
    src/pages/index.astro      →  /
    src/pages/sobre-mi.astro   →  /sobre-mi
    src/pages/blog/index.astro →  /blog
    src/pages/blog/[slug].astro → rutas dinámicas

Páginas dinámicas estáticas (SSG) con getStaticPaths:
    ---
    export function getStaticPaths() {
      return [
        { params: { slug: "primer-post" }, props: { autor: "Ana" } },
        { params: { slug: "segundo-post" } },
      ];
    }
    const { slug } = Astro.params;
    ---
    <h1>Post: {slug}</h1>

Los LAYOUTS comparten la envoltura (cabecera, pie, metas). En
src/layouts/Base.astro incluyes <slot /> y en cada página:
    <Base titulo="Inicio"><p>Contenido</p></Base>

Con SSR (output: "server" o prerender = false por página) las rutas se
generan en cada petición; si no, todo se pre-renderiza en build.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué combinación crea rutas estáticas tipo /blog/mi-post en Astro?
- A) src/pages/blog/[slug].astro + getStaticPaths
- B) next.config.js
- C) un archivo routes.json
- D) server.js con Express
### 2. ¿Para qué sirve un layout con <slot /> en Astro?
- A) Envolver páginas repitiendo cabecera y pie, metiendo el contenido dentro
- B) Optimizar imágenes
- C) Crear endpoints
- D) Minificar el HTML

---

## 🔑 Respuestas y explicaciones

**1.** ✅ src/pages/blog/[slug].astro + getStaticPaths — El [param].astro en src/pages + getStaticPaths enumera las rutas a generar en build.
**2.** ✅ Envolver páginas repitiendo cabecera y pie, metiendo el contenido dentro — El layout aporta la estructura común y cada página inyecta su contenido en el slot.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
