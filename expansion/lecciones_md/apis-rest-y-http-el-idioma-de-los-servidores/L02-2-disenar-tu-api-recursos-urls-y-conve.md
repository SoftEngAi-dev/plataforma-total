# 2. Diseñar tu API: recursos, URLs y convenciones

> 📚 Curso: **APIs REST y HTTP — El Idioma de los Servidores** · Lección 2 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
DISEÑO REST QUE LOS DEMÁS ENTIENDEN AL INSTANTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
LOS RECURSOS VIVEN EN LOS NOMBRES DE LAS URLs (sustantivos PLURALES, no verbos)
  GET    /api/tareas          lista (paginada con ?pagina=2&limite=20)
  POST   /api/tareas          crear (201 + body del creado)
  GET    /api/tareas/42       detalle de una
  PATCH  /api/tareas/42       modificar campos
  DELETE /api/tareas/42       borrar (204 sin body)

ERRORES CON FORMATEADO ÚNICO (los consumidores lo agradecen)
  400 → {"error": {"codigo": "VALIDACION", "mensaje": "titulo es requerido", "campo": "titulo"}}
  Simetric: el cliente parsea un formato y listo para siempre.

FILTROS/BÚSQUEDA/ORDEN con query params:
  /api/tareas?estado=pendiente&orden=-creado&busqueda=curso
PAGINACIÓN: ?pagina=2&limite=20 con next/prev en la respuesta (links o metadata count).

VERSIONADO: /api/v1/tareas (v2 rompe cuando la v1 mantienes viva para legacy: no rompes a tus consumidores).
DOCUMENTACIÓN: OpenAPI/Swagger auto-generada (FastAPI lo trae y regs gratis /docs interactivos)
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo es una buena URL de API?
- A) /api/crearTarea
- B) /api/tareas (sustantivo plural; la ACCIÓN va en el método HTTP, no en la URL)
- C) /api/tareas.php
- D) con verbo
### 2. ¿Por qué responder 201 con el recurso creado en el POST?
- A) Es largo
- B) El cliente recibe inmediato el objeto recién creado CON su id asignado; sin nueva llamada gratuita
- C) Hype
- D) Caché

---

## 🔑 Respuestas y explicaciones

**1.** ✅ /api/tareas (sustantivo plural; la ACCIÓN va en el método HTTP, no en la URL) — Recursos=sustantivos; acciones=GET/POST/PATCH/DELETE: esa es la legibilidad REST.
**2.** ✅ El cliente recibe inmediato el objeto recién creado CON su id asignado; sin nueva llamada gratuita — El status informa lo ocurrido + la respuesta entrega el valor resultante.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
