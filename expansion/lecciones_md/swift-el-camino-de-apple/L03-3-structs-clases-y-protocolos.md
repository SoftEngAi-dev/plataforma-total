# 3. Structs, clases y protocolos

> 📚 Curso: **Swift — El Camino de Apple** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```swift
EL TRIDENTE DEL MODELADO SWIFT
━━━━━━━━━━━━━━━━━━━━━━━━━━━
STRUCT (valor, copia — usarás ESTO por defecto)
  struct Punto { var x: Int; var y: Int }
  var p = Punto(x: 1, y: 2)
  p.x = 10                             // mutar ok (p es var)
  // init miembro a miembro es GRATIS

CLASS (referencia, herencia — para identidad/estado compartido)
  class Tarea {
      var titulo: String
      var hecha = false
      init(titulo: String) { self.titulo = titulo }   // init explícito
      func completar() { hecha = true }
  }

STRUCT vs CLASS (el SANO default Apple): struct por valor → copias seguras sin aliasing accidental.
class cuando necesites referencia compartida o herencia.

PROTOCOLOS (el interface de Swift — mucho más potente que herencia):
  protocol Describible { var descripcion: String { get } }
  extension Tarea: Describible {
      var descripcion: String { "Tarea: \(titulo)\(hecha ? " ✅" : "")" }
  }
  func imprimir(_ cosa: Describible) { print(cosa.descripcion) }

EXTENSIONS: agregas métodos a tipos EXISTENTES sin herencia:
  extension Int { var doble: Int { self * 2 } }   // 5.doble → 10
```

---

## 📝 Quiz de la lección

### 1. ¿Qué diferencia struct de class en Swift?
- A) Son iguales
- B) struct = tipo VALOR (se copia); class = tipo REFERENCIA (se comparte) con herencia
- C) class es gratis
- D) struct es lenta
### 2. ¿Qué permite una extension?
- A) Herencia múltiple
- B) Agregar funcionalidad a tipos existentes sin subclases: incluso a Int, String nativos
- C) Nada especial
- D) Async

---

## 🔑 Respuestas y explicaciones

**1.** ✅ struct = tipo VALOR (se copia); class = tipo REFERENCIA (se comparte) con herencia — Structs por defecto = menos bugs de aliasing; class solo para identidad compartida.
**2.** ✅ Agregar funcionalidad a tipos existentes sin subclases: incluso a Int, String nativos — Las extensiones hacen Swift extensible al infinito y súper idiomático.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
