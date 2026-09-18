# ⚠️ Errores comunes — 2. HTTPS, headers y sanitización: cimientos prácticos

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Oculta del JS» → Frente a «¿Qué hace el atributo HttpOnly en una cookie?» lo fácil es confundirse. **Verdad**: El JavaScript NO puede leerla: si un atacante ejecuta XSS no te roba la sesión. Las cookies de sesión SIEMPRE HttpOnly + Secure + SameSite.
- ❌ «La hace lenta» → Frente a «¿Qué hace el atributo HttpOnly en una cookie?» lo fácil es confundirse. **Verdad**: El JavaScript NO puede leerla: si un atacante ejecuta XSS no te roba la sesión. Las cookies de sesión SIEMPRE HttpOnly + Secure + SameSite.
- ❌ «Bloquea IPs» → Frente a «¿Qué defensa da Content-Security-Policy?» lo fácil es confundirse. **Verdad**: Limita de QUÉ orígenes pueden cargarse scripts/recursos: corta de raíz muchísimos XSS. CSP bien puesta desactiva la ejecución de scripts inyectados inline.
- ❌ «Acelera» → Frente a «¿Qué defensa da Content-Security-Policy?» lo fácil es confundirse. **Verdad**: Limita de QUÉ orígenes pueden cargarse scripts/recursos: corta de raíz muchísimos XSS. CSP bien puesta desactiva la ejecución de scripts inyectados inline.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
