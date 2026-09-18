# ⚡ Cheatsheet — 6. Relaciones: FOREIGN KEY y primer diseño

> SQL y Bases de Datos — Datos que Persisten · Lección 6 · 18/09/2026

## 💡 Idea central
MODELO RELACIONAL: NORMALIZAR BIEN

## 🧠 Autoexamen (tápate la respuesta)
- **¿Dónde va la FK en una relación 1 a muchos (autor-libros)?** → En libros (el lado 'muchos') _(Cada libro apunta a su autor: FK en la tabla del lado N.)_
- **¿Cómo se modela muchos-a-muchos?** → Tabla intermedia con ambas FK y PK compuesta _(La tabla puente (inscripciones) convierte M:N en dos relaciones 1:N.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
