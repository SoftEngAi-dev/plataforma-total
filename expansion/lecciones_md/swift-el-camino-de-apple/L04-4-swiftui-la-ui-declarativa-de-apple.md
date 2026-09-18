# 4. SwiftUI: la UI declarativa de Apple

> 📚 Curso: **Swift — El Camino de Apple** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```swift
SWIFTUI: UI = FUNCIÓN DEL ESTADO (¡otra vez!)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Desde 2019, la forma moderna: describís la UI y SwiftUI la redibuja al cambiar el estado.

  import SwiftUI
  struct ContadorView: View {
      @State private var cuenta = 0                 // ESTADO local (la fuente de verdad)

      var body: some View {                         // TODO view devuelve 'some View'
          VStack(spacing: 16) {                     // apila vertical (HStack horizontal)
              Text("Clicks: \(cuenta)")
                  .font(.largeTitle)
              Button("¡Tócame!") { cuenta += 1 }    // acción con closure
              HStack {
                  Button("Reiniciar") { cuenta = 0 }
                  Button("-1") { cuenta -= 1 }
              }
          }
          .padding()
      }
  }

CONCEPTOS CLAVE
• View protocol: todo componente es una struct con 'var body'
• @State: estado local — cambia y SwiftUI redibuja automático (como useState)
• @Binding: estado que viene del padre; @StateObject/@Observable para modelos
• Modifiers encadenados: .font().padding().foregroundColor() — el estilo en cadena
• Preview gratis en Xcode mientras editás (hot reload real)

LISTAS:
  List(items) { item in Text(item.nombre) }  // como FlatList/LazyColumn/React map
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace @State en SwiftUI?
- A) Nada especial
- B) Marca estado local que al cambiar provoca re-render automático del view que lo usa
- C) Guarda en disco
- D) Es async
### 2. ¿Qué es '.padding()' al final del VStack?
- A) Un import
- B) Un modifier: transforma la vista y devuelve una nueva (estilo encadenado)
- C) Un error
- D) Un bucle

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Marca estado local que al cambiar provoca re-render automático del view que lo usa — @State = useState de React: mutás y la UI se actualiza sola.
**2.** ✅ Un modifier: transforma la vista y devuelve una nueva (estilo encadenado) — Los modifiers se apilan de afuera hacia dentro: declarativos y componibles.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
