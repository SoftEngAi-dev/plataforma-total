# 🎤 Banco de entrevista — Testing — Programar con Red de Seguridad

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué te permite refactorizar sin miedo?**
   - Una buena suite de tests: si rompes algo al refactor, un test grita al instante  _(El valor práctico nº1 de una suite: cambiar código con confianza.)_

2. **¿Por qué un test no debe tocar internet/reloj reales?**
   - Para ser RÁPIDO, REPETIBLE y CONFIABLE: mismo resultado siempre, en cualquier máquina, sin depender de afuera  _(Mocks/fakes sustituyen lo externo: tu test decide el comportamiento externo, no la red.)_

3. **¿Qué patrón AAA estructura un buen test?**
   - Arrange (preparar datos) → Act (ejecutar lo probado) → Assert (verificar el resultado)  _(Estructura legible y consistente: la legibilidad de los tests es deuda evitada.)_

4. **¿Qué hace pytest.raises(ValueError) en with?**
   - Verifica que el código LANZA esa excepción concreta — test del comportamiento de error  _(Probar los caminos de error es tan importante (o más) que el camino feliz.)_

5. **¿Cuándo usar mock?**
   - Cuando tu función llama a algo EXTERNO (red/BD/tiempo) y quieres probar solo tu lógica con respuestas controladas  _(El mock convierte tu entorno en laboratorio: mismos datos, siempre, instantáneo.)_

6. **¿Qué reutiliza una fixture de pytest?**
   - La preparación compartida entre muchos tests (datos de prueba, conexiones, objetos complejos)  _(Fixture = DRY aplicado a tests: un usuario demo se define una vez y todos lo usan.)_

7. **¿Cuál es la mejor forma de evitar que un bug VUELVA?**
   - Escribir PRIMERO el test que reproduce el bug: queda eternamente verificado en la suite  _(Bug→test rojo→fix→test verde= la regresión muere definitivamente.)_

8. **¿Qué diferencia test E2E de integración?**
   - E2E = flujo de usuario REAL completo (browser/UI); integración = componentes juntos sin UI necesariamente  _(Pocos E2E (frágiles/lentos pero definitivos): el pico de la pirámide.)_

9. **¿Cuál secuencia TDD correcta?**
   - 🔴 test que falla → 🟢 código mínimo que pase → 🔵 refactor mejorando sin romper el verde  _(Primero el contrato del comportamiento (test), después el código que lo cumple.)_

10. **restar(-2, -3) == 1 es un test de...**
   - CASO BORDE (números negativos): los pros testean fronteras, no solo caminos felices  _(Los bugs viven en los bordes: tu suite debe patrullarlos siempre.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Testing y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Testing con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
