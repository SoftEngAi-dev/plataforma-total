# ⚠️ Errores comunes — 4. SwiftUI: la UI declarativa de Apple

> Swift — El Camino de Apple · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Nada especial» → Frente a «¿Qué hace @State en SwiftUI?» lo fácil es confundirse. **Verdad**: Marca estado local que al cambiar provoca re-render automático del view que lo usa. @State = useState de React: mutás y la UI se actualiza sola.
- ❌ «Guarda en disco» → Frente a «¿Qué hace @State en SwiftUI?» lo fácil es confundirse. **Verdad**: Marca estado local que al cambiar provoca re-render automático del view que lo usa. @State = useState de React: mutás y la UI se actualiza sola.
- ❌ «Un import» → Frente a «¿Qué es '.padding()' al final del VStack?» lo fácil es confundirse. **Verdad**: Un modifier: transforma la vista y devuelve una nueva (estilo encadenado). Los modifiers se apilan de afuera hacia dentro: declarativos y componibles.
- ❌ «Un error» → Frente a «¿Qué es '.padding()' al final del VStack?» lo fácil es confundirse. **Verdad**: Un modifier: transforma la vista y devuelve una nueva (estilo encadenado). Los modifiers se apilan de afuera hacia dentro: declarativos y componibles.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
