# 3. Estado con StatefulWidget y setState

> 📚 Curso: **Flutter — Apps Hermosas con Una Sola Base** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```dart
ESTADO: QUE LA APP REACCIONE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  class Contador extends StatefulWidget {
      const Contador({super.key});
      @override State<Contador> createState() => _ContadorState();
  }
  class _ContadorState extends State<Contador> {
      int cuenta = 0;
      @override
      Widget build(BuildContext context) {
          return Column(mainAxisAlignment: MainAxisAlignment.center, children: [
              Text("Clicks: $cuenta", style: TextStyle(fontSize: 32)),
              ElevatedButton(
                  onPressed: () {
                      setState(() { cuenta++; });   // setState avisa: "redibuja"
                  },
                  child: const Text("+1")),
          ]);
      }
  }

REGLA SUPREMA: mutar el valor NUNCA redibuja; SIEMPRE dentro de setState(...).
  cuenta++;            // ❌ UI no se entera
  setState(() => cuenta++);   // ✅ redibuja el widget

LISTENERS + ASYNC: pantalla típica = StatefulWidget + initState (corre 1 vez) donde inicias fetch/timers + dispose (limpias).

HOT RELOAD con setState: guardas y ves el cambio sin perder el estado. Desarrollar en Flutter es casi mágico por esto.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué dentro de setState(() { cuenta++; })?
- A) Por ritual
- B) setState marca el widget como sucio para que Flutter lo redibuje con el valor nuevo
- C) Evita null
- D) Es más rápido
### 2. ¿Dónde inicias un fetch o timer en un StatefulWidget?
- A) En build
- B) En initState (corre una vez al crearse); y liberas sus recursos en dispose
- C) En el constructor
- D) En main

---

## 🔑 Respuestas y explicaciones

**1.** ✅ setState marca el widget como sucio para que Flutter lo redibuje con el valor nuevo — Mutación sin setState = estado cambiado pero UI vieja: el bug de todo novato.
**2.** ✅ En initState (corre una vez al crearse); y liberas sus recursos en dispose — build se ejecuta muchas veces: inicialización va en initState, limpieza en dispose.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
