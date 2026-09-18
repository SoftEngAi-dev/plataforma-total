# 2. Formularios e inputs: la web habla contigo

> 📚 Curso: **HTML y CSS — Diseño Web Total** · Lección 2 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```html
FORMULARIOS: RECOGER DATOS DEL USUARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  <form action="/registro" method="POST">
    <label for="email">Email:</label>
    <input id="email" name="email" type="email" required>
    <input type="password" name="clave" minlength="8">
    <input type="number" name="edad" min="13" max="99">
    <select name="pais"><option value="UY">Uruguay</option></select>
    <textarea name="bio"></textarea>
    <button type="submit">Enviar</button>
  </form>

CLAVES
• name es lo que viaja al servidor (sin name no llega nada)
• label + for/id: accesibilidad Y clic más grande
• type valida gratis: email, number, date, url...
• required/min/max/minlength: validación HTML5 sin código

VALIDACIÓN EN DOS CAPAS
La validación HTML es para UX rápida; el servidor SIEMPRE valida de nuevo (el cliente es falsificable).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué atributo hace que el dato de un input llegue al servidor?
- A) id
- B) class
- C) name
- D) type
### 2. ¿Por qué validar también en el servidor si el HTML ya valida?
- A) Porque el HTML5 bugs mucho
- B) Porque la validación del cliente se puede saltar/falsificar
- C) No hace falta
- D) Para SEO

---

## 🔑 Respuestas y explicaciones

**1.** ✅ name — Sin name, el input no viaja con el formulario.
**2.** ✅ Porque la validación del cliente se puede saltar/falsificar — Toda entrada del cliente es hostil hasta que el servidor la valida.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
