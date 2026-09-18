# 10. Diseño final: modelar una app real en SQL

> 📚 Curso: **SQL y Bases de Datos — Datos que Persisten** · Lección 10 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```sql
DISEÑA: BLOG COMPLETO EN SQL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ejercicio sombrero: esquema real con todo el curso (ejecútalo en sqlite3):

  CREATE TABLE usuarios (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE NOT NULL,
      email TEXT UNIQUE NOT NULL,
      creado TEXT DEFAULT CURRENT_TIMESTAMP
  );
  CREATE TABLE posts (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
      titulo TEXT NOT NULL,
      cuerpo TEXT NOT NULL,
      publicado INTEGER DEFAULT 0 CHECK(publicado IN (0,1)),
      creado TEXT DEFAULT CURRENT_TIMESTAMP
  );
  CREATE TABLE comentarios (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      post_id INTEGER NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
      usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
      texto TEXT NOT NULL
  );
  CREATE INDEX idx_posts_usuario ON posts(usuario_id);

CONSULTA FINAL: los 5 posts con más comentarios
  SELECT p.titulo, COUNT(c.id) AS comentarios
  FROM posts p LEFT JOIN comentarios c ON c.post_id = p.id
  GROUP BY p.id ORDER BY comentarios DESC LIMIT 5;

✅ CHECKLIST DEL ESQUEMA BUENO: PKs · FKs con comportamiento ON DELETE · UNIQUE donde sea verdad · CHECKs · índices en columnas de búsqueda · nombres plural y snake_case.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué CASCADE en comentarios de un post borrado?
- A) Velocidad
- B) No quedan comentarios huérfanos de posts inexistentes
- C) Decora
- D) Sumar
### 2. ¿Qué patrón se repite en todo esquema serio?
- A) Todo en una tabla
- B) Entidades separadas + FKs + restricciones + índices en búsquedas frecuentes
- C) Solo JSON
- D) Sin PKs

---

## 🔑 Respuestas y explicaciones

**1.** ✅ No quedan comentarios huérfanos de posts inexistentes — La integridad referencial gestionada por la base: consistencia siempre.
**2.** ✅ Entidades separadas + FKs + restricciones + índices en búsquedas frecuentes — Normalización + restricciones = la base no permite corrupción de datos desde afuera.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
