# 1. Swift: elegancia tipada de Apple

> 📚 Curso: **Swift — El Camino de Apple** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```swift
SWIFT: MODERNO, SEGURO Y VELOZ
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lenguaje de Apple desde 2014 (reemplazando Objective-C). Abierto, compilado, leéble como Python pero con tipos estrictos y safety.

  let nombre = "Ada"               // let = constante (inmutable)
  var edad = 36                    // var = variable
  print("Hola, \(nombre)!")        // interpolación: \(expr)
  edad += 1

  let frutas = ["🍎", "🍌"]           // Array literal, tipo inferido [String]
  var precios: [String: Int] = ["café": 120]   // Dictionary
  precios["té"] = 80
  for (fruta) in frutas { print(fruta) }
  for (producto, precio) in precios { print("\(producto): $\(precio)") }

  func area(base: Int, altura: Int) -> Int {   // -> Tipo de retorno
      base * altura                            // return implícito si es 1 expresión
  }
  print(area(base: 5, altura: 3))               // argument labels: lee claro

NUMEROS: Int, Double (decimales), Float. Bool. String.
EJECUTAR: en Xcode (Playground es mágico para aprender) o `swift hola.swift` en terminal.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué distingue let de var en Swift?
- A) Nada
- B) let = constante inmutable; var = reasignable — igual que val/var de Kotlin
- C) let es para números
- D) var es privado
### 2. ¿Cómo interpola strings Swift?
- A) ${x}
- B) \(x) dentro del string
- C) f""
- D) %s

---

## 🔑 Respuestas y explicaciones

**1.** ✅ let = constante inmutable; var = reasignable — igual que val/var de Kotlin — Swift te empuja a let por defecto: mutación solo cuando la justificas.
**2.** ✅ \(x) dentro del string — "Hola \(nombre)" — la interpolación nativa de Swift.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
