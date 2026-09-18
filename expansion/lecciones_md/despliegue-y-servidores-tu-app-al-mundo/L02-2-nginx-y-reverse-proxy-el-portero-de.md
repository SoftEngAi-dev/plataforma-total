# 2. Nginx y reverse proxy: el portero de tu servidor

> 📚 Curso: **Despliegue y Servidores — Tu App al Mundo** · Lección 2 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
NGINX: LA PUERTA DE ENTRADA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  /etc/nginx/sites-available/miapp:
  server {
      listen 80;
      server_name tudominio.com;
      location / {
          proxy_pass http://localhost:8000;        ← tu app Node/Python interna
          proxy_set_header Host $host;
      }
  }
  sudo nginx -t && sudo systemctl reload nginx

¿POR QUÉ NO EXPONER LA APP DIRECTO?
• Nginx sirve archivos estáticos (css/js/imágenes) SIN tocar tu app: veloz
• Un punto para HTTPS, límites de rate, cabeceras de seguridad
• Varios apps en un servidor: app1.dominio.com → :8000, app2 → :8001 (un solo 80/443 público)

HTTPS AUTOMÁTICO
  sudo certbot --nginx -d tudominio.com   (Let's Encrypt: certificado gratis, se renueva solo)

CADDY es alternativa moderna: HTTPS automático de salida, config de 3 líneas.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace proxy_pass http://localhost:8000?
- A) Borra peticiones
- B) Nginx recibe en el 80 público y reenvía internamente a tu app en :8000
- C) Sube archivos
- D) Cierra el puerto
### 2. ¿Por qué es estándar que la app corra en 127.0.0.1:8000 y no exponga su puerto?
- A) Es más rápido
- B) Control y seguridad: solo Nginx habla con el mundo; aplica HTTPS, límites y cabeceras en un solo sitio
- C) Porque sí
- D) Legal

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Nginx recibe en el 80 público y reenvía internamente a tu app en :8000 — Reverse proxy: un solo punto público, muchas apps atrás.
**2.** ✅ Control y seguridad: solo Nginx habla con el mundo; aplica HTTPS, límites y cabeceras en un solo sitio — El perímetro en un punto único de control es higiene de seguridad básica.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
