# ⚠️ Errores comunes — 11. Objetos: diccionarios con superpoderes

> JavaScript — De Cero a Experto · Lección 11 · Aprender de los errores (propios y ajenos)

- ❌ «Borra nombre del objeto» → Frente a «¿Qué hace const { nombre } = alumno?» lo fácil es confundirse. **Verdad**: Extrae alumno.nombre en una variable llamada nombre (destructuring). Destructuring: la forma idiomática de extraer propiedades en JS moderno.
- ❌ «Crea un objeto» → Frente a «¿Qué hace const { nombre } = alumno?» lo fácil es confundirse. **Verdad**: Extrae alumno.nombre en una variable llamada nombre (destructuring). Destructuring: la forma idiomática de extraer propiedades en JS moderno.
- ❌ «Nunca, es obsoleto» → Frente a «¿Cuándo usar alumno["nombre"] en vez de alumno.nombre?» lo fácil es confundirse. **Verdad**: Cuando la clave viene de una variable o tiene espacios. Los corchetes aceptan expresiones: alumno[variable] resuelve la clave dinámicamente.
- ❌ «Es más rápido» → Frente a «¿Cuándo usar alumno["nombre"] en vez de alumno.nombre?» lo fácil es confundirse. **Verdad**: Cuando la clave viene de una variable o tiene espacios. Los corchetes aceptan expresiones: alumno[variable] resuelve la clave dinámicamente.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
