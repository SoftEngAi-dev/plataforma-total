# ⚡ Cheatsheet — 4. Asincronía en Node: no congeles el servidor

> Node.js — JavaScript en el Servidor · Lección 4 · 18/09/2026

## 💡 Idea central
EL EVENT LOOP: EL MOTOR DE NODE

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué prohibir readFileSync en un servidor (salvo arranque)?** → Bloquea el único hilo de Node: TODOS los usuarios esperan _(El event loop único detenido = servidor congelado para todos.)_
- **¿Cómo reconoce Express un middleware de errores?** → Tiene exactamente 4 parámetros (err, req, res, next) _(La firma de 4 argumentos es el contrato; se registra DESPUÉS de las rutas.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
