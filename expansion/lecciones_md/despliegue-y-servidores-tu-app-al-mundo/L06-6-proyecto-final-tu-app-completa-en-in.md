# 6. Proyecto final: tu app COMPLETA en internet con dominio

> 📚 Curso: **Despliegue y Servidores — Tu App al Mundo** · Lección 6 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
LA GRAN FINAL: DE CERO A URL PÚBLICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
LISTA DE MISIÓN (operativa, ~90 min, vale 1 curso entero)
1. App lista (backend con Dockerfile o web estática dist/)
2. ELIGE CAMINO:
   A) Estática → Netlify/GitHub Pages (ya la tienes en 5 min)
   B) Backend → Railway/Render (conecta repo → detecta Dockerfile → URL pública automática)
   C) VPS (el épico): Hetzner/DO ~$5 → ssh → docker compose up → nginx + certbot
3. DOMINIO: compra uno barato → registro A/CNAME a tu hosting → espera propagación
4. HTTPS: Caddy o certbot --nginx (confirmar candado verde en el navegador)
5. VARIABLES de producción seteadas (DB url, secrets) en el panel de tu proveedor
6. MONITOREO: Uptime Kuma propio o servicio simple que pida tu /health

EJERCICIO CLAVE: mándale el link a un amigo. "https://miapp.midominio.com funciona" = ya eres DevOps practicante en formación.

DOCUMENTA en el README: screenshot + URL + stack usado. Tu portafolio quedó completo: código (GitHub) + app viva (dominio) + pipeline (Actions verde).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué verifica que realmente desplegaste bien?
- A) Que corre local
- B) URL pública + HTTPS (candado) + datos persistiendo + se mantiene tras reinicios
- C) Compilar
- D) 1 test verde
### 2. ¿Por qué documentar el despliegue en el README del proyecto?
- A) Es bonito
- B) URL viva en tu portafolio es la prueba '#1 para recruiters: cualquiera entra y ve tu trabajo andando
- C) Google lo pide
- D) SEO del repo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ URL pública + HTTPS (candado) + datos persistiendo + se mantiene tras reinicios — Accesibilidad real desde afuera, seguridad básica y persistencia: la trifecta del deploy.
**2.** ✅ URL viva en tu portafolio es la prueba '#1 para recruiters: cualquiera entra y ve tu trabajo andando — El link que demuestra es infinitamente más persuasivo que la descripción.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
