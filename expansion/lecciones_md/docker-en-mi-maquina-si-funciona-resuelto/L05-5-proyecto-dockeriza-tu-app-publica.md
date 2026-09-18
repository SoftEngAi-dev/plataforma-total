# 5. Proyecto: dockeriza tu app + publica

> 📚 Curso: **Docker — 'En Mi Máquina Sí Funciona' Resuelto** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```dockerfile
DOCKERIZA UNA APP TUYA (HOY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PASOS (con tu proyecto Python o Node real)
1. Dockeriza: Dockerfile base slim + WORKDIR + requirements + COPY + CMD
2. docker build -t miusuario/miapp:1.0 .
3. Corre y verifica: docker run -p 8000:8000 miusuario/miapp:1.0 → abre localhost:8000
4. Datos: si usa SQLite o archivos, monta -v para persistirlos
5. Compose: agrega app + postgres/redis de juguete aunque no lo uses → practica up -d
6. Publica en Docker Hub: docker login && docker push miusuario/miapp:1.0
   → desde OTRO ordenador/servidor: docker pull y RUN: el momento "wow" entero.

CHECKLIST DE PRODUCCIÓN
• tag con versión exacta (no latest)
• imagen <200MB si se puede (multi-stage/alpine)
• secretos por -e / .env al correr: NUNCA en la imagen (está en las capas: pública)
• healthcheck o logs claros

🎯 Con esto, el curso de Despliegue se te hace fácil: un VPS moderno corre tu app con las mismas 2 órdenes.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué nunca incluir secretos DENTRO de la imagen Docker?
- A) La hace más lenta
- B) Las capas de la imagen son legibles por cualquiera que la tenga/descargue: filtras las claves
- C) Docker lo prohíbe
- D) No se puede
### 2. ¿Qué combina este proyecto como cierre del curso?
- A) Solo docker run
- B) Dockerfile + build + volúmenes + compose + push al registry
- C) Solo Kubernetes
- D) Edición de imágenes

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Las capas de la imagen son legibles por cualquiera que la tenga/descargue: filtras las claves — Secretos al correr (-e / compose env), nunca al build: la imagen te repite.
**2.** ✅ Dockerfile + build + volúmenes + compose + push al registry — El ciclo completo real: de tu código a imagen publicada y ejecutable en cualquier máquina.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
