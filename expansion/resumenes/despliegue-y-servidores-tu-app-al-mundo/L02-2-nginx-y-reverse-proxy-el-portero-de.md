# ⚡ Cheatsheet — 2. Nginx y reverse proxy: el portero de tu servidor

> Despliegue y Servidores — Tu App al Mundo · Lección 2 · 18/09/2026

## 💡 Idea central
NGINX: LA PUERTA DE ENTRADA

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué hace proxy_pass http://localhost:8000?** → Nginx recibe en el 80 público y reenvía internamente a tu app en :8000 _(Reverse proxy: un solo punto público, muchas apps atrás.)_
- **¿Por qué es estándar que la app corra en 127.0.0.1:8000 y no exponga su puerto?** → Control y seguridad: solo Nginx habla con el mundo; aplica HTTPS, límites y cabeceras en un solo sitio _(El perímetro en un punto único de control es higiene de seguridad básica.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
