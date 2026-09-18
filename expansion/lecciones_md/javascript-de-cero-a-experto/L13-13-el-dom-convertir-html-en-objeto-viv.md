# 13. El DOM: convertir HTML en objeto vivo

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 13 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
DOM: EL HTML COMO OBJETOS MANIPULABLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El navegador convierte tu HTML en un árbol de objetos: el DOM. JS lo lee y lo MODIFICA en vivo.

SELECCIONAR
  document.querySelector(".tarjeta")       ← el primero que coincide (selector CSS)
  document.querySelectorAll("p")           ← todos (NodeList iterable)
  document.getElementById("titulo")        ← por id (viejo pero válido)

LEER Y CAMBIAR
  el.textContent = "Nuevo texto";          // texto plano
  el.innerHTML = "<b>Marcado</b>";          // HTML (⚠ riesgo de inyección con input de usuario)
  el.style.color = "red";                   // CSS inline
  el.classList.add("activa");   el.classList.toggle("activa");   // clases ✅ mejor práctica

CREAR Y ANEXAR
  const p = document.createElement("p");
  p.textContent = "Hola, DOM";
  document.body.appendChild(p);

REGLA: evita innerHTML con datos de usuario (XSS); textContent es seguro por defecto.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué método es seguro para insertar TEXTO de usuario en la página?
- A) innerHTML
- B) textContent
- C) eval()
- D) document.write()
### 2. ¿Qué hace el.classList.toggle('activa')?
- A) Siempre la añade
- B) Siempre la quita
- C) La añade si no está, la quita si está
- D) La renombra

---

## 🔑 Respuestas y explicaciones

**1.** ✅ textContent — textContent no interpreta HTML: protege contra inyección XSS básica.
**2.** ✅ La añade si no está, la quita si está — Toggle = interruptor: perfecto para menús, modos oscuro/claro, etc.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
