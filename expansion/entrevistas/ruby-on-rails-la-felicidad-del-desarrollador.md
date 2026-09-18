# 🎤 Banco de entrevista — Ruby on Rails — La Felicidad del Desarrollador

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Cómo interpola cadenas Ruby?**
   - "#{variable}" dentro de comillas dobles  _(#{} solo en comillas dobles — distinción que bugs de novato llenan.)_

2. **¿Qué devuelve un método Ruby sin return?**
   - La última expresión evaluada (return implícito)  _("Lo último se devuelve" — por eso casi no verás return en Ruby idiomático.)_

3. **¿Qué es el 'scaffold' de Rails?**
   - Generador del CRUD completo (modelo, migración, controller, vistas, rutas) desde una consola  _(Ideal para aprender el MVC viendo todas las piezas en acción y de una vez.)_

4. **¿Qué significa Convention over Configuration?**
   - El framework asume estándares sensatos (Post↔posts, id PK...) y tú solo configuras lo distinto  _(CoC = menos decisiones triviales = velocidad de desarrollo enorme.)_

5. **¿Qué hace validates :titulo, presence: true?**
   - Rechaza guardar si falta el título; el objeto retorna valid? false con errores  _(Validaciones a nivel MODELO = defensa total (formulario, API, consola).)_

6. **has_many :posts presupone...**
   - Que la tabla posts tiene columna autor_id (convención Rails que la FK sigue el modelo singular+_id)  _(Por convención no tienes que decírselo: la FK es visible: autor_id.)_

7. **¿Diferencia entre <% %> y <%= %> en ERB?**
   - <% ejecuta sin imprimir (loops/ifs); <%= ejecuta E IMPRIME escapando HTML  _(El clásico bug: poner <%= en un @each y ver la lista entera impresa.)_

8. **¿Qué hace form_with model: @post?**
   - Formulario automático ligado al modelo: crea o edita según el objeto, con token CSRF incluido  _(Los helpers sienten la convención: si @post es nuevo → POST /posts; si existe → PATCH.)_

9. **¿Para qué sirve un scope en el modelo Rails?**
   - Guardar consultas frecuentes como métodos reutilizables: Post.publicados  _(Scope = query con nombre: lisible y combinables (Post.publicados.recientes).)_

10. **AddAutor a posts con autor:references en migración hace...**
   - Crea la columna autor_id + índice + FK en la tabla posts (relación completa en SQL)  _(Las migraciones versionan tu esquema en código: la BD se recrea con rails db:migrate.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Ruby on Rails y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Ruby on Rails con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
