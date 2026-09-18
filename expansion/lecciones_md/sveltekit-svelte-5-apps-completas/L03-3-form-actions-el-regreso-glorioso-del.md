# 3. Form actions: el regreso glorioso del <form>

> 📚 Curso: **🔥 SvelteKit & Svelte 5 — Apps Completas** · Lección 3 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```svelte

SvelteKit abraza la plataforma web: los formularios clásicos funcionan
SIN JavaScript y con JS se comportan como SPA (enhancement progresivo).

    <!-- +page.svelte -->
    <form method="POST" action="?/crear">
      <input name="texto" required />
      <button>Añadir</button>
    </form>

    // +page.server.js
    import { fail } from "@sveltejs/kit";
    export const actions = {
      crear: async ({ request }) => {
        const data = await request.formData();
        const texto = data.get("texto")?.toString().trim();
        if (!texto) return fail(422, { error: "Texto obligatorio" });
        await db.insertar({ texto });
        return { ok: true };
      },
    };

En la página, export let form (o $props()) recibe lo devuelto: errores de
validación sin estado manual. Con use:enhance obtienes comportamiento SPA
y mejor UX. acciones nombradas: ?/crear, ?/borrar por formulario.
Valida SIEMPRE en el servidor (zod/valibot encajan perfecto).
```

---

## 📝 Quiz de la lección

### 1. ¿Funciona un <form> de SvelteKit sin JavaScript?
- A) Sí: enhancement progresivo, funciona como formulario clásico
- B) No, siempre requiere JS
- C) Solo en Chrome
- D) Solo con use:enhance
### 2. ¿Cómo devuelves un error de validación al formulario desde una action?
- A) Con fail(422, { error })
- B) Con alert()
- C) Con console.log
- D) Con redirect(404)

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Sí: enhancement progresivo, funciona como formulario clásico — Ese es su punto fuerte: con JS es SPA; sin JS sigue funcionando vía POST estándar.
**2.** ✅ Con fail(422, { error }) — fail devuelve al navegador el estado y un objeto que la página lee en la prop form.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
