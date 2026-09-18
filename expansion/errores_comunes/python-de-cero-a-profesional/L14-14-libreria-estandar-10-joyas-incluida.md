# ⚠️ Errores comunes — 14. Librería estándar: 10 joyas incluidas

> Python — De Cero a Profesional · Lección 14 · Aprender de los errores (propios y ajenos)

- ❌ «Solo estética» → Frente a «¿Qué aporta Path de pathlib frente a strings de rutas?» lo fácil es confundirse. **Verdad**: Rutas portables Windows/Linux con operadores / y métodos read_text/exists. p = Path.home() / 'x' funciona igual en todos los SO — el estándar moderno de Python.
- ❌ «Velocidad» → Frente a «¿Qué aporta Path de pathlib frente a strings de rutas?» lo fácil es confundirse. **Verdad**: Rutas portables Windows/Linux con operadores / y métodos read_text/exists. p = Path.home() / 'x' funciona igual en todos los SO — el estándar moderno de Python.
- ❌ «Una lista» → Frente a «Counter('banana') devuelve...» lo fácil es confundirse. **Verdad**: {'a': 3, 'n': 2, 'b': 1} — conteo automático. collections.Counter = histograma listo con una línea.
- ❌ «'bn'» → Frente a «Counter('banana') devuelve...» lo fácil es confundirse. **Verdad**: {'a': 3, 'n': 2, 'b': 1} — conteo automático. collections.Counter = histograma listo con una línea.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
