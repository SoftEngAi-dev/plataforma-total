# ⚠️ Errores comunes — 4. Genéricos: reusabilidad con seguridad

> TypeScript — JavaScript con Superpoderes y Seguridad · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué gana identidad<T>(v: T): T respecto a misto?: any?» lo fácil es confundirse. **Verdad**: Recuerda el tipo exacto de entrada y lo devuelve: autocomplete y chequeo completos. Los genéricos modelan RELACIONES entre tipos — any solo las borra.
- ❌ «Es más rápido» → Frente a «¿Qué gana identidad<T>(v: T): T respecto a misto?: any?» lo fácil es confundirse. **Verdad**: Recuerda el tipo exacto de entrada y lo devuelve: autocomplete y chequeo completos. Los genéricos modelan RELACIONES entre tipos — any solo las borra.
- ❌ «Crea una clase T» → Frente a «¿Qué hace <T extends { length: number }>?» lo fácil es confundirse. **Verdad**: Restringe T a tipos que tengan la propiedad length. Constraint: puedo usar .length sabiendo que el compilador lo garantiza.
- ❌ «Hace T opcional» → Frente a «¿Qué hace <T extends { length: number }>?» lo fácil es confundirse. **Verdad**: Restringe T a tipos que tengan la propiedad length. Constraint: puedo usar .length sabiendo que el compilador lo garantiza.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
