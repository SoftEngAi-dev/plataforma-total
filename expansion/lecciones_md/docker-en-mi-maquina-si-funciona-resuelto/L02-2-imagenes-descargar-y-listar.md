# 2. Imágenes: descargar y listar

> 📚 Curso: **Docker — 'En Mi Máquina Sí Funciona' Resuelto** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```dockerfile
DOCKER HUB: LA TIENDA DE CONTENEDORES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  docker pull python:3.12-slim        # bajar imagen del registro público
  docker images                        # listar imágenes locales
  docker run -it python:3.12-slim      # correr interactiva (entra a su shell!)
  docker run -it python:3.12-slim python  # ejecuta python adentro

ETIQUETAS (:tag): python:3.12-slim · python:3.12-alpine (mínima) · latest (default, evítala en prod: no es determinista).
slim/alpine = mismos binarios, MUCHO menos MB: tu imagen de 1GB puede pesar 50MB.

CORRER UN SERVIDOR REAL (nginx) y verlo:
  docker run -d -p 8080:80 --name web nginx
  # -d = segundo plano · -p 8080:80 = tu puerto 8080 → puerto 80 del contenedor
  # abre http://localhost:8080 → ¡web servida sin instalar nginx!

  docker ps            # corriendo
  docker stop web      # parar
  docker rm web        # borrar el contenedor (la imagen queda)
```

---

## 📝 Quiz de la lección

### 1. En -p 8080:80, ¿qué es cada número?
- A) Dos contenedores
- B) Puerto DE TU MÁQUINA : puerto DEL CONTENEDOR
- C) CPU y memoria
- D) Versiones
### 2. ¿Por qué preferir python:3.12-slim sobre python:latest?
- A) Es más nueva
- B) Tamaño pequeño Y versión fijada (reproducible); latest es caja sorpresa y pesa GB
- C) Solo por moda
- D) latest no funciona

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Puerto DE TU MÁQUINA : puerto DEL CONTENEDOR — Mapeo de puertos: localhost:8080 → entra al contenedor en su puerto 80.
**2.** ✅ Tamaño pequeño Y versión fijada (reproducible); latest es caja sorpresa y pesa GB — Imágenes mínimas + tag exacto = builds rápidos, seguros y deterministas.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
