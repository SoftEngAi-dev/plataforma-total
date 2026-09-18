# 5. Hidratación con client:* y despliegue

> 📚 Curso: **🚀 Astro — La Web de Contenido Moderna** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

Las directivas client controlan CUÁNDO se hidrata cada isla:
    <Contador client:load />      → al cargar la página
    <Contador client:visible />   → cuando entra en pantalla (la más eficiente)
    <Contador client:idle />      → cuando el navegador está libre
    <Contador client:only="react" /> → sin pre-render en servidor

Solo viaja el JavaScript de tus islas: una página típica pasa de ~300 KB
de JS (SPA clásica) a ~5-20 KB. Puedes mezclar frameworks: una isla React
para el carrito, otra Svelte para el buscador, todo en la misma página.

DESPLIEGUE:
  · npm run build → carpeta dist/ estática: Netlify, Vercel, Cloudflare
    Pages, GitHub Pages, cualquier hosting estático.
  · SSR: añade un adapter (node, vercel, cloudflare) y output:"server" en
    astro.config.mjs para rutas dinámicas por petición.
  · Extra moderno: <ViewTransitions /> da navegación fluida tipo SPA.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué directiva hidrata una isla SOLO cuando el usuario la ve en pantalla?
- A) client:load
- B) client:visible
- C) client:only
- D) client:media
### 2. ¿Qué produce `astro build` por defecto?
- A) Un ejecutable .exe
- B) La carpeta dist/ estática lista para cualquier hosting
- C) Un contenedor Docker
- D) Una app móvil

---

## 🔑 Respuestas y explicaciones

**1.** ✅ client:visible — client:visible usa IntersectionObserver: cero coste hasta que la isla es visible.
**2.** ✅ La carpeta dist/ estática lista para cualquier hosting — Salida 100% estática: la subes a cualquier CDN/hosting estático y vuela.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
