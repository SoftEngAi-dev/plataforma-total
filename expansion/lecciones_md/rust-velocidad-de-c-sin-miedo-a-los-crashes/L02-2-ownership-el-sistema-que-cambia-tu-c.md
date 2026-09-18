# 2. Ownership: el sistema que cambia tu cabeza

> 📚 Curso: **Rust — Velocidad de C sin Miedo a los Crashes** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```rust
OWNERSHIP: LA REGLA DE ORO DE RUST
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tres reglas (de las que TODO se deriva):
1. Cada valor tiene UN dueño (una variable)
2. Solo puede haber UN dueño a la vez (al moverse, el anterior lo pierde)
3. Cuando el dueño sale de scope → valor liberado automáticamente (¡sin GC!)

  let a = String::from("hola");
  let b = a;              // MOVIDO: 'a' YA NO VALE (¡se 'movió' la propiedad!)
  // println!("{}", a);  // ❌ error de compilación: 'value used after move'
  println!("{}", b);      // ✅

  let r = &b;             // & = pedir prestado (lea, no mueve): puedo tener mil & lectores
  let w = &mut b_mut;     // &mut = prestar PARA ESCRIBIR: solo UNO a la vez (y sin lectores activos)

POR QUÉ IMPORTA: el compilador rechaza data races, use-after-free y double-free en COMPILACIÓN, no en producción. La memoria se libera sin garbage collector ni free manual.

.clone() copia de verdad cuando necesitas dos dueños. Strings con String (mutable en heap), &str vista/prestada (lo eficiente).
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué en Rust `let b = a` con Strings 'mueve' en vez de copiar?
- A) Es bug
- B) Ownership: solo un dueño por valor para liberar memoria automáticamente de forma segura
- C) Es C puro
- D) Para velocidad del IDE
### 2. ¿Qué garantiza que no haya data races en concurrente Rust?
- A) Suerte
- B) Un solo &mut Sin & lectores, o muchos & pero ningún mut: exclusión mutua GARANTIZADA por el compilador
- C) Threads especiales
- D) Locks manuales

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Ownership: solo un dueño por valor para liberar memoria automáticamente de forma segura — Si dos dueños intentaran liberar → double-free. Un dueño ya lo sabes: sin GC, sin peligro.
**2.** ✅ Un solo &mut Sin & lectores, o muchos & pero ningún mut: exclusión mutua GARANTIZADA por el compilador — 'Fearless concurrency': el type system TAN estricto hace im-posibles los race conditions clásicos.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
