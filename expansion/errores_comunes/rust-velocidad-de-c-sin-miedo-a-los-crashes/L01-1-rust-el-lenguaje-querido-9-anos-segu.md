# ⚠️ Errores comunes — 1. Rust: el lenguaje querido 9 años seguidos

> Rust — Velocidad de C sin Miedo a los Crashes · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Todos mutables» → Frente a «¿Qué es diferente de los valores en Rust por defecto?» lo fácil es confundirse. **Verdad**: Inmutables por defecto; declaras mut explícitamente para cambiar valores. La inmutabilidad por defecto evita enormes clases de bugs en concurrencia.
- ❌ «Todos globales» → Frente a «¿Qué es diferente de los valores en Rust por defecto?» lo fácil es confundirse. **Verdad**: Inmutables por defecto; declaras mut explícitamente para cambiar valores. La inmutabilidad por defecto evita enormes clases de bugs en concurrencia.
- ❌ «Puerto mar» → Frente a «¿Qué es cargo en el ecosistema Rust?» lo fácil es confundirse. **Verdad**: El todo en uno: compilar, gestionar dependencias (crates), testear, documentar. cargo new/run/test/build: el mejor gestor de proyectos del mundo compilado.
- ❌ «Un VC» → Frente a «¿Qué es cargo en el ecosistema Rust?» lo fácil es confundirse. **Verdad**: El todo en uno: compilar, gestionar dependencias (crates), testear, documentar. cargo new/run/test/build: el mejor gestor de proyectos del mundo compilado.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
