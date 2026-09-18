# 3. FastAPI: APIs con Python + TypeScript feel

> 📚 Curso: **APIs REST y HTTP — El Idioma de los Servidores** · Lección 3 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
FASTAPI: LA MÁQUINA DE APIs MODERNAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ventajas: tipado nativo, validación Pydantic automática, docs Swagger gratuitos, async nativo y¡veloz!.

  from fastapi import FastAPI, HTTPException
  from pydantic import BaseModel

  app = FastAPI()

  class TareaIn(BaseModel):              # ESQUEMA = validación automática de tus datos
      titulo: str
      hecha: bool = False

  tareas = []

  @app.get("/api/tareas")
  def listar():
      return {"tareas": tareas, "total": len(tareas)}

  @app.post("/api/tareas", status_code=201)
  def crear(tarea: TareaIn):              # FastAPI valida: si falta titulo → 422 automático
      nueva = {**tarea.dict(), "id": len(tareas) + 1}
      tareas.append(nueva)
      return nueva

  @app.get("/api/tareas/{id}")
  def una(id: int):
      if not 1 <= id <= len(tareas): raise HTTPException(404, "no existe")
      return tareas[id - 1]

  uvicorn main:app --reload           → http://localhost:8000/api/tareas
                                     → http://localhost:8000/docs  🎉 SWAGGER interactivo GRATIS

🎓 /docs + /redoc con tus endpoints, esquemas y botón "Try it out" sin escribir nada: por eso es el favorito.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace BaseModel de pydantic?
- A) Nada
- B) Esquema+validación automática de tus request bodies: si el usuario envía mal, 422 sin escribir código tú
- C) Only types
- D) SQL
### 2. ¿Qué dos cosas vienen GRATIS con FastAPI y ningún otro backend básico?
- A) Nada
- B) Swagger interactivo en /docs (probar la API desde el navegador) + validación automática
- C) Base de datos
- D) Frontend

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Esquema+validación automática de tus request bodies: si el usuario envía mal, 422 sin escribir código tú — TareaIn(titulo: str) garantiza str: errores de formato rechazados de fábrica (esa es la magia atrás de FastAPI).
**2.** ✅ Swagger interactivo en /docs (probar la API desde el navegador) + validación automática — Auto-docs + auto-valid: tu API se explica y se respeta sola.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
