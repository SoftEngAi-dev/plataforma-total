# 9. SQL con Python: sqlite3 práctico

> 📚 Curso: **SQL y Bases de Datos — Datos que Persisten** · Lección 9 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```sql
PYTHON + SQLITE: DATOS REALES DESDE TU CÓDIGO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  import sqlite3

  con = sqlite3.connect("plataforma.db")
  cur = con.cursor()

  # CRUD CON PARÁMETROS (¡la regla de oro del SQL!)
  cur.execute("INSERT INTO usuarios(nombre, edad) VALUES (?, ?)", ("Ada", 36))
  con.commit()

  cur.execute("SELECT * FROM usuarios WHERE edad > ?", (18,))
  for fila in cur.fetchall():      # fetchall → lista de tuplas
      print(fila)

  # Transacción segura con with (auto commit/rollback):
  with sqlite3.connect("plataforma.db") as con:
      con.execute("UPDATE ...")

⚠ SEGURIDAD CRÍTICA (SQL Injection):
  cur.execute(f"... WHERE nombre = '{nombre}'")     → MORTAL: el usuario escribe SQL
  cur.execute("... WHERE nombre = ?", (nombre,))    → SEGURO: la librería lo escapa

row_factory para dicts:
  con.row_factory = sqlite3.Row      → fila["nombre"] en vez de fila[1]
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué usar ? (parámetros) y nunca f-strings en SQL?
- A) Las f-strings son lentas
- B) Los parámetros previenen SQL injection: los datos jamás se interpretan como código
- C) Son más cortos
- D) Solo funciona con ?
### 2. ¿Qué aporta con.row_factory = sqlite3.Row?
- A) Autocommit
- B) Acceder a las columnas POR NOMBRE (fila['nombre']) en vez de índices
- C) Async
- D) Nada

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Los parámetros previenen SQL injection: los datos jamás se interpretan como código — Con f-strings, un usuario malicioso escribe SQL dentro de tu consulta: el primer ataque web de la historia.
**2.** ✅ Acceder a las columnas POR NOMBRE (fila['nombre']) en vez de índices — Código legible y resistente a cambios de orden de columnas.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
