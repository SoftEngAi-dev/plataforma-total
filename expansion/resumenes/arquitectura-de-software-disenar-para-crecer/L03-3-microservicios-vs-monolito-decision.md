# ⚡ Cheatsheet — 3. Microservicios vs monolito: decisión de adultos

> Arquitectura de Software — Diseñar para Crecer · Lección 3 · 18/09/2026

## 💡 Idea central
DÓNDE VIVEN LAS APPS SERIAS

## 🧠 Autoexamen (tápate la respuesta)
- **¿Cuál es la mayor ventaja real del monolito modular para una startup?** → Velocidad: un despliegue, llamadas internas sin red, debug y refactors baratos mientras el equipo es pequeño _(El tiempo al mercado es el recurso: el monlito bien diseñado desperdicia menos meses iniciales.)_
- **¿Cuál costo fijo traen los microservicios que no existe en un monolito?** → Distribución: red entre servicios, transacciones complejas, logs distribuidos, deployment/orquestación _(Cada petición que antes era una llamada local pasa a ser una operación de red que puede fallar.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
