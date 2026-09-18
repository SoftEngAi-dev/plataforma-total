# ⚡ Cheatsheet — 6. Narrowing y utilidades: escribir lógica segura

> TypeScript — JavaScript con Superpoderes y Seguridad · Lección 6 · 18/09/2026

## 💡 Idea central
NARROWING: DESECHAR CASOS Y GANAR CERTEZA

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué es una discriminated union?** → Una unión donde cada variante tiene una clave literal común (kind) que permite narrowing _(El patrón de modelado de estados favorito en TS: cada rama decide la forma disponible.)_
- **¿Qué significa x is string en un type guard?** → Le dice a TS: si esta función devuelve true, trata x como string de ahí en adelante _(Los guards personalizados enseñan al compilador a razonar sobre tus datos.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
