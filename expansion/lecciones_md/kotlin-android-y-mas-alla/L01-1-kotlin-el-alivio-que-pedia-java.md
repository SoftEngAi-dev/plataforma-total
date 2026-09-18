# 1. Kotlin: el alivio que pedía Java

> 📚 Curso: **Kotlin — Android y Más Allá** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```kotlin
KOTLIN: JAVA MODERNIZADA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lenguaje de JetBrains, oficial para Android desde 2017. Corre sobre la JVM, interopera 100% con Java y quita el dolor: null-safety, brevedad, data classes.

  fun main() {
      val nombre = "Ada"               // val = INMUTABLE (const)
      var edad: Int = 36               // var = mutable · tipo explícito (inferencia si asignas)
      println("Hola, $nombre, $edad")  // interpolación con $
      edad = 37                        // ✅ var permite; nombre = "X" daría ERROR (val)

      val frutas = listOf("🍎", "🍌", "🥝")      // lista inmutable
      val numeros = mutableListOf(1, 2, 3)        // mutable
      numeros.add(4)

      for (f in frutas) println(f)
      for (i in 1..5) println(i)                  // rangos: 1..5 incluye ambos

      val descripcion = when {                    // when = switch elegante/expresión
          edad >= 18 -> "mayor"
          else -> "menor"
      }
  }

NULL-SAFETY NUCLEAR: String no puede ser null; String? SÍ puede y el compilador te OBLIGA a manejarlo:
  var apodo: String? = null
  println(apodo?.length)        // ?. = llama solo si no es null (devuelve null si lo es)
  println(apodo?.length ?: 0)   // ?: Elvis: valor por defecto
```

---

## 📝 Quiz de la lección

### 1. ¿Qué diferencia val de var en Kotlin?
- A) Son iguales
- B) val es inmutable (referencia fija); var es reasignable
- C) val es para números
- D) var es más rápido
### 2. ¿Qué hace ?: (operador Elvis)?
- A) Nada
- B) Si lo de la izquierda es null, devuelve lo de la derecha
- C) Compara strings
- D) Bucle

---

## 🔑 Respuestas y explicaciones

**1.** ✅ val es inmutable (referencia fija); var es reasignable — Kotlin te empuja a inmutabilidad por defecto: val primero, var solo si hace falta.
**2.** ✅ Si lo de la izquierda es null, devuelve lo de la derecha — Elvis porque parece un peinado ?:  — null coalescing con nombre rockero.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
