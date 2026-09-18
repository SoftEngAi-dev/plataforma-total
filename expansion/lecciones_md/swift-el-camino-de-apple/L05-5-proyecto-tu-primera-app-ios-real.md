# 5. Proyecto: tu primera app iOS real

> 📚 Curso: **Swift — El Camino de Apple** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```swift
CONSTRUYE: MINI-APP NOTAS EN SWIFTUI
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Xcode → New Project → iOS App → SwiftUI → nombre "Notas"
2. Modelo:
  struct Nota: Identifiable {                      // Identifiable para listas
      let id = UUID(); var titulo: String; var texto: String
  }
3. Vista principal:
  struct NotasView: View {
      @State private var notas: [Nota] = []
      @State private var nueva = ""
      var body: some View {
          NavigationStack {
              VStack {
                  HStack {
                      TextField("Nueva nota...", text: $nueva)   // $ = binding doble vía
                      Button("+") {
                          guard !nueva.isEmpty else { return }
                          notas.append(Nota(titulo: nueva, texto: ""))
                          nueva = ""
                      }
                  }.padding()
                  List {
                      ForEach(notas) { n in Text(n.titulo) }
                      .onDelete { idx in notas.remove(atOffsets: idx) }  // ¡swipe to delete gratis!
                  }
              }.navigationTitle("Mis notas")
          }
      }
  }
4. Corre el simulador (Cmd+R) — swipe + borrar + agregar funcionan.

$ BINDING: text: $nueva = doble vía automática (escribes en el TextField y el estado cambia al instante).
Persistencia después: UserDefaults para cosas chicas, SwiftData/SQLite para serio.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué significa text: $nueva en un TextField?
- A) Error
- B) Binding bidireccional: el campo edita el estado y el estado actualiza el campo
- C) Es privado
- D) Es async
### 2. ¿Para qué sirve Identifiable en el modelo de una lista?
- A) Decoración
- B) Cada item tiene id único para que SwiftUI rastree qué cambió en la lista (como key en React)
- C) Base de datos
- D) Nada

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Binding bidireccional: el campo edita el estado y el estado actualiza el campo — $variable crea un Binding: ida y vuelta automática entre UI y estado.
**2.** ✅ Cada item tiene id único para que SwiftUI rastree qué cambió en la lista (como key en React) — List/ForEach necesitan identidad estable: id = la key del mundo Apple.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
