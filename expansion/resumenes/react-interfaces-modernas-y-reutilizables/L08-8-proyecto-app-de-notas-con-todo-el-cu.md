# ⚡ Cheatsheet — 8. Proyecto: app de notas con todo el curso

> React — Interfaces Modernas y Reutilizables · Lección 8 · 18/09/2026

## 💡 Idea central
CONSTRUYE: NOTAS REACT COMPLETAS

## 🧠 Autoexamen (tápate la respuesta)
- **¿Cómo editar una nota inmutablemente en un array de estado?** → map que devuelve objeto nuevo {...n, texto: x} solo para el id coincidente _(map con spread: reemplazas el objeto con uno NUEVO; referencias nuevas → React entiende y la UI se actualiza.)_
- **¿Qué dos APIs persisten las notas en esta app?** → useState + useEffect dentro de un custom hook useLocalStorage _(Estado + efecto que escribe a localStorage: patrón simple, potente y reutilizable.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
