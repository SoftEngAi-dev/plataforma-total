# ⚡ Cheatsheet — 5. Monitoreo y logs: saber cuando tu app llora

> DevOps y CI/CD — De Tu PC a Producción Sin Sudor · Lección 5 · 18/09/2026

## 💡 Idea central
OBSERVABILIDAD: DEL 'SÍ FUNCIONA' AL 'SÉ CÓMO VA'

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué niveles correctos de logs distinguen?** → DEBUG/INFO/WARNING/ERROR — filtras según la gravedad y el ambiente _(En prod corre INFO+; en dev activas DEBUG. El ruido bien dosificado vale oro.)_
- **¿Qué verifica un endpoint /health?** → Que la aplicación responde (200) — monitores externos lo sondean periódicamente _(Healthcheck es el '¿sigues viva?' de toda app desplegada: bases de alertas.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
