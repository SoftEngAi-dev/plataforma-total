# ⚡ Cheatsheet — 4. Volúmenes, redes y docker-compose: demasiado para la vida real

> Docker — 'En Mi Máquina Sí Funciona' Resuelto · Lección 4 · 18/09/2026

## 💡 Idea central
MÁS ALLÁ DEL CONTENEDOR EFÍMERO

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué un contenedor no debe guardar datos importantes adentro?** → Es efímero/desmontable: los datos persistentes van en volúmenes _(Contenedor descartable + volumen persistente = patrón sano.)_
- **¿Qué ventaja tiene docker compose sobre docker run largos?** → Todo el stack (app+db+caché) versionado en un YAML: up/down con una orden _(El stack completo se define, comparte y levanta reproduciblemente — adiós README de 40 pasos.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
