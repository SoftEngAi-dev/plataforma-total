# ⚡ Cheatsheet — 5. useEffect: sincronizar con el mundo exterior

> React — Interfaces Modernas y Reutilizables · Lección 5 · 18/09/2026

## 💡 Idea central
EFECTOS: DESPUÉS DEL RENDER

## 🧠 Autoexamen (tápate la respuesta)
- **¿Cuándo se ejecuta useEffect(fn, [])?** → Una vez al montar el componente _(Array vacío = sin dependencias: solo el montaje. La limpieza corre al desmontar.)_
- **¿Para qué sirve la función de limpieza del efecto?** → Cancelar trabajo pendiente (fetch, timers, subscripciones) antes de re-ejecutar o desmontar _(Evita race conditions y fugas: la respuesta tardía de un fetch viejo no pisa la nueva.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
