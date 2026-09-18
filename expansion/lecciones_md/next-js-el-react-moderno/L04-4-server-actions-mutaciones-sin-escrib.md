# 4. Server Actions: mutaciones sin escribir APIs

> 📚 Curso: **▲ Next.js — El React Moderno** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx

Las SERVER ACTIONS son funciones del servidor llamables desde la UI:
    // app/actions.ts
    "use server";
    import { revalidatePath } from "next/cache";
    import { z } from "zod";
    export async function crearTarea(formData) {
      const t = z.object({ texto: z.string().min(1) })
                 .parse({ texto: formData.get("texto") }); // ¡validar!
      await db.tarea.create({ data: t });
      revalidatePath("/tareas");          // refresca la caché
    }

    // app/tareas/page.tsx (Server Component)
    <form action={crearTarea}>
      <input name="texto" />
      <button>Nueva tarea</button>
    </form>

El form funciona INCLUSO SIN JAVASCRIPT (enhancement progresivo), y con
JS da UX instantánea. Hooks de apoyo en client: useActionState (estado/
errores), useFormStatus (pending del botón). Para APIs públicas o
webhooks: app/api/hola/route.ts con export async function POST().

Seguridad: cada action es un endpoint público → valida entradas y
permisos SIEMPRE dentro; nunca confíes en hidden inputs.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es una Server Action?
- A) Una función que corre en el servidor invocable desde la UI sin escribir un endpoint
- B) Un Service Worker
- C) Un middleware de Express
- D) Un hook de React
### 2. ¿Qué debes hacer SIEMPRE dentro de una Server Action?
- A) Validar entradas y comprobar permisos
- B) Confiar en los datos del formulario
- C) Guardar en localStorage
- D) Llamar a alert()

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Una función que corre en el servidor invocable desde la UI sin escribir un endpoint — Con 'use server' declaras funciones backend llamables: Next genera el canal seguro automáticamente.
**2.** ✅ Validar entradas y comprobar permisos — El cliente puede enviar cualquier cosa: la action es tu última línea de defensa (zod + auth).

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
