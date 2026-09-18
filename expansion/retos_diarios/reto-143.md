# 🥊 Reto del día 143

> Hoy tu cerebro ataca: **2. Ownership: el sistema que cambia tu cabeza** (Rust — Velocidad de C sin Miedo a los Crashes)

1. Explica en voz alta este tema durante 2 minutos, sin notas.
2. Relee la lección solo si el paso 1 trabó.
3. Reescribe desde cero el ejemplo clave de la lección.

## 🥊 Desafío exprés (sin mirar)
**¿Por qué en Rust `let b = a` con Strings 'mueve' en vez de copiar?**

<details><summary>👁 Ver respuesta</summary>

✅ Ownership: solo un dueño por valor para liberar memoria automáticamente de forma segura — Si dos dueños intentaran liberar → double-free. Un dueño ya lo sabes: sin GC, sin peligro.
</details>

💰 Vale 1 punto de maestría. Acumula 30 → date un premio real.
