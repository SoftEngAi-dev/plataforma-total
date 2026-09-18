# ⚠️ Errores comunes — 4. Amenazas en el código diario: XSS, CSRF y uploads

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Son iguales» → Frente a «¿En qué difiere XSS de CSRF?» lo fácil es confundirse. **Verdad**: XSS roba/ejecuta en NAVEGADOR ajeno (inyectar JS); CSRF fuerza ACCIONES con tu sesión (abusa confianza del sitio). XSS=inyección de scripts en users finales; CSRF=peticiones falsificadas usando la sesión del usuario.
- ❌ «Mismo vector» → Frente a «¿En qué difiere XSS de CSRF?» lo fácil es confundirse. **Verdad**: XSS roba/ejecuta en NAVEGADOR ajeno (inyectar JS); CSRF fuerza ACCIONES con tu sesión (abusa confianza del sitio). XSS=inyección de scripts en users finales; CSRF=peticiones falsificadas usando la sesión del usuario.
- ❌ «Hash» → Frente a «¿Cuál defensa mata CSRF de forma estructural?» lo fácil es confundirse. **Verdad**: Token CSRF único por formulario/sesión que el atacante no puede conocer + SameSite en cookies. El atacante puede enviar el request PERO no el token secreto del formulario legítimo.
- ❌ «HTTPS solo» → Frente a «¿Cuál defensa mata CSRF de forma estructural?» lo fácil es confundirse. **Verdad**: Token CSRF único por formulario/sesión que el atacante no puede conocer + SameSite en cookies. El atacante puede enviar el request PERO no el token secreto del formulario legítimo.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
