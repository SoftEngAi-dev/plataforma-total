# 1. Bases de datos y SQL: el lenguaje de los datos

> 📚 Curso: **SQL y Bases de Datos — Datos que Persisten** · Lección 1 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```sql
SQL: HABLARLE A LOS DATOS DESDE 1974
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Base de datos = tablas relacionadas con estructura estricta. SQL = el lenguaje para consultarlas. Misma sintaxis en PostgreSQL, MySQL, SQLite...

TU PRIMERA CONSULTA
  SELECT nombre, precio FROM productos;

CONCEPTOS
• Tabla (relación): filas y columnas
• Fila = registro · Columna = atributo (con tipo: INTEGER, TEXT, NUMERIC, DATE, BOOLEAN...)
• EN VERDAD: SQLITE incluida en tu sistema: no hay nada que instalar. Esta app misma la usa.
  sqlite3 datos.db  → abre la consola sqlite (o en Python: import sqlite3)

PK (primary key): identificador único de cada fila — casi siempre id autoincremental.

SQL ES DECLARATIVO: dices QUÉ quieres ("productos caros"), no CÓMO recorrerlos. El motor se encarga de la eficiencia.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace SELECT nombre, precio FROM productos?
- A) Crea la tabla
- B) Devuelve solo esas dos columnas de la tabla productos
- C) Inserta datos
- D) Borra filas
### 2. ¿Por qué SQLite es ideal para aprender/apps locales?
- A) Es para datos simples nada más
- B) Zero-config: la base ES un archivo; sin servidor, incluida en Python y en todos los SO
- C) No soporta SQL real
- D) Solo Mac

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Devuelve solo esas dos columnas de la tabla productos — SELECT = leer columnas elegidas de una tabla: la consulta más básica.
**2.** ✅ Zero-config: la base ES un archivo; sin servidor, incluida en Python y en todos los SO — Sin instalar servidor, pero con SQL completo: perfecta para apps desktop/móvil y aprender.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
