# ⚡ Cheatsheet — 6. Composición, context y custom hooks: las 3 escaleras

> React — Interfaces Modernas y Reutilizables · Lección 6 · 18/09/2026

## 💡 Idea central
CRECER SIN COLAPSAR

## 🧠 Autoexamen (tápate la respuesta)
- **¿Cuándo llegar a Context?** → Cuando muchos componentes a mucha profundidad necesitan el mismo dato (tema, usuario, idioma) _(Context resuelve prop-drilling global; estado local y composición resuelven la mayoría de los casos.)_
- **¿Qué reglas tienen los hooks (useState, useEffect, customs)?** → Top-level del componente, sin loops/ifs, nombres use* _(El orden fijo de llamadas es cómo React empareja hook con celda de estado: romperlo = caos.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
