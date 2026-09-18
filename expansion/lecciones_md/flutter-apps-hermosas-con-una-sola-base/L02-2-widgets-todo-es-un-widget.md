# 2. Widgets: TODO es un widget

> 📚 Curso: **Flutter — Apps Hermosas con Una Sola Base** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```dart
WIDGETS: LOS LEGO DE FLUTTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━
En Flutterabsolutamente TODO es un widget: botones, textos, paddings, hasta la app entera.

  import 'package:flutter/material.dart';
  void main() => runApp(const MiApp());

  class MiApp extends StatelessWidget {          // Stateless: no cambia por sí mismo
      const MiApp({super.key});
      @override
      Widget build(BuildContext context) {        // build = qué dibujar
          return MaterialApp(
              home: Scaffold(                     // página base con appbar/body
                  appBar: AppBar(title: const Text("Mi app")),
                  body: const Center(child: Text("¡Hola, Flutter!")),
                  floatingActionButton: FloatingActionButton(
                      onPressed: () {}, child: const Icon(Icons.add)),
              ),
          );
      }
  }

LOS 8 QUE COMEN TODO
Text · ElevatedButton · Column/Row (apilar) · Padding · Center · Container (caja con estilo) · Icon · Image

COMPOSE-AND-NEST: no configs ocultas: anidas widgets como bloques. Column(children: [...widgets]).
stateless (inmutable) vs stateful (tiene estado y setState) — la próxima lección.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es un StatelessWidget?
- A) Un error
- B) Un widget sin estado propio: se dibuja igual salvo que su PADRE le pase datos nuevos
- C) Un widget con tabs
- D) Un archivo
### 2. ¿Qué hace Column(children: [...])?
- A) Tabla
- B) Apila widgets verticalmente (Row es horizontal)
- C) CSV
- D) Nada

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Un widget sin estado propio: se dibuja igual salvo que su PADRE le pase datos nuevos — La mayoría de la UI: describe, no cambia. Lo con estado es StatefulWidget.
**2.** ✅ Apila widgets verticalmente (Row es horizontal) — Layouts de una dimensión; con Expanded/flex dentro controlas el reparto.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
