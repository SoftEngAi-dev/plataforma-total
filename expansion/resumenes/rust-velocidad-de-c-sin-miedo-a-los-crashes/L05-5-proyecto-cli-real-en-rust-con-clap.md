# ⚡ Cheatsheet — 5. Proyecto: CLI real en Rust con clap

> Rust — Velocidad de C sin Miedo a los Crashes · Lección 5 · 18/09/2026

## 💡 Idea central
CONSTRUYE: CLI DE NOTAS EN RUST

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué hace clap con macros derive?** → Genera el parser de argumentos/ayuda de tu CLI desde tus structs automáticamente (--help profesional gratis) _(Derive: Rust's compile-time code generation — CLI args tipados de regalo.)_
- **¿Qué desafío famoso te hará 'sentir' ownership en este proyecto?** → Elegir entre String (dueña) y &str (prestada) en structs/funcs: la decisión de propiedad explícita _(Las peleas con el borrow checker te enseñan el modelo: un mes después, es superpoder.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
