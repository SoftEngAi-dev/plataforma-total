# 🎤 Banco de entrevista — SQL y Bases de Datos — Datos que Persisten

> 20 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué hace SELECT nombre, precio FROM productos?**
   - Devuelve solo esas dos columnas de la tabla productos  _(SELECT = leer columnas elegidas de una tabla: la consulta más básica.)_

2. **¿Por qué SQLite es ideal para aprender/apps locales?**
   - Zero-config: la base ES un archivo; sin servidor, incluida en Python y en todos los SO  _(Sin instalar servidor, pero con SQL completo: perfecta para apps desktop/móvil y aprender.)_

3. **¿Cómo verificar si un campo es NULL?**
   - campo IS NULL  _(NULL no es un valor; solo IS NULL funciona — bug clásico en todo el mundo.)_

4. **SELECT * FROM empleados WHERE nombre LIKE 'Ana%' busca...**
   - Nombres que EMPIEZAN por Ana ( % = comodín de caracteres)  _(% sustituye cualquier secuencia; Ana% = empieza por.)_

5. **¿Qué devuelve COUNT(*)?**
   - Número TOTAL de filas (incluyendo nulos)  _(COUNT(*) cuenta filas; COUNT(columna) omite las NULL.)_

6. **ORDER BY precio DESC LIMIT 5 OFFSET 10 devuelve...**
   - Del puesto 11 al 15 en precio descendente  _(OFFSET salta las primeras N: base de la paginación de APIs y webs.)_

7. **¿Diferencia entre WHERE y HAVING?**
   - WHERE filtra filas antes de agrupar; HAVING filtra grupos después de la agregación  _(Orden lógico: WHERE → GROUP BY → HAVING. El clásico de entrevistas.)_

8. **¿Qué agregada debe estar en HAVING COUNT(*) >= 5?**
   - Las agregadas (COUNT, SUM...) se vetican en HAVING tras agrupar  _(HAVING vive en el mundo de los grupos; las funciones agregadas habitan ahí.)_

9. **¿Por qué UPDATE sin WHERE es un desastre clásico?**
   - Actualiza TODAS las filas de la tabla  _(Sin filtro = global: regla para la vida: escribe primero el WHERE... y después UPDATE/DELETE junto.)_

10. **¿Qué gana poner NOT NULL y CHECK en CREATE TABLE?**
   - La base de datos rechaza datos inválidos aunque bugs de la app los intenten insertar  _(La última línea de defensa de la calidad de datos está en el esquema.)_

11. **¿Dónde va la FK en una relación 1 a muchos (autor-libros)?**
   - En libros (el lado 'muchos')  _(Cada libro apunta a su autor: FK en la tabla del lado N.)_

12. **¿Cómo se modela muchos-a-muchos?**
   - Tabla intermedia con ambas FK y PK compuesta  _(La tabla puente (inscripciones) convierte M:N en dos relaciones 1:N.)_

13. **¿Qué registros incluye LEFT JOIN que INNER no?**
   - Los de la tabla izquierda sin coincidencia (con NULLs en la derecha)  _(LEFT preserva el lado izquierdo completo: ideal para 'X con o sin Y'.)_

14. **SELECT COUNT(l.id) con LEFT JOIN + GROUP BY autor da 0 cuando...**
   - El autor no tiene libros (las NULL no se cuentan en COUNT)  _(COUNT(columna) no cuenta NULLs: encaja perfecto con LEFT JOIN para conteos con cero.)_

15. **¿Cuándo crear un índice?**
   - En columnas usadas frecuentemente en WHERE/JOIN (con costo de escritura)  _(Índices aceleran lecturas pero encarecen escrituras: sobredimensionarlos es deuda.)_

16. **¿Qué garantiza una transacción bancaria (BEGIN...COMMIT)?**
   - Las dos actualizaciones suceden juntas o ninguna (atomicidad)  _(Si falla a mitad, ROLLBACK: nunca hay dinero perdido en el aire.)_

17. **¿Por qué usar ? (parámetros) y nunca f-strings en SQL?**
   - Los parámetros previenen SQL injection: los datos jamás se interpretan como código  _(Con f-strings, un usuario malicioso escribe SQL dentro de tu consulta: el primer ataque web de la historia.)_

18. **¿Qué aporta con.row_factory = sqlite3.Row?**
   - Acceder a las columnas POR NOMBRE (fila['nombre']) en vez de índices  _(Código legible y resistente a cambios de orden de columnas.)_

19. **¿Por qué CASCADE en comentarios de un post borrado?**
   - No quedan comentarios huérfanos de posts inexistentes  _(La integridad referencial gestionada por la base: consistencia siempre.)_

20. **¿Qué patrón se repite en todo esquema serio?**
   - Entidades separadas + FKs + restricciones + índices en búsquedas frecuentes  _(Normalización + restricciones = la base no permite corrupción de datos desde afuera.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve SQL y Bases de Datos y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta SQL y Bases de Datos con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
