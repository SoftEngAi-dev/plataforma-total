# ⚡ Cheatsheet — 4. Despliegue continuo y entornos

> DevOps y CI/CD — De Tu PC a Producción Sin Sudor · Lección 4 · 18/09/2026

## 💡 Idea central
ENTORNOS: DEV → STAGING → PROD

## 🧠 Autoexamen (tápate la respuesta)
- **¿Para qué existe staging?** → Ambiente IDÉNTICO a producción donde validar antes del deploy real _(Los bugs 'solo-pasan-en-prod' se atrapan en staging.)_
- **¿Qué regala Docker al momento de rollback?** → La versión anterior sigue como imagen: vuelves a correr esa y listo, sin reinstalar _(Inmutabilidad de imágenes = tiempo de restauración en segundos.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
