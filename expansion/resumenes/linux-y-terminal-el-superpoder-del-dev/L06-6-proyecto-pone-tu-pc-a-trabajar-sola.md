# ⚡ Cheatsheet — 6. Proyecto: pone tu PC a trabajar sola

> Linux y Terminal — El Superpoder del Dev · Lección 6 · 18/09/2026

## 💡 Idea central
AUTOMATIZA: 3 SCRIPTS DE TU VIDA DIARIA

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué ventaja tiene $fecha=$(date +%F) en el nombre del backup?** → Cada respaldo es distinto: nunca sobreescribes el de ayer _(Backups fechados = historia de restauración; sin fecha solo tienes una copia.)_
- **crontab -e + '0 21 * * * ./respaldo.sh' hace...** → Corre el respaldo automáticamente todos los días a las 21:00 _(cron = programador de tareas de Unix: tu computador trabaja mientras duermes.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
