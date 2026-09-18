# 📕 Resumen maestro — Rust — Velocidad de C sin Miedo a los Crashes

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Rust: el lenguaje querido 9 años seguidos
RUST: SIN GC, SIN SEGFAULTS, SEGURO DE MEMORIA EN COMPILACIÓN ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Rust compila tan rápido como C++ pero el COMPILADOR garantiza que no cuelgas punteros ni r…

## 2. 2. Ownership: el sistema que cambia tu cabeza
OWNERSHIP: LA REGLA DE ORO DE RUST ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Tres reglas (de las que TODO se deriva): 1. Cada valor tiene UN dueño (una variable) 2. Solo puede haber UN dueño a l…

## 3. 3. Result y Option: errores como parte del tipo
RESULT/OPTION: NULL Y EXCEPCIONES, PERO TIPADOS ━━━━━━━━━━━━━━━━━━━━━━━━━━━   // Result<T, E> en vez de excepciones; Option<T> en vez de null:   use std::fs;   fn leer() -> Result<…

## 4. 4. Structs, traits e iteradores: Rust en su salsa
MODELADO RÚSTICO ━━━━━━━━━━━━━━━━━━━━━━━━━━━ STRUCTS (tus datos)   #[derive(Debug, Clone)]                    // rasgos generados automagicamente   struct Tarea { titulo: String, h…

## 5. 5. Proyecto: CLI real en Rust con clap
CONSTRUYE: CLI DE NOTAS EN RUST ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1. cargo new notas && cd notas 2. Cargo.toml → [dependencies]: clap = { version = "4", features = ["derive"] } · serde/s…

---
✅ 5 lecciones · 📝 10 preguntas de repaso en quizzes_html/ · tests/