# ⚡ Cheatsheet — 7. Patrones reales: fetch con estados y manejo de errores

> React — Interfaces Modernas y Reutilizables · Lección 7 · 18/09/2026

## 💡 Idea central
 FETCH EN REACT NIVEL PRODUCCIÓN

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué 3 estados mínimos modelan cualquier fetch en UI?** → cargando, error, datos _(Con esos tres discriminas exáctamente qué pintar: spinner, mensaje de error o contenido.)_
- **¿Por qué la bandera 'cancelado' en el efecto de fetch?** → Evita que una respuesta tardía actualice estado de un componente desmontado (warning + race) _(En StrictMode y navegación rápida los componentes se montan/desmontan: la guardia lo hace robusto.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
