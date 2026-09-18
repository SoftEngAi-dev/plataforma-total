# 1. Islas: HTML primero, cero JS por defecto

> 📚 Curso: **🚀 Astro — La Web de Contenido Moderna** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

Astro es el framework para sitios de contenido (blogs, docs, marketing,
portafolios) que envía CERO JavaScript por defecto: cada página .astro
compila a HTML estático puro. Resultado: carga instantánea, SEO perfecto.

¿Interactividad? Creas ISLAS: componentes (React, Vue, Svelte…) que se
hidratan de forma aislada sin lastrar el resto de la página. Es una MPA
(Multi-Page App) con navegación opcional tipo SPA via View Transitions.

Tu primer fichero src/pages/index.astro:
    ---
    // FRONTMATTER: corre en el SERVIDOR o en build. NUNCA llega al cliente.
    const titulo = "Hola Astro";
    const res = await fetch("https://api.example.com/datos");
    const datos = await res.json();
    ---
    <html>
      <body>
        <h1>{titulo}</h1>
        <p>{datos.mensaje}</p>
      </body>
    </html>

El frontmatter entre --- es TypeScript/JavaScript con acceso total al
backend (ficheros, bases de datos, secretos); abajo escribes HTML con
expresiones {…}. Proyecto nuevo: npm create astro@latest.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué envía Astro al navegador por defecto?
- A) Un enorme bundle de JavaScript
- B) Solo HTML + CSS estático (cero JS)
- C) WebAssembly
- D) Un Service Worker obligatorio
### 2. ¿Qué son las <islas> de Astro?
- A) Componentes interactivos que se hidratan de forma aislada
- B) Archivos del servidor
- C) Rutas dinámicas
- D) Plugins de Vite

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Solo HTML + CSS estático (cero JS) — Esa es su superpotencia: HTML estático sin JS salvo que añadas islas interactivas.
**2.** ✅ Componentes interactivos que se hidratan de forma aislada — Una isla (con client:load/visible…) se hidrata sola: el resto de la página sigue siendo HTML estático.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
