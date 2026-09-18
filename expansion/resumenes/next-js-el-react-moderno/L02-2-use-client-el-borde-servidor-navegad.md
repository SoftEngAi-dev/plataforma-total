# ⚡ Cheatsheet — 2. 'use client': el borde servidor/navegador

> ▲ Next.js — El React Moderno · Lección 2 · 18/09/2026

## 💡 Idea central


## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué obliga escribir 'use client' al inicio de un componente?** → Usar useState, useEffect o manejadores como onClick _(Esas APIs son del navegador; sin la directiva el componente se trata como Server Component y falla.)_
- **¿Dónde conviene ubicar la directiva 'use client' para optimizar el bundle?** → En los componentes hoja interactivos, lo más abajo posible _(Cuanto más abajo, menos JS viaja: el resto del árbol permanece como Server Components.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
