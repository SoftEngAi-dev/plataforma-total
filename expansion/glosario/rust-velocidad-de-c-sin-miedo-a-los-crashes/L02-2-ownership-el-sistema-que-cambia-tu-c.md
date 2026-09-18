# 📖 Glosario — 2. Ownership: el sistema que cambia tu cabeza

> Rust — Velocidad de C sin Miedo a los Crashes · Lección 2 · Términos que debes poder definir sin mirar

- **Ownership: solo un dueño por valor para liberar memoria automáticamente de forma segura** — Si dos dueños intentaran liberar → double-free. Un dueño ya lo sabes: sin GC, sin peligro.
- **Un solo &mut Sin & lectores, o muchos & pero ningún mut: exclusión mutua GARANTIZADA por el compilador** — 'Fearless concurrency': el type system TAN estricto hace im-posibles los race conditions clásicos.

✍️ Ejercicio: añade debajo TU propia definición de cada término.
