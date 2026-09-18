# 16. fetch: hablar con APIs del mundo

> 📚 Curso: **JavaScript — De Cero a Experto** · Lección 16 de 18
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
FETCH: CLIENTE DE APIS EN 10 LÍNEAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GET (leer):
  const resp = await fetch("https://api.github.com/users/octocat");
  if (!resp.ok) throw new Error("HTTP " + resp.status);   // ¡fetch NO falla en 404/500!
  const datos = await resp.json();

POST (enviar):
  const resp = await fetch("/api/tareas", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ titulo: "Aprender fetch" })
  });

LAYOUT COMPLETO PROFESIONAL
  async function api(url, opciones = {}) {
    const resp = await fetch(url, opciones);
    if (!resp.ok) throw new Error(`${resp.status} ${resp.statusText}`);
    return resp.json();
  }

RECUERDOS VITALES
1. resp.ok es tu responsabilidad: fetch solo rechaza en error de RED
2. JSON requiere el header Content-Type al enviar
3. Las APIs públicas gratis para practicar: JSONPlaceholder, PokéAPI, GitHub API
```

---

## 📝 Quiz de la lección

### 1. ¿Cuándo rechaza fetch (lanza error) SIN ayuda tuya?
- A) En cualquier error HTTP 4xx/5xx
- B) Solo en errores de red (sin conexión, CORS, DNS)
- C) Siempre que resp.ok es false
- D) Nunca
### 2. ¿Qué header obliga al enviar JSON con POST?
- A) Accept
- B) Content-Type: application/json
- C) Authorization
- D) User-Agent

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Solo en errores de red (sin conexión, CORS, DNS) — Por eso el patrón: chequear resp.ok y lanzar tu propio error en 4xx/5xx.
**2.** ✅ Content-Type: application/json — Sin ese header, muchos servidores no interpretan el body como JSON.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
