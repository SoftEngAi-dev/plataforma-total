# ⚠️ Errores comunes — 4. Structs, traits e iteradores: Rust en su salsa

> Rust — Velocidad de C sin Miedo a los Crashes · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Clases normales» → Frente a «¿Qué son los traits de Rust?» lo fácil es confundirse. **Verdad**: Interfaces de comportamiento (comparable a interfaces Java/protocols) implementables por cualquier tipo — aún nativos predefinidos. derive(Debug) o impl Trait for MiStruct: comportamiento compartido sin herencia tradicional.
- ❌ «Macros» → Frente a «¿Qué son los traits de Rust?» lo fácil es confundirse. **Verdad**: Interfaces de comportamiento (comparable a interfaces Java/protocols) implementables por cualquier tipo — aún nativos predefinidos. derive(Debug) o impl Trait for MiStruct: comportamiento compartido sin herencia tradicional.
- ❌ «Mucho (boxed)» → Frente a «¿Qué coste extra tienen los iteradores encadenados de Rust?» lo fácil es confundirse. **Verdad**: Cero: se compilan al mismo código que un bucle for manual (zero-cost abstractions). 'What you don't use, you don't pay for; what you do, you couldn't hand-code better' = lema.
- ❌ «Algo en runtime» → Frente a «¿Qué coste extra tienen los iteradores encadenados de Rust?» lo fácil es confundirse. **Verdad**: Cero: se compilan al mismo código que un bucle for manual (zero-cost abstractions). 'What you don't use, you don't pay for; what you do, you couldn't hand-code better' = lema.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
