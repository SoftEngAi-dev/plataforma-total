# ⚡ Cheatsheet — 9. SQL con Python: sqlite3 práctico

> SQL y Bases de Datos — Datos que Persisten · Lección 9 · 18/09/2026

## 💡 Idea central
PYTHON + SQLITE: DATOS REALES DESDE TU CÓDIGO

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué usar ? (parámetros) y nunca f-strings en SQL?** → Los parámetros previenen SQL injection: los datos jamás se interpretan como código _(Con f-strings, un usuario malicioso escribe SQL dentro de tu consulta: el primer ataque web de la historia.)_
- **¿Qué aporta con.row_factory = sqlite3.Row?** → Acceder a las columnas POR NOMBRE (fila['nombre']) en vez de índices _(Código legible y resistente a cambios de orden de columnas.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
