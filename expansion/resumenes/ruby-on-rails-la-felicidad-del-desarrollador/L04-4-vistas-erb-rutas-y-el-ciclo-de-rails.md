# ⚡ Cheatsheet — 4. Vistas ERB, rutas y el ciclo de Rails

> Ruby on Rails — La Felicidad del Desarrollador · Lección 4 · 18/09/2026

## 💡 Idea central
DE URL A PANTALLA (VISTAS + RUTAS)

## 🧠 Autoexamen (tápate la respuesta)
- **¿Diferencia entre <% %> y <%= %> en ERB?** → <% ejecuta sin imprimir (loops/ifs); <%= ejecuta E IMPRIME escapando HTML _(El clásico bug: poner <%= en un @each y ver la lista entera impresa.)_
- **¿Qué hace form_with model: @post?** → Formulario automático ligado al modelo: crea o edita según el objeto, con token CSRF incluido _(Los helpers sienten la convención: si @post es nuevo → POST /posts; si existe → PATCH.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
