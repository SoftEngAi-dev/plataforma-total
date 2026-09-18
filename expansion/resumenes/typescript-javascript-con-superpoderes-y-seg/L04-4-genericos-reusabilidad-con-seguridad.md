# ⚡ Cheatsheet — 4. Genéricos: reusabilidad con seguridad

> TypeScript — JavaScript con Superpoderes y Seguridad · Lección 4 · 18/09/2026

## 💡 Idea central
GENÉRICOS: <T> = TIPO PARÁMETRO

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué gana identidad<T>(v: T): T respecto a misto?: any?** → Recuerda el tipo exacto de entrada y lo devuelve: autocomplete y chequeo completos _(Los genéricos modelan RELACIONES entre tipos — any solo las borra.)_
- **¿Qué hace <T extends { length: number }>?** → Restringe T a tipos que tengan la propiedad length _(Constraint: puedo usar .length sabiendo que el compilador lo garantiza.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
