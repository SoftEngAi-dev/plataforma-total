# ⚠️ Errores comunes — 5. Proyecto: CLI real en Rust con clap

> Rust — Velocidad de C sin Miedo a los Crashes · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué hace clap con macros derive?» lo fácil es confundirse. **Verdad**: Genera el parser de argumentos/ayuda de tu CLI desde tus structs automáticamente (--help profesional gratis). Derive: Rust's compile-time code generation — CLI args tipados de regalo.
- ❌ «Compila Rust» → Frente a «¿Qué hace clap con macros derive?» lo fácil es confundirse. **Verdad**: Genera el parser de argumentos/ayuda de tu CLI desde tus structs automáticamente (--help profesional gratis). Derive: Rust's compile-time code generation — CLI args tipados de regalo.
- ❌ «Null» → Frente a «¿Qué desafío famoso te hará 'sentir' ownership en este proyecto?» lo fácil es confundirse. **Verdad**: Elegir entre String (dueña) y &str (prestada) en structs/funcs: la decisión de propiedad explícita. Las peleas con el borrow checker te enseñan el modelo: un mes después, es superpoder.
- ❌ «Threads» → Frente a «¿Qué desafío famoso te hará 'sentir' ownership en este proyecto?» lo fácil es confundirse. **Verdad**: Elegir entre String (dueña) y &str (prestada) en structs/funcs: la decisión de propiedad explícita. Las peleas con el borrow checker te enseñan el modelo: un mes después, es superpoder.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
