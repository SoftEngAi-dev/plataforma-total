# ⚠️ Errores comunes — 3. C++: C más objetos y la STL (los superpoderes)

> C y C++ — Los Cimientos del Software Moderno · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué aporta vector<T> de la STL respecto a arrays C?» lo fácil es confundirse. **Verdad**: Array dinámico gestionado: crece solo, sabe su tamaño, sin malloc/free manual. vector + string + sort + map = la STL: productividad C++, sin pelear malloc manual.
- ❌ «Es de Java» → Frente a «¿Qué aporta vector<T> de la STL respecto a arrays C?» lo fácil es confundirse. **Verdad**: Array dinámico gestionado: crece solo, sabe su tamaño, sin malloc/free manual. vector + string + sort + map = la STL: productividad C++, sin pelear malloc manual.
- ❌ «Un error» → Frente a «¿Qué es RAII en C++?» lo fácil es confundirse. **Verdad**: Adquisición/liberación de recursos ligada al ciclo de vida de objetos: scope-ended = recurso liberado (origen del modelo que perfecciona Rust). Destructor al salir del bloque: no olvidas liberar; es la contra a los leaks/locks olvidados.
- ❌ «Una clase» → Frente a «¿Qué es RAII en C++?» lo fácil es confundirse. **Verdad**: Adquisición/liberación de recursos ligada al ciclo de vida de objetos: scope-ended = recurso liberado (origen del modelo que perfecciona Rust). Destructor al salir del bloque: no olvidas liberar; es la contra a los leaks/locks olvidados.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
