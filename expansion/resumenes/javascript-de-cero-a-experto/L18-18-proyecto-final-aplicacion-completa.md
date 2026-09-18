# ⚡ Cheatsheet — 18. Proyecto final: aplicación completa de tareas (DOM + eventos + JSON)

> JavaScript — De Cero a Experto · Lección 18 · 18/09/2026

## 💡 Idea central
CONSTRUYE: GESTOR DE TAREAS COMPLETO

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué dos llamadas sincronizan la app con localStorage?** → parse y stringify de JSON _(stringify al guardar, parse al cargar: JSON es el puente.)_
- **¿Por qué delegación de eventos en la lista en vez de listener por li?** → Los li se recrean en cada render; un solo listener en el ul sigue funcionando siempre _(Contenido dinámico = listener en el padre estable, acción según e.target.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
