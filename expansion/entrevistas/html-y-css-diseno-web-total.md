# 🎤 Banco de entrevista — HTML y CSS — Diseño Web Total

> 20 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué define HTML en una página web?**
   - La estructura y el significado del contenido  _(HTML = estructura/semántica; CSS = presentación; JS = comportamiento.)_

2. **¿Para qué sirve <head> en un documento HTML?**
   - Metadatos: title, charset, enlaces a CSS/JS — no se muestra en la página  _(Todo lo de <head> configura la página; lo visible vive en <body>.)_

3. **¿Qué atributo hace que el dato de un input llegue al servidor?**
   - name  _(Sin name, el input no viaja con el formulario.)_

4. **¿Por qué validar también en el servidor si el HTML ya valida?**
   - Porque la validación del cliente se puede saltar/falsificar  _(Toda entrada del cliente es hostil hasta que el servidor la valida.)_

5. **¿Qué selector tiene más especificidad?**
   - id (#principal)  _(id gana sobre clase y etiqueta. Inline style gana sobre todos.)_

6. **¿Qué hace box-sizing: border-box?**
   - width/height incluyen padding y border (lo intuitivo)  _(Sin él, width:100px + padding te da una caja de más de 100px; con él, es exacto.)_

7. **¿Qué línea centra un elemento horizontal y verticalmente dentro de su padre?**
   - display:flex; justify-content:center; align-items:center  _(Flexbox con ambos ejes centrados — el centramiento perfecto ya no es chiste.)_

8. **¿Qué hace flex: 1 en un hijo?**
   - Lo hace crecer para repartir el espacio sobrante del contenedor  _(flex-grow/shrink/basis abreviado: típicamente reparte el espacio equitativamente.)_

9. **¿Qué hace repeat(auto-fit, minmax(250px, 1fr))?**
   - Columnas dinámicas: entran las quepan con mínimo 250px y rellenan el espacio  _(El patrón responsive por excelencia: se adapta solo al ancho disponible.)_

10. **¿Cuándo elegir Grid sobre Flexbox?**
   - Cuando el diseño es bidimensional (filas y columnas)  _(Flex = una dimensión; Grid = dos. Conviven felices.)_

11. **¿Qué hace la meta etiqueta viewport?**
   - Dice al móvil que use el ancho real del dispositivo y no una miniatura  _(Sin ella, el móvil renderiza como si fuera un desktop de 980px y escala.)_

12. **¿Qué significa mobile-first?**
   - Escribir el CSS base para móvil y crecer con min-width media queries  _(Base simple en pantalla chica; complejidad progresiva hacia pantallas grandes.)_

13. **¿Qué ventaja da definir colores como variables en :root?**
   - Cambias una línea y actualizas toda la web (sistema de diseño)  _(Las variables convierten estilos sueltos en un sistema coherente y mantenible.)_

14. **¿Cuál es el largo de línea recomendado para texto legible?**
   - ~45-75 caracteres (65ch) por línea  _(Líneas demasiado largas cansan la vista: limita el ancho del texto.)_

15. **¿Qué propiedades se deben animar para rendimiento fluido?**
   - transform y opacity  _(Solo esas dos no provocan reflow/repaint del layout: la GPU las acelera.)_

16. **¿Qué duración se siente natural en micro-interacciones de UI?**
   - 150-300ms  _(Suficiente para percibirse, corto para no frenar.)_

17. **¿Cuál es el éxito mínimo del proyecto?**
   - Que se vea bien tanto en móvil como en desktop  _(Responsive sólido es la meta; el gusto se entrena después.)_

18. **¿Qué combinación cubre los layouts del proyecto?**
   - Flexbox para el nav + Grid para las tarjetas  _(Flex para 1 dimensión (nav), Grid para 2 (cards): la receta moderna.)_

19. **¿Qué elemento es correcto para acción clickeable accesible?**
   - <button>  _(<button> trae gratis: foco de teclado, Enter/Espacio, y semántica para lectores de pantalla.)_

20. **¿Cuál es el contraste mínimo texto/fondo recomendado?**
   - 4.5:1  _(WCAG AA: 4.5:1 para texto normal (3:1 para texto grande).)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve HTML y CSS y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta HTML y CSS con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
