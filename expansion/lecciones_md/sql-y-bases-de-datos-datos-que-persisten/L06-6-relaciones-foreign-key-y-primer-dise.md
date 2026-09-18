# 6. Relaciones: FOREIGN KEY y primer diseño

> 📚 Curso: **SQL y Bases de Datos — Datos que Persisten** · Lección 6 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```sql
MODELO RELACIONAL: NORMALIZAR BIEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Los datos se separan en entidades y se conectan por claves:

  CREATE TABLE autores (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre TEXT NOT NULL UNIQUE
  );
  CREATE TABLE libros (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      titulo TEXT NOT NULL,
      autor_id INTEGER NOT NULL REFERENCES autores(id)   -- FOREIGN KEY
  );

REGLA: NO repitas datos en varias filas (nombre del autor mil veces); ponlo una vez y enlaza.

TIPOS DE RELACIÓN
• 1 a muchos: autor → libros (FK en el lado "muchos": libros.autor_id)
• muchos a muchos: estudiantes ↔ cursos → tabla intermedia:
  inscripciones(estudiante_id, curso_id, fecha, PRIMARY KEY(estudiante_id, curso_id))
• 1 a 1: user ↔ perfil (FK UNIQUE)

ON DELETE: qué pasa con los libros si borro el autor
  REFERENCES autores(id) ON DELETE CASCADE    (borrar hijos) / SET NULL / RESTRICT
```

---

## 📝 Quiz de la lección

### 1. ¿Dónde va la FK en una relación 1 a muchos (autor-libros)?
- A) En autores
- B) En libros (el lado 'muchos')
- C) En ambos
- D) En una tabla aparte
### 2. ¿Cómo se modela muchos-a-muchos?
- A) Con arrays
- B) Tabla intermedia con ambas FK y PK compuesta
- C) Duplicando datos
- D) No se puede

---

## 🔑 Respuestas y explicaciones

**1.** ✅ En libros (el lado 'muchos') — Cada libro apunta a su autor: FK en la tabla del lado N.
**2.** ✅ Tabla intermedia con ambas FK y PK compuesta — La tabla puente (inscripciones) convierte M:N en dos relaciones 1:N.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
