# 4. Proyecto: API REST completa+cliente que la consume

> 📚 Curso: **APIs REST y HTTP — El Idioma de los Servidores** · Lección 4 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
CONSTRUYE: API + CLIENTE (LA PAREJA REAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. BACKEND: FastAPI (o tu framework del curso) con el CRUD completo de "recetas":
   recetas = [ ]  lista de {'id', 'titulo', 'ingredientes': lista, 'tiempo_min'}
   GET todos · GET /{id} · POST (validate: titulo requerido, min 3 chars) · PATCH · DELETE.
2. VALIDACIÓN Pydantic real: titulo: str; ingredientes: list[str]; tiempo_min: int = Field(gt=0).
3. MIDDLEWARE: logueo request method+path+time_ms (¡consola de verdad!)
4. CLIENTE (script separado):
     import httpx
     r = httpx.get("http://localhost:8000/api/recetas")
     for receta in r.json(): print(receta["id"], receta["titulo"])
     nueva = httpx.post(url, json={"titulo": "Tacos", ...}).json()
5. PRUEBA ACID TEST: cierras el servidor → corre el cliente → ¿EXCEPCIÓN? tu código NO está listo si no maneja errores de red (try/except + mensaje lindo).
6. ENTREGA: tu API corriendo en /docs abierta en el navegador en la captura del proyecto: el cliente consola mostrando datos vivos.

CONEXIÓN FRONTEND luego: esa MISMA api puede leerla el React/JS de tu proyecto anterior con fetch — MISMAS RECETAS EN WEB VIVA.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué testear el cliente CON EL API APAGADA?
- A) Por castigo
- B) El mundo real: redes caen siempre; tu cliente debe manejar errores de conexión con gracia, no un traceback
- C) Sin motivo
- D) Por bucles
### 2. ¿Qué hace especial al acceso a /docs de FastAPI?
- A) Nada especial
- B)  Swagger generado automáticamente de tus tipos: probar tu API en vivo desde el navegador, documentación incluida
- C) Caché
- D) SQL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ El mundo real: redes caen siempre; tu cliente debe manejar errores de conexión con gracia, no un traceback — Resiliencia honesta: probar el camino triste es parte del camino profesional.
**2.** ✅  Swagger generado automáticamente de tus tipos: probar tu API en vivo desde el navegador, documentación incluida — Value real: es tu documentacíon VIVA sin ninguna pieza extra de código your part.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
