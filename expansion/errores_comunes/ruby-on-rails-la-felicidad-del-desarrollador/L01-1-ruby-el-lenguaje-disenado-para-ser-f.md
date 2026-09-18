# ⚠️ Errores comunes — 1. Ruby: el lenguaje diseñado para ser feliz

> Ruby on Rails — La Felicidad del Desarrollador · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «${}» → Frente a «¿Cómo interpola cadenas Ruby?» lo fácil es confundirse. **Verdad**: "#{variable}" dentro de comillas dobles. #{} solo en comillas dobles — distinción que bugs de novato llenan.
- ❌ «f''» → Frente a «¿Cómo interpola cadenas Ruby?» lo fácil es confundirse. **Verdad**: "#{variable}" dentro de comillas dobles. #{} solo en comillas dobles — distinción que bugs de novato llenan.
- ❌ «nil siempre» → Frente a «¿Qué devuelve un método Ruby sin return?» lo fácil es confundirse. **Verdad**: La última expresión evaluada (return implícito). "Lo último se devuelve" — por eso casi no verás return en Ruby idiomático.
- ❌ «Error» → Frente a «¿Qué devuelve un método Ruby sin return?» lo fácil es confundirse. **Verdad**: La última expresión evaluada (return implícito). "Lo último se devuelve" — por eso casi no verás return en Ruby idiomático.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
