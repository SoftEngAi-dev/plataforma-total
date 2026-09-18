# 2. Tipos básicos y anotaciones

> 📚 Curso: **TypeScript — JavaScript con Superpoderes y Seguridad** · Lección 2 de 7
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
EL VOCABULARIO DE TIPOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const nombre: string = "Ada";
  const edad: number = 36;
  const activa: boolean = true;
  const temas: string[] = ["js", "ts"];
  const punto: [number, number] = [10, 20];        // tupla: posición y tipo fijos
  let cualquier: any = ...;                        // ⚠ desactiva la seguridad: evítalo
  let desconocido: unknown = ...;                  // any seguro: obliga a verificar antes de usar

INFERENCIA: TS adivina; SÓLO anota cuando no es obvio
  let total = 0;              // TS sabe que es number (no anotes de más)

FUNCIONES — lo más valioso está aquí:
  function sumar(a: number, b: number): number { return a + b; }
  const log = (m: string): void => { console.log(m); };    // void: no devuelve

OBJETOS
  type Alumno = { nombre: string; edad: number; email?: string };   // ? = opcional
  const ada: Alumno = { nombre: "Ada", edad: 36 };

LITERALES: type Rol = "admin" | "editor" | "lector";   ← solo esos valores
```

---

## 📝 Quiz de la lección

### 1. ¿Cuándo anotar tipos explícitamente?
- A) En TODAS las variables
- B) Cuando la inferencia no es obvia (y siempre en firmas de funciones públicas)
- C) Nunca
- D) Solo en clases
### 2. ¿Qué diferencia hay entre any y unknown?
- A) Ninguna
- B) any desactiva toda verificación; unknown exige comprobar el tipo antes de usarlo
- C) unknown es más corto
- D) any es para números

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Cuando la inferencia no es obvia (y siempre en firmas de funciones públicas) — TS infiere en la asignación; anota donde el contrato importa.
**2.** ✅ any desactiva toda verificación; unknown exige comprobar el tipo antes de usarlo — unknown = 'no sé aún, pero TS me protege'; any = 'ríndete, compilador'.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
