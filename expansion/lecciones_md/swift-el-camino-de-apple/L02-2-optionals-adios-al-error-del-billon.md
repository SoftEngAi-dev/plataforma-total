# 2. Optionals: adiós al error del billón de dólares

> 📚 Curso: **Swift — El Camino de Apple** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```swift
OPTIONALS: NULL-SAFETY EN EL ADN
━━━━━━━━━━━━━━━━━━━━━━━━━━━
En Swift un valor SÍ puede faltar, pero el tipo te obliga a encararlo:
  var apodo: String? = nil            // String? = "String opcional": puede ser nil
  var nombre: String = "Ada"          // String plano: NUNCA puede ser nil (¡el tipo lo garantiza!)

DESEMPAQUETAR (las 4 formas de la vida real)
1. IF LET (la más segura y común):
   if let a = apodo { print("Se llama \(a)") } else { print("sin apodo") }
2. GUARD LET (salida temprana — el favorito en funciones):
   guard let a = apodo else { return }   // si nil, te vas ya; abajo 'a' es String real
   print(a.count)
3. NIL COALESCING ?? :
   let mostrar = apodo ?? "sin apodo"
4. OPTIONAL CHAINING ?. :
   let largo = apodo?.count            // solo si existe; largo queda Int?

⚠ EL PELIGRO: ! (force unwrap: apodo!) — crash si es nil. Úsalo solo cuando estés 100% seguro.
Esta rigurosidad es POR QUÉ las apps Swift crashean menos de pánico nil.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace guard let x = y else { return }?
- A) Repite
- B) Si y es nil, sale de la función ya; si no, x queda disponible desempaquetada para el resto
- C) Un bucle
- D) Un error
### 2. ¿Por qué se considera peligroso el force unwrap (!) ?
- A) Es lento
- B) Si el valor es nil, la app CRASHEA en runtime: evitas el mecanismo que te protege
- C) No compila
- D) Es obsoleto

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Si y es nil, sale de la función ya; si no, x queda disponible desempaquetada para el resto — Guard clause: los casos raros se despachan arriba y el código queda plano y claro.
**2.** ✅ Si el valor es nil, la app CRASHEA en runtime: evitas el mecanismo que te protege — El '!' es jurarle al compilador 'está ahí': cuando mientes, paga la app.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
