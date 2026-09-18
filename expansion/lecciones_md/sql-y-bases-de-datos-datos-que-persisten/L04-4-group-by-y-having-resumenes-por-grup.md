# 4. GROUP BY y HAVING: resúmenes por grupos

> 📚 Curso: **SQL y Bases de Datos — Datos que Persisten** · Lección 4 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```sql
GROUP BY: ANALÍTICA EN UNA LÍNEA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pregunta de negocio: ¿cuánto vendí por categoría?
  SELECT categoria,
         COUNT(*) AS productos,
         SUM(precio) AS total,
         AVG(precio) AS promedio
  FROM productos
  GROUP BY categoria;

LA CASCADA LÓGICA (apréndelas de memoria — confunden a todos):
  FROM → WHERE (filtra FILAS) → GROUP BY (agrupa) → HAVING (filtra GRUPOS) → SELECT → ORDER BY

HAVING: filtra tras agrupar
  GROUP BY categoria
  HAVING SUM(precio) > 1000;       -- solo categorías que venden > 1000
  HAVING COUNT(*) >= 5;

WHERE ≠ HAVING:
  WHERE descarta filas ANTES de agrupar (usa columnas crudas)
  HAVING filtra DESPUÉS (usa resultados de agregadas)

JUGADA REAL: ¿qué clientes han hecho más de 3 pedidos?
  SELECT cliente_id, COUNT(*) AS pedidos FROM pedidos
  GROUP BY cliente_id HAVING COUNT(*) > 3 ORDER BY pedidos DESC;
```

---

## 📝 Quiz de la lección

### 1. ¿Diferencia entre WHERE y HAVING?
- A) Ninguna
- B) WHERE filtra filas antes de agrupar; HAVING filtra grupos después de la agregación
- C) HAVING es más rápido
- D) WHERE es para números
### 2. ¿Qué agregada debe estar en HAVING COUNT(*) >= 5?
- A) Ninguna permitida
- B) Las agregadas (COUNT, SUM...) se vetican en HAVING tras agrupar
- C) Solo AVG
- D) Solo SUM

---

## 🔑 Respuestas y explicaciones

**1.** ✅ WHERE filtra filas antes de agrupar; HAVING filtra grupos después de la agregación — Orden lógico: WHERE → GROUP BY → HAVING. El clásico de entrevistas.
**2.** ✅ Las agregadas (COUNT, SUM...) se vetican en HAVING tras agrupar — HAVING vive en el mundo de los grupos; las funciones agregadas habitan ahí.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
