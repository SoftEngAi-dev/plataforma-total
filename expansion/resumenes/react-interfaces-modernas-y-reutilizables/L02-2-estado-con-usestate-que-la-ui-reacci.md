# ⚡ Cheatsheet — 2. Estado con useState: que la UI reaccione

> React — Interfaces Modernas y Reutilizables · Lección 2 · 18/09/2026

## 💡 Idea central
ESTADO: LA MEMORIA DEL COMPONENTE

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué setTareas([...tareas, nueva]) y no tareas.push(nueva)?** → React detecta cambios por REFERENCIA: hay que pasarle un array NUEVO o no re-renderiza _(Inmutabilidad: nueva referencia = señal de re-render. push muta en silencio.)_
- **¿Qué forma de actualización de estado es segura con valores previos?** → setCuenta(c => c + 1) _(La forma funcional garantiza trabajar sobre el estado más reciente (clicks encolados).)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
