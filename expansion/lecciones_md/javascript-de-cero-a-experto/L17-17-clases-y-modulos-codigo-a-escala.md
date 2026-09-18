# 17. Clases y módulos: código a escala

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 17 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
ESTRUCTURA CUANDO CRECE EL PROYECTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLASES (plantillas de objetos con comportamiento)
  class Tarea {
    constructor(titulo) {
      this.titulo = titulo;
      this.completada = false;
    }
    completar() { this.completada = true; }
    static desdeJSON(obj) { return Object.assign(new Tarea(obj.titulo), obj); }
  }
  const t = new Tarea("Estudiar clases");
  t.completar();

  class TareaUrgente extends Tarea {     // herencia
    completar() { super.completar(); this.prioridad = "alta"; }
  }

MÓDULOS ES (1 responsabilidad = 1 archivo)
  // utilidades.js
  export const sumar = (a, b) => a + b;
  export default class Calculadora { }

  // app.js
  import Calculadora, { sumar } from "./utilidades.js";

  En el navegador: <script type="module" src="app.js"></script>

REGLA: archivos como cajones etiquetados. Cuando uno pasa de ~300 líneas, pregúntate si son dos.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace export default frente a export nombrado?
- A) Es más rápido
- B) Un solo default por archivo, se importa sin llaves; los nombrados van con llaves exactas
- C) Default es privado
- D) No hay diferencia
### 2. ¿Qué hace super.completar() en una subclase?
- A) Borra el método del padre
- B) Invoca la versión del método en la clase padre
- C) Copia el objeto
- D) Nada

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Un solo default por archivo, se importa sin llaves; los nombrados van con llaves exactas — import X from... (default) vs import { x } from... (nombrados).
**2.** ✅ Invoca la versión del método en la clase padre — super = acceso a la clase padre: reutilizas y extiendes en vez de reescribir.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
