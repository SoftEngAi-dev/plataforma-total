# ⚠️ Errores comunes — 1. C#: lenguaje que ya no es 'de Windows'

> C# y .NET — El Ecosistema Microsoft Moderno · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué hace el $ antes de una cadena en C#?» lo fácil es confundirse. **Verdad**: Habilita interpolación: $"{variable}" inserta valores. $"{nombre}" es la f-string/template literal de C#.
- ❌ «Es regex» → Frente a «¿Qué hace el $ antes de una cadena en C#?» lo fácil es confundirse. **Verdad**: Habilita interpolación: $"{variable}" inserta valores. $"{nombre}" es la f-string/template literal de C#.
- ❌ «SQL puro» → Frente a «LINQ Where(...).Select(...) equivale a...» lo fácil es confundirse. **Verdad**: filter + map encadenados sobre colecciones, tipo JS/Python. LINQ es funcional sobre colecciones: es una de las mayores comodidades de C#.
- ❌ «loops for» → Frente a «LINQ Where(...).Select(...) equivale a...» lo fácil es confundirse. **Verdad**: filter + map encadenados sobre colecciones, tipo JS/Python. LINQ es funcional sobre colecciones: es una de las mayores comodidades de C#.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
