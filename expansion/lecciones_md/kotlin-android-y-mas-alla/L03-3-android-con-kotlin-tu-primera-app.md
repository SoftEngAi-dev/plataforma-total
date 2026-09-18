# 3. Android con Kotlin: tu primera app

> 📚 Curso: **Kotlin — Android y Más Allá** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```kotlin
ANDROID: ACTIVITIES, VIEWS Y GRADLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Flujo: Android Studio (oficial, gratis) → New Project → "Empty Activity" → corre en emulador o tu celu por USB (activa Opciones de Desarrollador).

ESTRUCTURA CLAVE
  app/src/main/java/.../MainActivity.kt   ← tu código
  app/src/main/res/layout/activity_main.xml ← la UI (XML declarativo)
  app/build.gradle.kts                     ← dependencias/build

MAIN ACTIVITY CLÁSICA
  class MainActivity : AppCompatActivity() {
      override fun onCreate(savedInstanceState: Bundle?) {
          super.onCreate(savedInstanceState)
          setContentView(R.layout.activity_main)
          val boton = findViewById<Button>(R.id.miBoton)
          val texto = findViewById<TextView>(R.id.miTexto)
          boton.setOnClickListener { texto.text = "¡Clickeado!" }
      }
  }

CICLO DE VIDA: onCreate → onStart → onResume (visible) → onPause → onStop → onDestroy.
Respétalo: guarda estado en onSaveInstanceState, libera recursos al pausar.

HOY EN DÍA Jetpack Compose es la UI moderna (declarativa, estilo React):
  setContent { Button(onClick = { count++ }) { Text("Clicks: $count") } }
Empieza con Compose si vas nuevo: es el presente/futuro de Android.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace findViewById<Button>(R.id.miBoton)?
- A) Crea un botón
- B) Conecta el código Kotlin con la vista definida en el XML por su id
- C) Borra la vista
- D) Abre la cámara
### 2. ¿Qué es Jetpack Compose?
- A) Otro lenguaje
- B) UI declarativa de Android: describes la interfaz con funciones Kotlin y el estado la redibuja
- C) Un emulador
- D) Una BD

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Conecta el código Kotlin con la vista definida en el XML por su id — El puente código↔layout clásico; con Jetpack Compose ya no se necesita.
**2.** ✅ UI declarativa de Android: describes la interfaz con funciones Kotlin y el estado la redibuja — Mismo paradigma que React/Flutter: UI = f(estado) también en Android nativo.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
