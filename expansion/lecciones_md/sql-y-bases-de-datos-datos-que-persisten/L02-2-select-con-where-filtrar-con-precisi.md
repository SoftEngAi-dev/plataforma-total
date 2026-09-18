# 2. SELECT con WHERE: filtrar con precisión

> 📚 Curso: **SQL y Bases de Datos — Datos que Persisten** · Lección 2 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```sql
FILTRAR ADULTOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SELECT nombre, precio
  FROM productos
  WHERE precio > 100;               -- comentario con dos guiones

OPERADORES
  = · != · > · < · >= · <=
  BETWEEN 5 AND 10          (inclusive)
  IN ('a', 'b')
  LIKE 'Ana%'               (empieza por) · '%ana' · '%ana%'
  IS NULL / IS NOT NULL     (⚠ NULL = NULL es falso; usa IS)
  AND · OR · NOT

CUIDADO CON NULL: null significa DESCONOCIDO — no es igual a nada, ni siquiera a otro null:
  WHERE edad = NULL     → siempre vacío
  WHERE edad IS NULL    → correcto

COMBINAR CON PARÉNTESIS (la precedencia anda traicionera):
  WHERE (precio > 100 OR oferta = 1) AND activo = 1;

PRÁCTICA: pon datos juguete en una tabla en tu SQLite y escribe 5 WHERE distintos. 10 minutos.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo verificar si un campo es NULL?
- A) campo = NULL
- B) campo IS NULL
- C) campo == NULL
- D) NULL(campo)
### 2. SELECT * FROM empleados WHERE nombre LIKE 'Ana%' busca...
- A) Nombres que terminan en Ana
- B) Nombres que EMPIEZAN por Ana ( % = comodín de caracteres)
- C) Exactamente 'Ana%'
- D) Todo lo que no sea Ana

---

## 🔑 Respuestas y explicaciones

**1.** ✅ campo IS NULL — NULL no es un valor; solo IS NULL funciona — bug clásico en todo el mundo.
**2.** ✅ Nombres que EMPIEZAN por Ana ( % = comodín de caracteres) — % sustituye cualquier secuencia; Ana% = empieza por.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
