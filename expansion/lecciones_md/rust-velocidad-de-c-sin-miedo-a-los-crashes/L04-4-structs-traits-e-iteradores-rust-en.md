# 4. Structs, traits e iteradores: Rust en su salsa

> 📚 Curso: **Rust — Velocidad de C sin Miedo a los Crashes** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```rust
MODELADO RÚSTICO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
STRUCTS (tus datos)
  #[derive(Debug, Clone)]                    // rasgos generados automagicamente
  struct Tarea { titulo: String, hecha: bool }

IMPL (los métodos del struct)
  impl Tarea {
      fn nueva(titulo: &str) -> Self {                 // constructor convencional
          Tarea { titulo: titulo.to_string(), hecha: false }
      }
      fn completar(&mut self) { self.hecha = true; }   // muta: requiere instancia mut
  }

TRAITS (interfaces compartidas: el polimorfismo de Rust)
  trait Saludable { fn saludar(&self) -> String; }
  impl Saludable for Tarea { fn saludar(&self) -> String { format!("Soy {}!", self.titulo) } }
  // genéricos con trait bounds: fn imprimir<T: Saludable>(x: &T) → cero overhead

ITERADORES puros: encadena sin loops manuales, cero coste:
  let numeros = vec![1, 2, 3, 4, 5];
  let resultado: Vec<i32> = numeros.iter().filter(|n| *n % 2 == 0).map(|n| n * 10).collect();
  let suma: i32 = numeros.iter().sum();
```

---

## 📝 Quiz de la lección

### 1. ¿Qué son los traits de Rust?
- A) Clases normales
- B) Interfaces de comportamiento (comparable a interfaces Java/protocols) implementables por cualquier tipo — aún nativos predefinidos
- C) Macros
- D) Bases de datos
### 2. ¿Qué coste extra tienen los iteradores encadenados de Rust?
- A) Mucho (boxed)
- B) Cero: se compilan al mismo código que un bucle for manual (zero-cost abstractions)
- C) Algo en runtime
- D) Lentísimos

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Interfaces de comportamiento (comparable a interfaces Java/protocols) implementables por cualquier tipo — aún nativos predefinidos — derive(Debug) o impl Trait for MiStruct: comportamiento compartido sin herencia tradicional.
**2.** ✅ Cero: se compilan al mismo código que un bucle for manual (zero-cost abstractions) — 'What you don't use, you don't pay for; what you do, you couldn't hand-code better' = lema.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
