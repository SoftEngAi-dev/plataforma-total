# 4. Endpoints +server.js, adapters y despliegue

> 📚 Curso: **🔥 SvelteKit & Svelte 5 — Apps Completas** · Lección 4 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```svelte

APIs con endpoints de archivo:
    // src/routes/api/tareas/+server.js
    import { json } from "@sveltejs/kit";
    export async function GET() {
      return json([{ id: 1, texto: "Aprender SvelteKit" }]);
    }
    export async function POST({ request }) {
      const body = await request.json();
      // guardar…
      return json(body, { status: 201 });
    }

ADAPTERS: el mismo proyecto compila para donde despliegues:
  · adapter-auto    → detecta Vercel/Netlify/Cloudflare
  · adapter-node    → tu VPS o contenedor Docker
  · adapter-static  → SSG puro (sitios sin servidor)
Pre-render por página: export const prerender = true.

Variables de entorno seguras: $env/static/private jamás llega al cliente;
$env/dynamic/public para valores públicos.

Svelte 5 + SvelteKit destaca en Core Web Vitals: menos JS enviado,
rendimiento de compilador. Ideal para apps completas modernas con
presupuesto de bytes ajustado.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo creas un endpoint JSON en SvelteKit?
- A) Con un archivo +server.js que exporta funciones GET/POST
- B) Con una carpeta /api de Next
- C) Con localStorage
- D) Con ngrok
### 2. ¿Qué adapter eliges para desplegar SvelteKit en tu propio contenedor Docker?
- A) adapter-node
- B) adapter-static
- C) adapter-auto
- D) ninguno

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Con un archivo +server.js que exporta funciones GET/POST — +server.js en una ruta define handlers HTTP que devuelven json() personalizados.
**2.** ✅ adapter-node — adapter-node genera un servidor Node independiente, perfecto para VPS o Docker.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
