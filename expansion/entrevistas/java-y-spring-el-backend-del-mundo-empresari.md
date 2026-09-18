# 🎤 Banco de entrevista — Java y Spring — El Backend del Mundo Empresarial

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Dónde empieza a ejecutar un programa Java?**
   - El método public static void main(String[] args)  _(La firma exacta main es el punto de entrada universal de Java.)_

2. **¿Qué es la JVM?**
   - La máquina virtual que ejecuta el bytecode Java haciéndolo portable (una compilation, corre en to-do SO con JVM)  _(Compile once run anywhere: el bytecode .class corre en cualquier JVM.)_

3. **¿Qué resuelve Optional<T>?**
   - Representa explícitamente la posible ausencia de valor: obliga a decidir (orElse, ifPresent) en vez de explotar con null  _(Hacer visible el 'puede faltar' en el TIPO es el antídoto contra NullPointerException.)_

4. **streams en Java se parecen a...**
   - map/filter/reduce encadenados estilo funcional como en JS/Python  _(Operaciones declarativas sobre colecciones — Java moderno abraza lo funcional.)_

5. **¿Qué hace @RestController?**
   - Declara la clase como controlador web: los métodos responden HTTP y devuelven datos serializados (JSON)  _(@RestController = @Controller + @ResponseBody: todo método = respuesta JSON directa.)_

6. **¿Qué es inyección de dependencias en Spring?**
   - El framework crea y entrega los objetos que necesita tu clase por el constructor: cambiar implementación sin tocar tu código  _(Recibes lo que necesitas; no lo construyes: testeo con mocks y evolución sin drama.)_

7. **¿Qué hace JpaRepository con findByHechaFalse()?**
   - Spring Data genera la query automáticamente a partir del NOMBRE del método (derivada por convención)  _(Query derivation: nombras bien el método, la query existe sin escribirla.)_

8. **¿Qué papel tiene @Entity?**
   - Marca la clase como tabla de BD manejada por el ORM (cada instancia = fila)  _(El mapeo objeto-relacional (ORM): objetos Java ↔ filas SQL.)_

9. **¿Qué es H2 en este proyecto?**
   - Base de datos SQL embebida/en memoria para desarrollo rápido, reemplazable luego por PostgreSQL sin tocar el código JPA  _(H2 para arrancar sin instalar BD; cambia el datasource y punto: eso es abstracción ORM.)_

10. **¿Qué genera el .jar empaquetado con spring-boot:package?**
   - Un ejecutable autocontenido (app+servidor Tomcat embebido): dockerizar es trivial  _(El fat jar = tu app + servidor interno: corre en cualquier JVM sola.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Java y Spring y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Java y Spring con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
