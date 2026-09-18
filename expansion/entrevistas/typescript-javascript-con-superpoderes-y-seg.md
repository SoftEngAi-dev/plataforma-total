# 🎤 Banco de entrevista — TypeScript — JavaScript con Superpoderes y Seguridad

> 14 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué es TypeScript exactamente?**
   - JavaScript + chequeo estático de tipos que se compila a JS puro  _(Superconjunto tipado: corre como JS tras compilar — el navegador jamás ve tipos.)_

2. **¿Cuándo detecta TypeScript los errores de tipo?**
   - Al editar/compilar, antes de ejecutar  _(Shift-left: el error aparece cuando lo escribes, no cuando el usuario lo encuentra.)_

3. **¿Cuándo anotar tipos explícitamente?**
   - Cuando la inferencia no es obvia (y siempre en firmas de funciones públicas)  _(TS infiere en la asignación; anota donde el contrato importa.)_

4. **¿Qué diferencia hay entre any y unknown?**
   - any desactiva toda verificación; unknown exige comprobar el tipo antes de usarlo  _(unknown = 'no sé aún, pero TS me protege'; any = 'ríndete, compilador'.)_

5. **¿Cuándo elegir interface sobre type?**
   - Para formas de objetos: más legible, mensajes de error claros y extensión natural  _(Interface para modelos de dominio; type para uniones y composiciones.)_

6. **¿Qué expresa type Estado = "cargando" | "ok" | "error"?**
   - Una unión de literales: la variable solo vale uno de esos strings  _(Uniones de literales = estados exhaustivos que TS puede verificar (sin strings sueltos).)_

7. **¿Qué gana identidad<T>(v: T): T respecto a misto?: any?**
   - Recuerda el tipo exacto de entrada y lo devuelve: autocomplete y chequeo completos  _(Los genéricos modelan RELACIONES entre tipos — any solo las borra.)_

8. **¿Qué hace <T extends { length: number }>?**
   - Restringe T a tipos que tengan la propiedad length  _(Constraint: puedo usar .length sabiendo que el compilador lo garantiza.)_

9. **¿Qué permite una propiedad private?**
   - Solo acceso dentro de la propia clase  _(Encapsulación: el estado interno solo cambia por métodos controlados.)_

10. **¿Para qué sirve implements?**
   - Obligar a la clase a cumplir el contrato de una interface  _(El compilador verifica que cumples el contrato — la base de sustituir implementaciones (mocks, DBs).)_

11. **¿Qué es una discriminated union?**
   - Una unión donde cada variante tiene una clave literal común (kind) que permite narrowing  _(El patrón de modelado de estados favorito en TS: cada rama decide la forma disponible.)_

12. **¿Qué significa x is string en un type guard?**
   - Le dice a TS: si esta función devuelve true, trata x como string de ahí en adelante  _(Los guards personalizados enseñan al compilador a razonar sobre tus datos.)_

13. **¿Qué activa "strict": true en tsconfig?**
   - Una familia de protecciones: null checks, noImplicitAny, etc. — el modo serio de TS  _(Strict atrapa el grueso de los bugs de tipo. Proyecto profesional sin strict = medio TS.)_

14. **¿Cómo usar tipos con una librería JS como express?**
   - npm i -D @types/express (definiciones de tipos de la comunidad)  _(@types/* cubre todo el ecosistema popular: tu editor la entiende como si fuera TS nativa.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve TypeScript y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta TypeScript con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
