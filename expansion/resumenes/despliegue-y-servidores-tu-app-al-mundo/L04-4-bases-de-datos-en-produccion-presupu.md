# ⚡ Cheatsheet — 4. Bases de datos en producción: presupuesto mínimo de seriedad

> Despliegue y Servidores — Tu App al Mundo · Lección 4 · 18/09/2026

## 💡 Idea central
DATOS EN PROD: ALGUNOS PRECEPTOS DUROS

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué la base de datos NUNCA se expone directamente a internet?** → Ataques automáticos la encontrarían en horas; debe escuchar solo localhost/red interna _(Postgres/MySQL abiertos al mundo topan scanners a los minutos: firewall + bind local o red privada.)_
- **¿Qué es un backup 'probado'?** → Que REALMENTE restauraste alguna vez y verificaste que funciona _(Sin undrill de restauración periodic, el backup puede estar corrupto sin que lo sepas.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
