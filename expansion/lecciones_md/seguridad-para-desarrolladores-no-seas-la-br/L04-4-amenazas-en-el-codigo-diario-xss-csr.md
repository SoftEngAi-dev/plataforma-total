# 4. Amenazas en el código diario: XSS, CSRF y uploads

> 📚 Curso: **Seguridad para Desarrolladores — No Seas la Brecha** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
LOS 3 MONSTRUOS COTIDIANOS DEL LADO CLIENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
XSS (Cross-Site Scripting): atacante mete JavaScript en tu página y se ejecuta en navegadores ajenos.
  Vector: renderizar crudo lo que escribe el usuario: <img src=x onerror=robar()>
  Defensa: escapar SIEMPRE output (framework lo hace), CSP, evitar innerHTML/v-html con datos,
           sanitizar librerías probadas (DOMPurify) si HTML permitido.

CSRF (Cross-Site Request Forgery): usas mi sesión logueada para que YO haga acciones sin saberlo.
  Vector: mi banca logueada + página maliciosa envía <img src="banca.com/transferir?a=atacante&monto=1000">
  Defensa: tokens CSRF en formularios (el servidor solo acepta posts con su token aleatorio),
           cookies SameSite=Lax/Strict (no se mandan desde sitios cruzados).

UPLOADS (riesgo subido a 11)
  Nunca confiar extensión ni Content-Type (¡los falsifican!)
  Reglas: whitelist de extensiones · limita tamaño · chequea el MAGIC BYTES real (cabecera del archivo)
  · guarda fuera del root del servidor · nombres generados por ti (no el del usuario) · antivirus
  · imágenes: re-procesar (Pillow/ImageSharp las sanitiza normalizando).

PRINCIPIO TRANSVERSAL: toda decisión de seguridad = preguntar "¿y si el usuario es mi enemigo?" antes de escribir el endpoint.
```

---

## 📝 Quiz de la lección

### 1. ¿En qué difiere XSS de CSRF?
- A) Son iguales
- B) XSS roba/ejecuta en NAVEGADOR ajeno (inyectar JS); CSRF fuerza ACCIONES con tu sesión (abusa confianza del sitio)
- C) Mismo vector
- D) CSRF es más viejo
### 2. ¿Cuál defensa mata CSRF de forma estructural?
- A) Hash
- B) Token CSRF único por formulario/sesión que el atacante no puede conocer + SameSite en cookies
- C) HTTPS solo
- D) CSP

---

## 🔑 Respuestas y explicaciones

**1.** ✅ XSS roba/ejecuta en NAVEGADOR ajeno (inyectar JS); CSRF fuerza ACCIONES con tu sesión (abusa confianza del sitio) — XSS=inyección de scripts en users finales; CSRF=peticiones falsificadas usando la sesión del usuario.
**2.** ✅ Token CSRF único por formulario/sesión que el atacante no puede conocer + SameSite en cookies — El atacante puede enviar el request PERO no el token secreto del formulario legítimo.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
