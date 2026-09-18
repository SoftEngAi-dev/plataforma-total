# 📕 Resumen maestro — SQL y Bases de Datos — Datos que Persisten

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Bases de datos y SQL: el lenguaje de los datos
SQL: HABLARLE A LOS DATOS DESDE 1974 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Base de datos = tablas relacionadas con estructura estricta. SQL = el lenguaje para consultarlas. Misma sintaxi…

## 2. 2. SELECT con WHERE: filtrar con precisión
FILTRAR ADULTOS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   SELECT nombre, precio   FROM productos   WHERE precio > 100;               -- comentario con dos guiones  OPERADORES   = · != · > …

## 3. 3. Ordenar, limitar y funciones agregadas
SUMARIZAR Y ORDENAR ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ORDENAR   SELECT nombre, precio FROM productos ORDER BY precio DESC;      -- ASC es defecto   ORDER BY categoria ASC, precio DES…

## 4. 4. GROUP BY y HAVING: resúmenes por grupos
GROUP BY: ANALÍTICA EN UNA LÍNEA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Pregunta de negocio: ¿cuánto vendí por categoría?   SELECT categoria,          COUNT(*) AS productos,          SUM(…

## 5. 5. CREATE, INSERT, UPDATE, DELETE: escribir datos
CRUD COMPLETO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ CREAR TABLA   CREATE TABLE productos (       id INTEGER PRIMARY KEY AUTOINCREMENT,   -- SQLite       nombre TEXT NOT NULL,       preci…

## 6. 6. Relaciones: FOREIGN KEY y primer diseño
MODELO RELACIONAL: NORMALIZAR BIEN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Los datos se separan en entidades y se conectan por claves:    CREATE TABLE autores (       id INTEGER PRIMARY KE…

## 7. 7. JOINs: consultar varias tablas
JOINS: PEGAR TABLAS POR SUS CLAVES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ INNER JOIN (intersección): solo lo que coincide en ambas   SELECT l.titulo, a.nombre   FROM libros l   JOIN autor…

## 8. 8. Índices y transacciones: velocidad y seguridad
ÍNDICES: DEL O(n) AL O(log n) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Sin índice, buscar email es leer TODA la tabla. Con índice, es un árbol: rapidísimo.   CREATE INDEX idx_email ON usuar…

## 9. 9. SQL con Python: sqlite3 práctico
PYTHON + SQLITE: DATOS REALES DESDE TU CÓDIGO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   import sqlite3    con = sqlite3.connect("plataforma.db")   cur = con.cursor()    # CRUD CON PARÁMETR…

## 10. 10. Diseño final: modelar una app real en SQL
DISEÑA: BLOG COMPLETO EN SQL ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Ejercicio sombrero: esquema real con todo el curso (ejecútalo en sqlite3):    CREATE TABLE usuarios (       id INTEGER …

---
✅ 10 lecciones · 📝 20 preguntas de repaso en quizzes_html/ · tests/