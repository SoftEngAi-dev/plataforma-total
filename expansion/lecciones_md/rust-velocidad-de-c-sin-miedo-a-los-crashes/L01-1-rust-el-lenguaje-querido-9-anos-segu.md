# 1. Rust: el lenguaje querido 9 años seguidos

> 📚 Curso: **Rust — Velocidad de C sin Miedo a los Crashes** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```rust
RUST: SIN GC, SIN SEGFAULTS, SEGURO DE MEMORIA EN COMPILACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Rust compila tan rápido como C++ pero el COMPILADOR garantiza que no cuelgas punteros ni rompes memoria (sin garbage collector encima). Por eso: #1 'most loved' de StackOverflow 8+ años.

  // main.rs
  fn main() {
      let nombre = "Ada";                        // inmutable POR DEFECTO (inmutabilidad manda)
      let mut edad = 36;                         // mutable requiere mut explícito
      edad += 1;
      println!("{} tiene {} años", nombre, edad);

      let frutas = vec!["manzana", "pera"];       // Vec<T>: array dinámico
      for f in &frutas { println!("{}", f); }     // & = BY REFERENCIA (¡el corazón!)

      fn area(b: i32, h: i32) -> i32 { b * h }    // -> tipo de retorno, return implícito sin ;
  }

INSTALACIÓN: rustup (rustup.rs) → cargo (el gestor TODO: build+deps+test)
  cargo new miapp && cd miapp && cargo run    ← el flujo feliz

cargotest integrado; docs automáticas: cargo doc --open
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es diferente de los valores en Rust por defecto?
- A) Todos mutables
- B) Inmutables por defecto; declaras mut explícitamente para cambiar valores
- C) Todos globales
- D) Todos públicos
### 2. ¿Qué es cargo en el ecosistema Rust?
- A) Puerto mar
- B) El todo en uno: compilar, gestionar dependencias (crates), testear, documentar
- C) Un VC
- D) Solo build

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Inmutables por defecto; declaras mut explícitamente para cambiar valores — La inmutabilidad por defecto evita enormes clases de bugs en concurrencia.
**2.** ✅ El todo en uno: compilar, gestionar dependencias (crates), testear, documentar — cargo new/run/test/build: el mejor gestor de proyectos del mundo compilado.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
