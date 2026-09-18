# ⚡ Cheatsheet — 3. PDO: bases de datos sin inyección

> PHP y Laravel — El Backend Que Alimenta la Web · Lección 3 · 18/09/2026

## 💡 Idea central
PDO: SQL SEGURO EN PHP

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué protegen los prepared statements?** → SQL injection: los datos van apartados del SQL y nunca se interpretan como código _(prepare() separa instrucción de datos: ' OR 1=1 -- queda como simple texto.)_
- **¿Qué PDO::FETCH_ASSOC devuelve?** → Cada fila como array asociativo ['columna'=>valor] _(Acceso por nombre de columna: código legible y resiliente.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
