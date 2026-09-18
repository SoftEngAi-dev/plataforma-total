# ⚡ Cheatsheet — 7. JOINs: consultar varias tablas

> SQL y Bases de Datos — Datos que Persisten · Lección 7 · 18/09/2026

## 💡 Idea central
JOINS: PEGAR TABLAS POR SUS CLAVES

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué registros incluye LEFT JOIN que INNER no?** → Los de la tabla izquierda sin coincidencia (con NULLs en la derecha) _(LEFT preserva el lado izquierdo completo: ideal para 'X con o sin Y'.)_
- **SELECT COUNT(l.id) con LEFT JOIN + GROUP BY autor da 0 cuando...** → El autor no tiene libros (las NULL no se cuentan en COUNT) _(COUNT(columna) no cuenta NULLs: encaja perfecto con LEFT JOIN para conteos con cero.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
