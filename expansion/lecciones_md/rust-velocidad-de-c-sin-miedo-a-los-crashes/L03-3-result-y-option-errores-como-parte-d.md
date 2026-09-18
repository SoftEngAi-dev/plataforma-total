# 3. Result y Option: errores como parte del tipo

> 📚 Curso: **Rust — Velocidad de C sin Miedo a los Crashes** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```rust
RESULT/OPTION: NULL Y EXCEPCIONES, PERO TIPADOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  // Result<T, E> en vez de excepciones; Option<T> en vez de null:
  use std::fs;
  fn leer() -> Result<String, std::io::Error> {
      let texto = fs::read_to_string("notas.txt")?;      // ? = si error, devuélvelo ya
      Ok(texto)
  }

  // en main:
  match leer() {
      Ok(texto)   => println!("Contenido: {}", texto),
      Err(error)  => eprintln!("Falló: {}", error),
  }

  // Option para ausencia de valor (su Some/None):
  let tal = vec![1,2,3].first();      // Some(1) o None si vacío
  match tal {
      Some(n) => println!("primero: {}", n),
      None    => println!("lista vacía"),
  }
  // atajos: .unwrap_or(0) · .unwrap_or_else(...) (¡.unwrap() explota: avoid!)

EL PUNTO GENIAL: el COMPILADOR te obliga a manejar ambos casos. No hay "ops, me olvidé del null".

El operador ? propaga el error hacia arriba automáticamente = código delgado y seguro a la vez.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace el operador ? tras una llamada Result?
- A) Nada
- B) Si es Ok, desenvuelve el valor; si es Err, lo retorna inmediatamente a la función llamante (propagación elegante)
- C) Borra
- D) Bucle
### 2. ¿En qué consiste la seguridad adicional de Option<T> vs null?
- A) Es un puntero
- B) No hay null: la AUSENCIA es parte del TIPO y el compilador EXIGE manejar el caso None
- C) Es más rápido
- D) Sin diferencia

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Si es Ok, desenvuelve el valor; si es Err, lo retorna inmediatamente a la función llamante (propagación elegante) — El equivalente Go-verboso pero sin boilerplate: error handling conciso y explícito.
**2.** ✅ No hay null: la AUSENCIA es parte del TIPO y el compilador EXIGE manejar el caso None — Null = 'agujero invisible'; None = 'la firma te avisa y obliga'. Billion-dollar mistake corregida.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
