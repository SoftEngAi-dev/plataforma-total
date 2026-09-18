# 2. HTTPS, headers y sanitización: cimientos prácticos

> 📚 Curso: **Seguridad para Desarrolladores — No Seas la Brecha** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
DEFENSA EN CAPAS (LO QUE CONFIGURAS HOY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
HTTPS OBLIGATORIO SIEMPRE
• Todo login/dato viaja cifrado. Certbot + Let's Encrypt = gratis y automático.
• Redirect 80→443, y HSTS header (instruye al navegador a usar SIEMPRE https).

HEADERS DE SEGURIDAD (configuración de 5 minutos que suman mucho)
  Content-Security-Policy: default-src 'self'    ← de dónde puede cargar recursos (anti-XSS fuerte)
  X-Frame-Options: DENY                          ← anti clickjacking (no te meten en iframe falso)
  X-Content-Type-Options: nosniff
  Referrer-Policy: no-referrer
  Strict-Transport-Security: max-age=31536000    (HSTS)
En: securityheaders.com pegas tu URL y te evalúa gratis.

SANITIZAR VS ESCAPAR (distintos y ambos necesarios)
• VALIDAR: formato, tipo, rango ("email", número 0-100) al ENTRAR
• ESCAPAR: convertir <script> a &lt;script&gt; al MOSTRAR → el XSS muere de risa
  Frameworks modernos (React {{}}, Django {{ }} escapan por defecto; cuando usas innerHTML/href dinámicos arriesgas.
• Cookies seguras: HttpOnly (JS no las lee, anti-XSS robo) + Secure (solo https) + SameSite=Lax (anti-CSRF)
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace el atributo HttpOnly en una cookie?
- A) Oculta del JS
- B) El JavaScript NO puede leerla: si un atacante ejecuta XSS no te roba la sesión
- C) La hace lenta
- D) Borra cookies
### 2. ¿Qué defensa da Content-Security-Policy?
- A) Bloquea IPs
- B) Limita de QUÉ orígenes pueden cargarse scripts/recursos: corta de raíz muchísimos XSS
- C) Acelera
- D) Nada útil

---

## 🔑 Respuestas y explicaciones

**1.** ✅ El JavaScript NO puede leerla: si un atacante ejecuta XSS no te roba la sesión — Las cookies de sesión SIEMPRE HttpOnly + Secure + SameSite.
**2.** ✅ Limita de QUÉ orígenes pueden cargarse scripts/recursos: corta de raíz muchísimos XSS — CSP bien puesta desactiva la ejecución de scripts inyectados inline.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
