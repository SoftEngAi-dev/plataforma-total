# ⚡ Cheatsheet — 3. Overfitting vs underfitting y validación

> Machine Learning — Primer Contacto Real · Lección 3 · 18/09/2026

## 💡 Idea central
EL DILEMA CENTRAL: MEMORIZAR VS APRENDER

## 🧠 Autoexamen (tápate la respuesta)
- **Train 99%, test 72%. ¿Diagnóstico?** → OVERFIT: memorizó el entrenamiento, no generaliza — modelo demasiado complejo para los datos _(La brecha train>>test es el síntoma canónico de sobreajuste.)_
- **¿Qué aporta cross_val_score(modelo, X, y, cv=5) sobre un solo split?** → Evalúa 5 veces con particiones rotadas: medida mucho más estable y robusta de tu desempeño real _(Un solo split puede tener suerte/mala suerte con qué datos tocaron: la CV promedia esa lotería.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
