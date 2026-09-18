# 15. Asincronía: setTimeout, promesas y async/await

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 15 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
ASINCRONÍA: NO BLOQUEAR LA FIESTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JS corre en un solo hilo. Las operaciones lentas (red, disco, timers) NO deben congelar la página. Solución: asincronía.

TIMER
  setTimeout(() => console.log("pasaron 2s"), 2000);   // no bloquea

PROMESAS (un valor que llegará: pending → fulfilled/rejected)
  fetch(url)
    .then(respuesta => respuesta.json())
    .then(datos => console.log(datos))
    .catch(error => console.error(error));

ASYNC/AWAIT — la sintaxis moderna (ES azúcar sobre promesas, se lee de arriba hacia abajo)
  async function traerUsuarios() {
    try {
      const resp = await fetch("/api/usuarios");
      const datos = await resp.json();
      console.log(datos);
    } catch (e) { console.error("Falló:", e); }
  }

REGLAS
1. await SOLO dentro de async
2. Siempre maneja errores (try/catch o .catch)
3. Promise.all([p1, p2]) → varias en paralelo
```

---

## 📝 Quiz de la lección

### 1. ¿Qué devuelve inmediatamente una función async?
- A) El resultado final
- B) Una promesa
- C) undefined
- D) El error
### 2. ¿Para qué sirve Promise.all?
- A) Cancelar promesas
- B) Esperar varias promesas EN PARALELO y continuar cuando todas terminan
- C) Convertir promesas a callbacks
- D) Una por una

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Una promesa — async significa 'esto devolverá una promesa'; await desenvuelve su valor.
**2.** ✅ Esperar varias promesas EN PARALELO y continuar cuando todas terminan — Paralelismo de verdad: si son independientes, esperar juntas = mitad del tiempo.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
