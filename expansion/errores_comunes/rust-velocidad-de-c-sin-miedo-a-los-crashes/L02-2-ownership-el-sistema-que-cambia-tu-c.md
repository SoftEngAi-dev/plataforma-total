# ⚠️ Errores comunes — 2. Ownership: el sistema que cambia tu cabeza

> Rust — Velocidad de C sin Miedo a los Crashes · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Es bug» → Frente a «¿Por qué en Rust `let b = a` con Strings 'mueve' en vez de copiar?» lo fácil es confundirse. **Verdad**: Ownership: solo un dueño por valor para liberar memoria automáticamente de forma segura. Si dos dueños intentaran liberar → double-free. Un dueño ya lo sabes: sin GC, sin peligro.
- ❌ «Es C puro» → Frente a «¿Por qué en Rust `let b = a` con Strings 'mueve' en vez de copiar?» lo fácil es confundirse. **Verdad**: Ownership: solo un dueño por valor para liberar memoria automáticamente de forma segura. Si dos dueños intentaran liberar → double-free. Un dueño ya lo sabes: sin GC, sin peligro.
- ❌ «Suerte» → Frente a «¿Qué garantiza que no haya data races en concurrente Rust?» lo fácil es confundirse. **Verdad**: Un solo &mut Sin & lectores, o muchos & pero ningún mut: exclusión mutua GARANTIZADA por el compilador. 'Fearless concurrency': el type system TAN estricto hace im-posibles los race conditions clásicos.
- ❌ «Threads especiales» → Frente a «¿Qué garantiza que no haya data races en concurrente Rust?» lo fácil es confundirse. **Verdad**: Un solo &mut Sin & lectores, o muchos & pero ningún mut: exclusión mutua GARANTIZADA por el compilador. 'Fearless concurrency': el type system TAN estricto hace im-posibles los race conditions clásicos.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
