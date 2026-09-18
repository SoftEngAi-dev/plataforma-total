# 📖 Glosario — 4. Amenazas en el código diario: XSS, CSRF y uploads

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 4 · Términos que debes poder definir sin mirar

- **XSS roba/ejecuta en NAVEGADOR ajeno (inyectar JS); CSRF fuerza ACCIONES con tu sesión (abusa confianza del sitio)** — XSS=inyección de scripts en users finales; CSRF=peticiones falsificadas usando la sesión del usuario.
- **Token CSRF único por formulario/sesión que el atacante no puede conocer + SameSite en cookies** — El atacante puede enviar el request PERO no el token secreto del formulario legítimo.

✍️ Ejercicio: añade debajo TU propia definición de cada término.
