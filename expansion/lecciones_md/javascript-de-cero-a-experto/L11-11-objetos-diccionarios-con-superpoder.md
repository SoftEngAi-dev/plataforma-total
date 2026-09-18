# 11. Objetos: diccionarios con superpoderes

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 11 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
OBJETOS: CLAVE → VALOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const alumno = {
    nombre: "Ada",
    edad: 36,
    cursos: ["JS", "Python"],
    saludar() { return `Hola, soy ${this.nombre}`; }
  };

ACCEDER
  alumno.nombre              → "Ada"   (punto: lo más cómodo)
  alumno["edad"]             → 36      (corchete: claves dinámicas)
  const campo = "nombre"; alumno[campo] → "Ada"   ← por qué existe

  alumno.ciudad = "Londres";           // agregar
  delete alumno.edad;                  // borrar

ATALHOS MODERNOS
  const { nombre, edad = 18 } = alumno;      // DESTRUCTURING (¡úsalo!)
  const copia = { ...alumno, edad: 37 };     // spread: copia + sobreescribe

UTILIDADES
  Object.keys(alumno)      → ["nombre", "edad", "cursos", "saludar"]
  Object.values(alumno)    → lista de valores
  Object.entries(alumno)   → [["nombre","Ada"], ...]

THIS: dentro de métodos apunta al objeto. Las arrow functions NO lo capturan bien (usar function/método).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace const { nombre } = alumno?
- A) Borra nombre del objeto
- B) Extrae alumno.nombre en una variable llamada nombre (destructuring)
- C) Crea un objeto
- D) Convierte a JSON
### 2. ¿Cuándo usar alumno["nombre"] en vez de alumno.nombre?
- A) Nunca, es obsoleto
- B) Cuando la clave viene de una variable o tiene espacios
- C) Es más rápido
- D) Para métodos solamente

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Extrae alumno.nombre en una variable llamada nombre (destructuring) — Destructuring: la forma idiomática de extraer propiedades en JS moderno.
**2.** ✅ Cuando la clave viene de una variable o tiene espacios — Los corchetes aceptan expresiones: alumno[variable] resuelve la clave dinámicamente.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
