# ⚡ Cheatsheet — 2. Ownership: el sistema que cambia tu cabeza

> Rust — Velocidad de C sin Miedo a los Crashes · Lección 2 · 18/09/2026

## 💡 Idea central
OWNERSHIP: LA REGLA DE ORO DE RUST

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué en Rust `let b = a` con Strings 'mueve' en vez de copiar?** → Ownership: solo un dueño por valor para liberar memoria automáticamente de forma segura _(Si dos dueños intentaran liberar → double-free. Un dueño ya lo sabes: sin GC, sin peligro.)_
- **¿Qué garantiza que no haya data races en concurrente Rust?** → Un solo &mut Sin & lectores, o muchos & pero ningún mut: exclusión mutua GARANTIZADA por el compilador _('Fearless concurrency': el type system TAN estricto hace im-posibles los race conditions clásicos.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
