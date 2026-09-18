# 4. Genéricos: reusabilidad con seguridad

> 📚 Curso: **TypeScript — JavaScript con Superpoderes y Seguridad** · Lección 4 de 7
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
GENÉRICOS: <T> = TIPO PARÁMETRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sin genérico pierdes tipos o repites código:
  function identidad<T>(valor: T): T { return valor; }
  identidad("hola")      → T = string
  identidad(42)          → T = number      (TS lo infiere)

CASOS REALES (los verás en TODAS las librerías)
  Array<string>          ≡ string[]
  Promise<Usuario>       → el await te da Usuario
  Map<string, number>    → diccionario con clave/valor tipados

RESTRINGIR (constraints): el genérico con requisitos mínimos:
  function largo<T extends { length: number }>(x: T): number { return x.length; }
  largo("hola")    ✅ (string tiene length)
  largo(42)        ❌

GENÉRICOS EN FUNCIONES DE API (el patrón favorito del mundo real):
  async function api<T>(url: string): Promise<T> { ... }
  const user = await api<Usuario>("/me");   // user: Usuario, autocomplete total

REGLA: cuando la firma de una función depende del tipo de OTRA parte de sí misma → genérico.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué gana identidad<T>(v: T): T respecto a misto?: any?
- A) Nada
- B) Recuerda el tipo exacto de entrada y lo devuelve: autocomplete y chequeo completos
- C) Es más rápido
- D) Evita compilar
### 2. ¿Qué hace <T extends { length: number }>?
- A) Crea una clase T
- B) Restringe T a tipos que tengan la propiedad length
- C) Hace T opcional
- D) Borra el tipo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Recuerda el tipo exacto de entrada y lo devuelve: autocomplete y chequeo completos — Los genéricos modelan RELACIONES entre tipos — any solo las borra.
**2.** ✅ Restringe T a tipos que tengan la propiedad length — Constraint: puedo usar .length sabiendo que el compilador lo garantiza.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
