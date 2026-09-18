# 📕 Resumen maestro — Swift — El Camino de Apple

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Swift: elegancia tipada de Apple
SWIFT: MODERNO, SEGURO Y VELOZ ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Lenguaje de Apple desde 2014 (reemplazando Objective-C). Abierto, compilado, leéble como Python pero con tipos estrictos …

## 2. 2. Optionals: adiós al error del billón de dólares
OPTIONALS: NULL-SAFETY EN EL ADN ━━━━━━━━━━━━━━━━━━━━━━━━━━━ En Swift un valor SÍ puede faltar, pero el tipo te obliga a encararlo:   var apodo: String? = nil            // String?…

## 3. 3. Structs, clases y protocolos
EL TRIDENTE DEL MODELADO SWIFT ━━━━━━━━━━━━━━━━━━━━━━━━━━━ STRUCT (valor, copia — usarás ESTO por defecto)   struct Punto { var x: Int; var y: Int }   var p = Punto(x: 1, y: 2)   p…

## 4. 4. SwiftUI: la UI declarativa de Apple
SWIFTUI: UI = FUNCIÓN DEL ESTADO (¡otra vez!) ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Desde 2019, la forma moderna: describís la UI y SwiftUI la redibuja al cambiar el estado.    import SwiftU…

## 5. 5. Proyecto: tu primera app iOS real
CONSTRUYE: MINI-APP NOTAS EN SWIFTUI ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1. Xcode → New Project → iOS App → SwiftUI → nombre "Notas" 2. Modelo:   struct Nota: Identifiable {               …

---
✅ 5 lecciones · 📝 10 preguntas de repaso en quizzes_html/ · tests/