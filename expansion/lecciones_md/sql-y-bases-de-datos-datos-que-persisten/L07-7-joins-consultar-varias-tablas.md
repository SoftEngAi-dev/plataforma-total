# 7. JOINs: consultar varias tablas

> 📚 Curso: **SQL y Bases de Datos — Datos que Persisten** · Lección 7 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```sql
JOINS: PEGAR TABLAS POR SUS CLAVES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INNER JOIN (intersección): solo lo que coincide en ambas
  SELECT l.titulo, a.nombre
  FROM libros l
  JOIN autores a ON l.autor_id = a.id;

LEFT JOIN (todo el lado izquierdo, aunque falte el derecho: NULLs)
  SELECT a.nombre, COUNT(l.id) AS libros
  FROM autores a
  LEFT JOIN libros l ON l.autor_id = a.id
  GROUP BY a.nombre;
  → autores sin libros aparecen con 0 (INNER los habría escondido)

VISUALIZACIÓN RÁPIDA
• INNER: intersección (solo los emparejados)
• LEFT: todo A + lo emparejable de B (resto NULLs)
• RIGHT: al revés · FULL: todos de ambos (pocos motores)

ALIAS CORTOS (l/a): estándar profesional para legibilidad cuando hay varias tablas.

PRÁCTICA: ejecuta ambos INNERS y LEFT sobre datos de juguete y mira la diferencia. Ahí vive el 80% del entendimiento de JOINs.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué registros incluye LEFT JOIN que INNER no?
- A) Todos los de la derecha
- B) Los de la tabla izquierda sin coincidencia (con NULLs en la derecha)
- C) Duplicados
- D) Ninguno
### 2. SELECT COUNT(l.id) con LEFT JOIN + GROUP BY autor da 0 cuando...
- A) Error
- B) El autor no tiene libros (las NULL no se cuentan en COUNT)
- C) El join falló
- D) La tabla está vacía

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Los de la tabla izquierda sin coincidencia (con NULLs en la derecha) — LEFT preserva el lado izquierdo completo: ideal para 'X con o sin Y'.
**2.** ✅ El autor no tiene libros (las NULL no se cuentan en COUNT) — COUNT(columna) no cuenta NULLs: encaja perfecto con LEFT JOIN para conteos con cero.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
