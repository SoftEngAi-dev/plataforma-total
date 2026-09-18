# 📕 Resumen maestro — Docker — 'En Mi Máquina Sí Funciona' Resuelto

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Docker: qué es y por qué lo necesitas
CONTENEDORES: EMBALAJE ESTÁNDAR DE SOFTWARE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ PROBLEMA: "en mi máquina sí funciona" — Python 3.11 vs 3.9, librerías distintas, configs distintas. SOLU…

## 2. 2. Imágenes: descargar y listar
DOCKER HUB: LA TIENDA DE CONTENEDORES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   docker pull python:3.12-slim        # bajar imagen del registro público   docker images                     …

## 3. 3. Dockerfile: empaquetar TU app
TU PROPIA IMAGEN: DOCKERFILE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   # Dockerfile (app Python)   FROM python:3.12-slim   WORKDIR /app   COPY requirements.txt .   RUN pip install --no-cac…

## 4. 4. Volúmenes, redes y docker-compose: demasiado para la vida real
MÁS ALLÁ DEL CONTENEDOR EFÍMERO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ DATOS QUE SOBREVIVEN: un contenedor es descartable; una BD que borra datos al reiniciarse no sirve.   docker run -v …

## 5. 5. Proyecto: dockeriza tu app + publica
DOCKERIZA UNA APP TUYA (HOY) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ PASOS (con tu proyecto Python o Node real) 1. Dockeriza: Dockerfile base slim + WORKDIR + requirements + COPY + CMD 2. …

---
✅ 5 lecciones · 📝 10 preguntas de repaso en quizzes_html/ · tests/