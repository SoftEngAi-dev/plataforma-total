# 12. JSON: el idioma universal de los datos

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 12 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
JSON: DE TEXTO A DATOS Y VUELTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JSON (JavaScript Object Notation) es EL formato para mover datos entre sistemas: APIs, archivos, bases de datos.

SE PARECE a un objeto JS pero: claves SIEMPRE con comillas dobles, sin funciones, sin comentarios.
  '{"nombre":"Ada","edad":36,"activa":true}'

LAS DOS FUNCIONES
我们可以JSON
  const texto = JSON.stringify(alumno);      // objeto → TEXTO (para enviar/guardar)
  const obj   = JSON.parse(texto);           // TEXTO → objeto (al recibir/leer)

USO REAL
  // Guardar en localStorage del navegador:
  localStorage.setItem("alumno", JSON.stringify(alumno));
  const recuperado = JSON.parse(localStorage.getItem("alumno"));

  // Enviar a una API (lo veremos con fetch):
  fetch("/api", { method: "POST", body: JSON.stringify(datos) })

TRAPPER ERROR COMÚN
JSON.parse(texto inválido) → SyntaxError. En producción: try/catch y valida.

INDENTADO para humanos: JSON.stringify(obj, null, 2).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace JSON.stringify(datos)?
- A) Lee un archivo
- B) Convierte datos JS en texto JSON para guardar/enviar
- C) Valida el JSON
- D) Imprime bonito
### 2. ¿Qué pasa si JSON.parse recibe texto mal formado?
- A) Devuelve null
- B) Devuelve el texto igual
- C) Lanza SyntaxError
- D) Lo repara solo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Convierte datos JS en texto JSON para guardar/enviar — stringify serializa; parse deserializa. Juntas son el puente de datos.
**2.** ✅ Lanza SyntaxError — parse es estricto — envuélvelo en try/catch en código serio.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
