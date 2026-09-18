# ⚡ Cheatsheet — 8. Índices y transacciones: velocidad y seguridad

> SQL y Bases de Datos — Datos que Persisten · Lección 8 · 18/09/2026

## 💡 Idea central
ÍNDICES: DEL O(n) AL O(log n)

## 🧠 Autoexamen (tápate la respuesta)
- **¿Cuándo crear un índice?** → En columnas usadas frecuentemente en WHERE/JOIN (con costo de escritura) _(Índices aceleran lecturas pero encarecen escrituras: sobredimensionarlos es deuda.)_
- **¿Qué garantiza una transacción bancaria (BEGIN...COMMIT)?** → Las dos actualizaciones suceden juntas o ninguna (atomicidad) _(Si falla a mitad, ROLLBACK: nunca hay dinero perdido en el aire.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
