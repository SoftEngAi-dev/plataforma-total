# 4. Content Collections: Markdown con tipos

> 📚 Curso: **🚀 Astro — La Web de Contenido Moderna** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

La forma profesional de gestionar contenido en Astro: CONTENT COLLECTIONS.

1. Crea src/content/blog/mi-post.md con frontmatter:
    ---
    title: "Hola mundo"
    fecha: 2026-01-10
    tags: ["astro"]
    ---
    Contenido en **Markdown**…

2. Define el esquema en src/content.config.ts:
    import { defineCollection, z } from "astro:content";
    const blog = defineCollection({
      schema: z.object({ title: z.string(), fecha: z.date(),
                         tags: z.array(z.string()).optional() }),
    });
    export const collections = { blog };

3. Consulta tipada:
    import { getCollection } from "astro:content";
    const posts = await getCollection("blog");
    posts.sort((a, b) => b.data.fecha - a.data.fecha);

Ventajas: el frontmatter se valida en BUILD (si falta title, falla la
compilación), autocompletado total de entry.data, y con MDX puedes usar
componentes dentro del Markdown. Ideal para blogs y documentación.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué valida el esquema zod de una Content Collection?
- A) El frontmatter de cada Markdown durante el build
- B) El CSS
- C) Las llamadas HTTP
- D) Nada, es decorativo
### 2. ¿Cómo obtienes todas las entradas de la colección blog?
- A) getCollection('blog')
- B) leyendo el directorio con fs
- C) fetch('/api/blog')
- D) una consulta SQL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ El frontmatter de cada Markdown durante el build — Si un post incumple el esquema, el build falla: contenido corrupto nunca llega a producción.
**2.** ✅ getCollection('blog') — getCollection devuelve las entradas tipadas; con entry.render() obtienes el HTML.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
