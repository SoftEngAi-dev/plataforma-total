# 3. Ordenar, limitar y funciones agregadas

> 📚 Curso: **SQL y Bases de Datos — Datos que Persisten** · Lección 3 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```sql
SUMARIZAR Y ORDENAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ORDENAR
  SELECT nombre, precio FROM productos ORDER BY precio DESC;      -- ASC es defecto
  ORDER BY categoria ASC, precio DESC;                             -- varias columnas

LIMITAR (paginación)
  ORDER BY precio DESC LIMIT 5 OFFSET 10;                         -- página 3 de 5 en 5

AGREGADAS (resumen de todo el grupo)
  COUNT(*)      → cuántas filas
  COUNT(email)  → cuántas no NULAS
  SUM · AVG · MIN · MAX
  SELECT COUNT(*), AVG(precio) FROM productos;

DISTINCT (únicos)
  SELECT DISTINCT categoria FROM productos;

ALIAS (legibilidad)
  SELECT AVG(precio) AS precio_promedio FROM productos;

ARITMÉTICA EN SELECT: SELECT nombre, precio * 1.22 AS con_iva FROM productos;
```

---

## 📝 Quiz de la lección

### 1. ¿Qué devuelve COUNT(*)?
- A) Columnas
- B) Número TOTAL de filas (incluyendo nulos)
- C) Promedio
- D) Suma
### 2. ORDER BY precio DESC LIMIT 5 OFFSET 10 devuelve...
- A) Los 5 más baratos
- B) Del puesto 11 al 15 en precio descendente
- C) Todo menos 10
- D) Error

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Número TOTAL de filas (incluyendo nulos) — COUNT(*) cuenta filas; COUNT(columna) omite las NULL.
**2.** ✅ Del puesto 11 al 15 en precio descendente — OFFSET salta las primeras N: base de la paginación de APIs y webs.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
