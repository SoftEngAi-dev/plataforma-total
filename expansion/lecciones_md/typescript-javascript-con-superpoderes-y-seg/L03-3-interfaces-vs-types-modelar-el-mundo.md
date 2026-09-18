# 3. Interfaces vs Types: modelar el mundo

> 📚 Curso: **TypeScript — JavaScript con Superpoderes y Seguridad** · Lección 3 de 7
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
MODELAR DATOS CON ESTILO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERFACE — el contrato de forma de un objeto:
  interface Usuario {
    id: number;
    nombre: string;
    email?: string;          // opcional
    readonly creado: Date;   // solo lectura tras crear
  }
  function guardar(u: Usuario) { ... }

TYPE — el comodín: uniones, intersecciones, alias, todo:
  type Resultado = "ok" | "error";
  type Admin = Usuario & { permisos: string[] };        // intersección

EXTENDER
  interface ConEmail extends Usuario { email: string; }  // requerido aquí

¿CUÁL USAR? Convención 2026:
• Formas de objetos/clases/domínio → interface (mensajes de error más claros, se fusionan)
• Uniones, tuplas, funciones, composiciones → type

UTILITY TYPES (los usarás con React y APIs):
  Partial<Usuario>  (todo opcional) ·  Required  ·  Pick<Usuario,"nombre">  ·  Omit
```

---

## 📝 Quiz de la lección

### 1. ¿Cuándo elegir interface sobre type?
- A) Siempre
- B) Para formas de objetos: más legible, mensajes de error claros y extensión natural
- C) Nunca
- D) Solo en Angular
### 2. ¿Qué expresa type Estado = "cargando" | "ok" | "error"?
- A) Un objeto
- B) Una unión de literales: la variable solo vale uno de esos strings
- C) Un enum numérico
- D) Un error

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Para formas de objetos: más legible, mensajes de error claros y extensión natural — Interface para modelos de dominio; type para uniones y composiciones.
**2.** ✅ Una unión de literales: la variable solo vale uno de esos strings — Uniones de literales = estados exhaustivos que TS puede verificar (sin strings sueltos).

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
