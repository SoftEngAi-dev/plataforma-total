# 1. HTTP: el protocolo que habla el mundo

> 📚 Curso: **APIs REST y HTTP — El Idioma de los Servidores** · Lección 1 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
HTTP: LA LENGUA FRANCA DE INTERNET
━━━━━━━━━━━━━━━━━━━━━━━━━━━
REQUEST (tu pedido)
  GET /api/tareas/42 HTTP/1.1
  Host: miapp.com
  Authorization: Bearer eyJ...

RESPONSE (su respuesta)
  HTTP/1.1 200 OK
  Content-Type: application/json
  {"id": 42, "titulo": "Aprender HTTP"}

MÉTODOS (verbos, el QUÉ quieres hacer)
  GET    leer (no cambia nada, idempotente y cacheable)
  POST   crear (o acción compleja) NO idempotente: dos veces = dos efectos
  PUT    reemplazar completo · PATCH modificar parcial · DELETE borrar
STATUS (códigos que DEBES conocer de memoria)
  2xx ok: 200 ok · 201 creado · 204 borrado sin contenido
  3xx: 301 movido permanentemente · 304 no cambió (caché)
  4xx TU culpa: 400 malformado · 401 no autenticado · 403 autenticado pero prohibido
         · 404 no existe · 409 conflicto · 422 validación · 429 rate limit excedido
  5xx MI culpa (servidor): 500 error genérico · 503 caído temporalmente

HEADERS vitals: Content-Type · Accept · Authorization · Cookie · User-Agent · Cache-Control
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál es la diferencia entre 401 y 403?
- A) Ninguna
- B) 401 = falta autenticación (quién eres); 403 = ya sé quién eres pero NO tienes permiso
- C) 404
- D) 500 famila
### 2. ¿Qué significa que GET sea idempotente?
- A) Es lento
- B) Repetirlo N veces tiene el mismo efecto que 1: exige NO cambiar estado por definición REST
- C) Es seguro contra hackers
- D) Es corto

---

## 🔑 Respuestas y explicaciones

**1.** ✅ 401 = falta autenticación (quién eres); 403 = ya sé quién eres pero NO tienes permiso — Autenticación vs autorización: la confusión más común en APIs.
**2.** ✅ Repetirlo N veces tiene el mismo efecto que 1: exige NO cambiar estado por definición REST — GET/PUT/DELETE= idempotentes; POST no: eso decide reintentos seguros en tu cliente.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
