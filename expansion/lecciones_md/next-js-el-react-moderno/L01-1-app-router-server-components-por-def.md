# 1. App Router: Server Components por defecto

> 📚 Curso: **▲ Next.js — El React Moderno** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx

Next.js 14/15 con APP ROUTER cambia las reglas: en la carpeta app/,
TODOS los componentes son REACT SERVER COMPONENTS salvo que digas lo
contrario. Eso significa:
  · Se ejecutan en el servidor; su JavaScript NO viaja al navegador.
  · Pueden ser async y leer bases de datos, ficheros o secretos directo.

    // app/panel/page.tsx   →  ruta /panel
    import db from "@/lib/db";
    export default async function Panel() {
      const pedidos = await db.query("SELECT * FROM pedidos");
      return <ul>{pedidos.map(p => <li key={p.id}>{p.total}</li>)}</ul>;
    }

Convenciones por carpeta:
  page.tsx     → la ruta en sí        layout.tsx → envoltura persistente
  loading.tsx  → fallback automático  error.tsx  → Error Boundary
  not-found.tsx→ 404 por segmento

Menos JS enviado, primera carga rapidísima, y acceso a datos sin APIs
intermedias. Proyecto: npx create-next-app@latest (App Router activo).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es un React Server Component en Next.js App Router?
- A) Un componente que se renderiza en el servidor y no envía su JS al cliente
- B) Un microservicio
- C) Un Web Worker
- D) Una librería de CSS
### 2. ¿Qué archivo crea la ruta /dashboard en el App Router?
- A) app/dashboard/page.tsx
- B) pages/dashboard.tsx
- C) app/routes/dashboard.ts
- D) src/dashboard.jsx

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Un componente que se renderiza en el servidor y no envía su JS al cliente — Corre en el servidor: puede usar async/await y recursos backend sin exponerlos al navegador.
**2.** ✅ app/dashboard/page.tsx — En app/, cada carpeta con page.tsx es una ruta; layouts y loading se anidan por segmento.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
