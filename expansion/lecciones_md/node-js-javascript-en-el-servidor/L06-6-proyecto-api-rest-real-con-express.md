# 6. Proyecto: API REST real con Express

> 📚 Curso: **Node.js — JavaScript en el Servidor** · Lección 6 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
CONSTRUYE: API DE NOTAS COMPLETA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MVP (3 pomodoros)
1. npm init -y; "type": "module"; npm i express dotenv
2. Rutas: GET /api/notas · GET /api/notas/:id · POST /api/notas · PATCH /api/notas/:id · DELETE /api/notas/:id
3. Datos: array en memoria primero; LUEGO archivito JSON con fs (persistencia real)
4. Validación: titulo obligatorio → 400; no existe → 404
5. status correctos: 200/201/400/404/500
6. Middleware: json + logger (console.log(req.method, req.url))
7. Probar: curl o Postman:
     curl -X POST localhost:3000/api/notas -H "Content-Type: application/json" -d '{"titulo":"hola"}'

BONUS NIVEL PRO
• Router modular en rutas/notas.js
• Middleware de errores 4-parámetros centralizado
• Paginación en GET: ?pagina=1&limite=10
• Tests con node --test + supertest

✅ Cuando: hiciste 5 endpoints funcionando con persistencia y status correctos, ya sabes construir backends. El curso de SQL le da memoria de verdad.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué códigos HTTP usan POST-crear y 'recurso no encontrado' respectivamente?
- A) 200 y 400
- B) 201 y 404
- C) 204 y 500
- D) 200 y 404
### 2. ¿Cómo probar un POST sin frontend?
- A) Solo desde el navegador
- B) curl / Postman / thunder client: cliente HTTP para probar endpoints
- C) Con console.log
- D) No se puede

---

## 🔑 Respuestas y explicaciones

**1.** ✅ 201 y 404 — 201 = creado; 404 = not found. La semántica HTTP es el idioma de las APIs.
**2.** ✅ curl / Postman / thunder client: cliente HTTP para probar endpoints — curl/demand-tester cliente es tu amigo backend: probar sin UI es el standard.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
