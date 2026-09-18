# 5. Proyecto: CLI real en Rust con clap

> 📚 Curso: **Rust — Velocidad de C sin Miedo a los Crashes** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```rust
CONSTRUYE: CLI DE NOTAS EN RUST
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. cargo new notas && cd notas
2. Cargo.toml → [dependencies]: clap = { version = "4", features = ["derive"] } · serde/serde_json (parse/serializa JSON)
   cargo add clap --features derive serde serde_json
3. Estructura: main.rs CLI con clap:
   #[derive(clap::Parser)] struct Args { #[command(subcommand)] cmd: Cmd }
   #[derive(clap::Subcommand)] enum Cmd { Agregar { titulo: String }, Lista, Borrar { id: usize } }
4. notas.rs: struct Nota + Vec<Nota> guardado en notas.json (serde_json + fs write/read)
   → practicarás: Result, ? , Option, ownership con Strings
5. Matching el comando, cargas, mutas, guardas. fuzz con clap: notas agregar "Estudiar Rust" → agrega
6. cargo test para funciones internas (tests al lado del código: #[test] fn ...{})
7. cargo build --release → target/release/notas → ¡tu binario final nativo para portar/entregar!

CON LO QUE ENFRENTÁS de verdad: lifetimes básicos (peleas del novato: hence String vs &str decisiones), Result serializable, CLI parse profesional. Próximo área: async con tokio, tu primer servicio web rápido.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace clap con macros derive?
- A) Nada
- B) Genera el parser de argumentos/ayuda de tu CLI desde tus structs automáticamente (--help profesional gratis)
- C) Compila Rust
- D) Instala crates
### 2. ¿Qué desafío famoso te hará 'sentir' ownership en este proyecto?
- A) Null
- B) Elegir entre String (dueña) y &str (prestada) en structs/funcs: la decisión de propiedad explícita
- C) Threads
- D) Red

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Genera el parser de argumentos/ayuda de tu CLI desde tus structs automáticamente (--help profesional gratis) — Derive: Rust's compile-time code generation — CLI args tipados de regalo.
**2.** ✅ Elegir entre String (dueña) y &str (prestada) en structs/funcs: la decisión de propiedad explícita — Las peleas con el borrow checker te enseñan el modelo: un mes después, es superpoder.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
