# 2. Funciones y data classes: brevedad con tipos

> 📚 Curso: **Kotlin — Android y Más Allá** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```kotlin
FUNCIONES Y CLASES SIN CEREMONIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  fun suma(a: Int, b: Int = 2): Int = a + b      // single-expression + default
  fun saludar(nombre: String = "mundo") = "Hola, $nombre"   // sin tipo: infiere
  saludar(nombre = "Ada")                        // ARGUMENTOS NOMBRADOS (legibilidad)

NULL HANDLING EN FUNCIONES
  fun largo(s: String?): Int = s?.length ?: 0    // acepta null, devuelve Int seguro

DATA CLASS — el record de Kotlin (toString/equals/hashCode/copy gratis):
  data class Tarea(val titulo: String, var hecha: Boolean = false)
  val t = Tarea("Estudiar Kotlin")
  val copia = t.copy(hecha = true)               // copia con cambios (inmutabilidad fácil)
  println(t)   // Tarea(titulo=Estudiar Kotlin, hecha=false)  ← toString útil auto

CLASES NORMALES + herencia (open = permite heredar, por defecto selladas):
  open class Animal(val nombre: String) { open fun sonido() = "..." }
  class Perro(nombre: String) : Animal(nombre) { override fun sonido() = "¡Guau!" }

LAMBDAS estilo funcional: listOf(1,2,3,4).filter { it % 2 == 0 }.map { it * 10 }  // 'it' implícito
```

---

## 📝 Quiz de la lección

### 1. ¿Qué genera automáticamente una data class?
- A) Solo getters
- B) equals(), hashCode(), toString(), copy() y componentN() — todo el boilerplate de datos
- C) SQL
- D) Nada
### 2. En listOf(1,2,3).map { it * 2 }, ¿qué es 'it'?
- A) Un error
- B) El parámetro implícito de la lambda cuando hay uno solo
- C) Un global
- D) Un índice

---

## 🔑 Respuestas y explicaciones

**1.** ✅ equals(), hashCode(), toString(), copy() y componentN() — todo el boilerplate de datos — Una línea reemplaza 50 de Java: define campos y listo.
**2.** ✅ El parámetro implícito de la lambda cuando hay uno solo — Lambdas de un parámetro pueden usar 'it' sin declararlo — típico estilo Kotlin.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
