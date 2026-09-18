# 🎤 Banco de entrevista — Kotlin — Android y Más Allá

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué diferencia val de var en Kotlin?**
   - val es inmutable (referencia fija); var es reasignable  _(Kotlin te empuja a inmutabilidad por defecto: val primero, var solo si hace falta.)_

2. **¿Qué hace ?: (operador Elvis)?**
   - Si lo de la izquierda es null, devuelve lo de la derecha  _(Elvis porque parece un peinado ?:  — null coalescing con nombre rockero.)_

3. **¿Qué genera automáticamente una data class?**
   - equals(), hashCode(), toString(), copy() y componentN() — todo el boilerplate de datos  _(Una línea reemplaza 50 de Java: define campos y listo.)_

4. **En listOf(1,2,3).map { it * 2 }, ¿qué es 'it'?**
   - El parámetro implícito de la lambda cuando hay uno solo  _(Lambdas de un parámetro pueden usar 'it' sin declararlo — típico estilo Kotlin.)_

5. **¿Qué hace findViewById<Button>(R.id.miBoton)?**
   - Conecta el código Kotlin con la vista definida en el XML por su id  _(El puente código↔layout clásico; con Jetpack Compose ya no se necesita.)_

6. **¿Qué es Jetpack Compose?**
   - UI declarativa de Android: describes la interfaz con funciones Kotlin y el estado la redibuja  _(Mismo paradigma que React/Flutter: UI = f(estado) también en Android nativo.)_

7. **¿Qué hace suspend en una función?**
   - Puede pausar su ejecución sin bloquear el hilo y reanudar luego  _(suspend + delay = esperar sin congelar: la base de toda app Android moderna.)_

8. **¿Por qué lifecycleScope en Android?**
   - Las corrutinas de UI se cancelan solas al destruirse la pantalla: sin fugas de memoria ni crashes  _(Scope atado al ciclo de vida = gestión de concurrencia automática y segura.)_

9. **¿Qué hace remember { mutableStateOf(0) }?**
   - Estado que Compose observa: al cambiarlo, las funciones que lo leen se redibujan solas  _(El equivalente a useState de React pero nativo Android: UI reactiva real.)_

10. **¿Qué difiere Compose de los layouts XML clásicos?**
   - UI como código Kotlin declarativo (funciones + estado) en vez de XML + findViewById imperativo  _(Menos glue code, mismo paradigma que React/Flutter: el futuro oficial de Android.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Kotlin y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Kotlin con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
