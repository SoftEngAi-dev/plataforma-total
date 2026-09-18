# 5. CREATE, INSERT, UPDATE, DELETE: escribir datos

> 📚 Curso: **SQL y Bases de Datos — Datos que Persisten** · Lección 5 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```sql
CRUD COMPLETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CREAR TABLA
  CREATE TABLE productos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,   -- SQLite
      nombre TEXT NOT NULL,
      precio NUMERIC CHECK (precio >= 0),
      categoria TEXT DEFAULT 'general',
      creado TEXT DEFAULT CURRENT_TIMESTAMP
  );

INSERT
  INSERT INTO productos (nombre, precio) VALUES ('Café', 120);
  INSERT INTO productos (nombre, precio) VALUES ('Pan', 45), ('Té', 80);

UPDATE — siempre con WHERE
  UPDATE productos SET precio = 110 WHERE id = 1;
⚠ UPDATE sin WHERE cambia TODA la tabla — regla 1 de un DBA.

DELETE — siempre con WHERE
  DELETE FROM productos WHERE id = 3;
⚠ DELETE sin WHERE vacía la tabla.

RESTRICCIONES (integrity gratis): NOT NULL · UNIQUE · DEFAULT · CHECK · PRIMARY KEY
La base rechaza datos inválidos aunque tu código se equivoque. Ponlas siempre: la integridad vive en la BD, no en tu app.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué UPDATE sin WHERE es un desastre clásico?
- A) Es error de sintaxis
- B) Actualiza TODAS las filas de la tabla
- C) Es más lento
- D) Solo en MySQL
### 2. ¿Qué gana poner NOT NULL y CHECK en CREATE TABLE?
- A) Decora
- B) La base de datos rechaza datos inválidos aunque bugs de la app los intenten insertar
- C) Nada
- D) Velocidad de index

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Actualiza TODAS las filas de la tabla — Sin filtro = global: regla para la vida: escribe primero el WHERE... y después UPDATE/DELETE junto.
**2.** ✅ La base de datos rechaza datos inválidos aunque bugs de la app los intenten insertar — La última línea de defensa de la calidad de datos está en el esquema.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
