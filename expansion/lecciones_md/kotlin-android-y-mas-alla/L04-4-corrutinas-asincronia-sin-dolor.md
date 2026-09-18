# 4. Corrutinas: asincronía sin dolor

> 📚 Curso: **Kotlin — Android y Más Allá** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```kotlin
CORRUTINAS: LO MÁS FINO DE KOTLIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Problema: red, disco y timers no deben congelar la UI (si la app se congela 5s Android muestra "no responde" y la cierra).

  import kotlinx.coroutines.*

  fun main() = runBlocking {                     // puente al mundo coroutine
      launch {                                    // nueva corrutina (liviana, miles ok)
          delay(1000)                             // espera SIN bloquear el hilo
          println("¡async!")
      }
      println("esto va primero")
  }

SUSPEND: marca funciones que pueden pausarse y reanudar:
  suspend fun descargar(): String {
      delay(2000)                                 // simula red
      return "datos"
  }
Y CÓMO LLAMARLAS: desde otra suspend o un scope:
  GlobalScope.launch { val datos = descargar(); println(datos) }

async/await (paralelo de verdad):
  val a = async { descargar("usuarios") }
  val b = async { descargar("posts") }
  println(a.await() + b.await())                  // ambas corrieron a la vez

EN ANDROID: lifecycleScope.launch { ... } — la corrutina muere sola con la pantalla (sin fugas).
DIFERENCIA CON THREADS: una corrutina pesa ~1 KB; un hilo ~1 MB. Miles de corrutinas vs cientos de hilos.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace suspend en una función?
- A) La hace más lenta
- B) Puede pausar su ejecución sin bloquear el hilo y reanudar luego
- C) La hace pública
- D) La hace final
### 2. ¿Por qué lifecycleScope en Android?
- A) Porque sí
- B) Las corrutinas de UI se cancelan solas al destruirse la pantalla: sin fugas de memoria ni crashes
- C) Es más rápido
- D) Para SQL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Puede pausar su ejecución sin bloquear el hilo y reanudar luego — suspend + delay = esperar sin congelar: la base de toda app Android moderna.
**2.** ✅ Las corrutinas de UI se cancelan solas al destruirse la pantalla: sin fugas de memoria ni crashes — Scope atado al ciclo de vida = gestión de concurrencia automática y segura.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
