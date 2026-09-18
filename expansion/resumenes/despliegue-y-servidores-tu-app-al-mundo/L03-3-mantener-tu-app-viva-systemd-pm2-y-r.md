# ⚡ Cheatsheet — 3. Mantener tu app viva: systemd, pm2 y reinicios

> Despliegue y Servidores — Tu App al Mundo · Lección 3 · 18/09/2026

## 💡 Idea central
PROCESOS QUE NO MUEREN (TRANQUILAMENTE)

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué hace Restart=always en systemd?** → Si el proceso muere, systemd lo vuelve a levantar automáticamente _(Con enable (boot) + Restart, tu app sobrevive cuelgues Y reboots sin tocarte el dedo.)_
- **¿Por qué un proceso 'detached' no basta para producción?** → Un pipeline nohup se pierde en reboots y caídas no planificadas; systemd/pm2 vigilan y resucitan _(La supervisor de procesos es la diferencia entre hobby y servicio confiable.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
