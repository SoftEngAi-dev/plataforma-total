# ⚡ Cheatsheet — 5. Express + estructura real + variables de entorno

> Node.js — JavaScript en el Servidor · Lección 5 · 18/09/2026

## 💡 Idea central
DE EJEMPLO A PROYECTO REAL

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué los secretos van en variables de entorno y no en el código?** → Para no publicarlos en git y poder variarlos por entorno (dev/prod) _(Código público + secretos = filtración. .env + .gitignore es la norma; nunca commitees el .env.)_
- **¿Qué aporta separar app.js de index.js (listen)?** → Puedes importar y TESTEAR la app sin abrir puerto; separa configuración de ejecución _(La app testeable se exporta sin listen; en tests corren peticiones contra ella con supertest.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
