# 3. Dockerfile: empaquetar TU app

> 📚 Curso: **Docker — 'En Mi Máquina Sí Funciona' Resuelto** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```dockerfile
TU PROPIA IMAGEN: DOCKERFILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  # Dockerfile (app Python)
  FROM python:3.12-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  COPY . .
  CMD ["python", "app.py"]

CONSTRUIR Y CORRER
  docker build -t mi-app:1.0 .
  docker run -p 8000:8000 mi-app:1.0

LAYER CACHING (por qué ese orden): cada línea crea una capa cacheada. requirements PRIMERO (cambia poco), el código al FINAL (cambia siempre) → rebuilds en segundos.

.dockerignore (igual que .gitignore): evita copiar al contexto .git, .venv, node_modules → builds rápidos.

BUENAS PRÁCTICAS ESTRELLA
1. Imagen base slim/alpine · 2. Un proceso por contenedor · 3. No metas secretos (env al correr, no en la imagen) · 4. Multi-stage si compilas (golang/node): el binario final salta a una imagen vacía de compilador.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué COPY requirements.txt . va ANTES de COPY . .?
- A) Orden alfabético
- B) Cache de capas: cambiar el CÓDIGO no reinstala las dependencias (build rápido)
- C) Es más seguro
- D) Docker lo obliga
### 2. ¿Qué hace CMD ["python", "app.py"]?
- A) Instala python
- B) Define el comando por defecto al arrancar el contenedor
- C) Abre una shell
- D) Nada (comentario)

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Cache de capas: cambiar el CÓDIGO no reinstala las dependencias (build rápido) — Capas inmutables cacheadas: poner lo que menos cambia arriba maximiza reuso.
**2.** ✅ Define el comando por defecto al arrancar el contenedor — ENTRYPOINT+CMD definen el proceso principal: un contenedor sano = un proceso.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
