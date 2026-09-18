# 📕 Resumen maestro — Despliegue y Servidores — Tu App al Mundo

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Dónde puede vivir tu app: el menú de opciones
OPCIONES DE HOSPEDAJE 2026 ━━━━━━━━━━━━━━━━━━━━━━━━━━━ ESTÁTICO (HTML/CSS/JS, SPAs compiladas — gratis y global): • GitHub Pages (directo de tu repo) · Netlify · Vercel (arrastras …

## 2. 2. Nginx y reverse proxy: el portero de tu servidor
NGINX: LA PUERTA DE ENTRADA ━━━━━━━━━━━━━━━━━━━━━━━━━━━   /etc/nginx/sites-available/miapp:   server {       listen 80;       server_name tudominio.com;       location / {         …

## 3. 3. Mantener tu app viva: systemd, pm2 y reinicios
PROCESOS QUE NO MUEREN (TRANQUILAMENTE) ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Cerrar la terminal no mataba tu app? Ahí entra el gestor de procesos.  SYSTEMD (nativo, universal en Linux — rec…

## 4. 4. Bases de datos en producción: presupuesto mínimo de seriedad
DATOS EN PROD: ALGUNOS PRECEPTOS DUROS ━━━━━━━━━━━━━━━━━━━━━━━━━━━ DONDE PONER LA BD • Hobby/practicar: SQLite en volumen persistente funciona PERFECTO (miles de apps reales la usa…

## 5. 5. GitHub Pages y Netlify: tu estática en 5 minutos
PUBLICA TU PRIMERA WEB HOY MISMO ━━━━━━━━━━━━━━━━━━━━━━━━━━━ A) GITHUB PAGES (desde tu repo) 1. Repo con index.html en la raíz 2. Settings → Pages → Source: "Deploy from a branch" …

## 6. 6. Proyecto final: tu app COMPLETA en internet con dominio
LA GRAN FINAL: DE CERO A URL PÚBLICA ━━━━━━━━━━━━━━━━━━━━━━━━━━━ LISTA DE MISIÓN (operativa, ~90 min, vale 1 curso entero) 1. App lista (backend con Dockerfile o web estática dist/…

---
✅ 6 lecciones · 📝 12 preguntas de repaso en quizzes_html/ · tests/