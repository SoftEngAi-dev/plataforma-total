# ⚡ Cheatsheet — 2. Optionals: adiós al error del billón de dólares

> Swift — El Camino de Apple · Lección 2 · 18/09/2026

## 💡 Idea central
OPTIONALS: NULL-SAFETY EN EL ADN

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué hace guard let x = y else { return }?** → Si y es nil, sale de la función ya; si no, x queda disponible desempaquetada para el resto _(Guard clause: los casos raros se despachan arriba y el código queda plano y claro.)_
- **¿Por qué se considera peligroso el force unwrap (!) ?** → Si el valor es nil, la app CRASHEA en runtime: evitas el mecanismo que te protege _(El '!' es jurarle al compilador 'está ahí': cuando mientes, paga la app.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
