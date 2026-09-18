# 14. Eventos: la web reacciona

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 14 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
EVENTOS: LISTENERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  const boton = document.querySelector("#agregar");
  boton.addEventListener("click", () => {
    console.log("¡Clickeaste!");
  });

EVENTOS COMUNES
  click · dblclick · submit (formularios) · input/keydown/change (campos)
  mouseenter/mouseleave · scroll · DOMContentLoaded

EL OBJETO EVENT
  input.addEventListener("input", (evento) => {
    console.log(evento.target.value);      // lo que hay en el campo
  });

FORMULARIOS: el default es RECARGAR la página — evítalo:
  form.addEventListener("submit", (e) => {
    e.preventDefault();                    // ¡siempres!
    // procesar datos aquí
  });

DELEGACIÓN (para listas dinámicas): un listener en el padre que filtra por e.target
  lista.addEventListener("click", e => {
    if (e.target.matches(".borrar")) e.target.parentElement.remove();
  });
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué e.preventDefault() en el submit de un formulario?
- A) Acelera el envío
- B) Evita que el navegador recargue la página para procesarlo con JS
- C) Valida los campos
- D) Es opcional sin efecto
### 2. ¿Qué es delegación de eventos?
- A) Un listener por cada hijo
- B) Un solo listener en el padre que reacciona según e.target
- C) Eventos automáticos
- D) Eventos de red

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Evita que el navegador recargue la página para procesarlo con JS — Sin preventDefault, el formulario navega/recarga y tu lógica JS no corre.
**2.** ✅ Un solo listener en el padre que reacciona según e.target — Clave para contenido dinámico: los hijos futuros también funcionan.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
