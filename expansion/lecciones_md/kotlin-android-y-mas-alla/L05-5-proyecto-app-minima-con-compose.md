# 5. Proyecto: app mínima con Compose

> 📚 Curso: **Kotlin — Android y Más Allá** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```kotlin
CONSTRUYE: CONTADOR APP CON JETPACK COMPOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Android Studio → New Project → Empty Activity (Compose)
2. En MainActivity.kt, dentro de setContent { }:

  var cuenta by remember { mutableStateOf(0) }   // estado: redibuja solo al cambiar

  Column(
      modifier = Modifier.fillMaxSize().padding(24.dp),
      verticalArrangement = Arrangement.Center,
      horizontalAlignment = Alignment.CenterHorizontally
  ) {
      Text("Clicks: $cuenta", fontSize = 32.sp)
      Spacer(Modifier.height(16.dp))
      Button(onClick = { cuenta++ }) { Text("¡Tócame!") }
      Button(onClick = { cuenta = 0 }) { Text("Reiniciar") }
  }

3. Corre en emulador o tu celu físico (USB + modo depuración)
4. Evoluciona: lista de tareas con LazyColumn { items(tareas) { } } + TextField para agregar

RECORDAR: en Compose NO llamas setText/vistas: describes UI = f(estado). Cambias 'cuenta' y Compose redibuja lo tocado. Si sabes React, ya lo entendiste.

ENTREGA: captura de la app corriendo + código en GitHub. Con Compose + Kotlin tienes el stack oficial moderno de Android lista para crecer (Room para BD, Retrofit para red).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace remember { mutableStateOf(0) }?
- A) Nada
- B) Estado que Compose observa: al cambiarlo, las funciones que lo leen se redibujan solas
- C) Guarda en disco
- D) Es un hilo
### 2. ¿Qué difiere Compose de los layouts XML clásicos?
- A) Nada crucial
- B) UI como código Kotlin declarativo (funciones + estado) en vez de XML + findViewById imperativo
- C) Es XML igual
- D) Es más lento

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Estado que Compose observa: al cambiarlo, las funciones que lo leen se redibujan solas — El equivalente a useState de React pero nativo Android: UI reactiva real.
**2.** ✅ UI como código Kotlin declarativo (funciones + estado) en vez de XML + findViewById imperativo — Menos glue code, mismo paradigma que React/Flutter: el futuro oficial de Android.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
