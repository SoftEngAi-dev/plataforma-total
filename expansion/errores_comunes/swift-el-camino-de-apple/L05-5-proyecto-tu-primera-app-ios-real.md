# ⚠️ Errores comunes — 5. Proyecto: tu primera app iOS real

> Swift — El Camino de Apple · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Error» → Frente a «¿Qué significa text: $nueva en un TextField?» lo fácil es confundirse. **Verdad**: Binding bidireccional: el campo edita el estado y el estado actualiza el campo. $variable crea un Binding: ida y vuelta automática entre UI y estado.
- ❌ «Es privado» → Frente a «¿Qué significa text: $nueva en un TextField?» lo fácil es confundirse. **Verdad**: Binding bidireccional: el campo edita el estado y el estado actualiza el campo. $variable crea un Binding: ida y vuelta automática entre UI y estado.
- ❌ «Decoración» → Frente a «¿Para qué sirve Identifiable en el modelo de una lista?» lo fácil es confundirse. **Verdad**: Cada item tiene id único para que SwiftUI rastree qué cambió en la lista (como key en React). List/ForEach necesitan identidad estable: id = la key del mundo Apple.
- ❌ «Base de datos» → Frente a «¿Para qué sirve Identifiable en el modelo de una lista?» lo fácil es confundirse. **Verdad**: Cada item tiene id único para que SwiftUI rastree qué cambió en la lista (como key en React). List/ForEach necesitan identidad estable: id = la key del mundo Apple.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
