# 3. PDO: bases de datos sin inyección

> 📚 Curso: **PHP y Laravel — El Backend Que Alimenta la Web** · Lección 3 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```php
PDO: SQL SEGURO EN PHP
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  $pdo = new PDO("sqlite:".__DIR__."/datos.db");
  $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

CREAR Y ESCRIBIR (prepared: USA SIEMPRE)
  $pdo->exec("CREATE TABLE IF NOT EXISTS tareas(id INTEGER PRIMARY KEY, titulo TEXT)");
  $stmt = $pdo->prepare("INSERT INTO tareas(titulo) VALUES (?)");
  $stmt->execute([$_POST["titulo"]]);           // los datos VAN SEPARADOS del SQL

LEER (fetch asociativo, EL dict php)
  $stmt = $pdo->prepare("SELECT * FROM tareas WHERE id = ?");
  $stmt->execute([$id]);
  $tarea = $stmt->fetch(PDO::FETCH_ASSOC);     // ['id'=>1,'titulo'=>'x']
  $todas = $pdo->query("SELECT * FROM tareas")->fetchAll(PDO::FETCH_ASSOC);

REGLA DE ORO DE NUEVO:
  "... VALUES ('".$_POST['x']."')"     → ☠ SQL INJECTION (¡el clásico de los clásicos!)
  prepare + execute                  → seguro por diseño

PDO misma API para SQLite/MySQL/PostgreSQL — cambias una línea al crecer.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué protegen los prepared statements?
- A) La velocidad
- B) SQL injection: los datos van apartados del SQL y nunca se interpretan como código
- C) El código PHP
- D) La memoria
### 2. ¿Qué PDO::FETCH_ASSOC devuelve?
- A) XML
- B) Cada fila como array asociativo ['columna'=>valor]
- C) Objetos siempre
- D) CSV

---

## 🔑 Respuestas y explicaciones

**1.** ✅ SQL injection: los datos van apartados del SQL y nunca se interpretan como código — prepare() separa instrucción de datos: ' OR 1=1 -- queda como simple texto.
**2.** ✅ Cada fila como array asociativo ['columna'=>valor] — Acceso por nombre de columna: código legible y resiliente.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
