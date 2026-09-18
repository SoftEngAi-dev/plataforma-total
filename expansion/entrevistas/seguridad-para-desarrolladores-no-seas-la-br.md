# 🎤 Banco de entrevista — Seguridad para Desarrolladores — No Seas la Brecha

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué es IDOR?**
   - Broken Access Control: cambiar el ID en la URL y acceder a datos de OTROS usuarios porque el servidor no verifica propiedad  _(/perfil/1 → cambias a /perfil/2 y ves datos ajenos si el servidor no checkea dueño.)_

2. **¿Cómo se guardan contraseñas correctamente?**
   - Hash con bcrypt/argon2 + salt: ni siquiera tú (admin) puedes leerlas  _(El hash robusto es irreversible y lento a propósito: el que dicen los propios hashes débiles.)_

3. **¿Qué hace el atributo HttpOnly en una cookie?**
   - El JavaScript NO puede leerla: si un atacante ejecuta XSS no te roba la sesión  _(Las cookies de sesión SIEMPRE HttpOnly + Secure + SameSite.)_

4. **¿Qué defensa da Content-Security-Policy?**
   - Limita de QUÉ orígenes pueden cargarse scripts/recursos: corta de raíz muchísimos XSS  _(CSP bien puesta desactiva la ejecución de scripts inyectados inline.)_

5. **¿Qué diferencia sesión-clásica de JWT?**
   - Sesión clásica guarda estado en el servidor con ID en cookie; JWT firma y viaja el estado EN EL TOKEN (stateless)  _(Trade: estado revocable/central vs escalabilidad sin estado ni revocación simple.)_

6. **¿Por qué JWT en localStorage es riesgoso?**
   - Cualquier XSS puede JavaScript-leerlo y robar identidad; cookie HttpOnly no es legible por JS  _(El trade de seguridad: lo que JavaScript toca, un XSS también toca.)_

7. **¿En qué difiere XSS de CSRF?**
   - XSS roba/ejecuta en NAVEGADOR ajeno (inyectar JS); CSRF fuerza ACCIONES con tu sesión (abusa confianza del sitio)  _(XSS=inyección de scripts en users finales; CSRF=peticiones falsificadas usando la sesión del usuario.)_

8. **¿Cuál defensa mata CSRF de forma estructural?**
   - Token CSRF único por formulario/sesión que el atacante no puede conocer + SameSite en cookies  _(El atacante puede enviar el request PERO no el token secreto del formulario legítimo.)_

9. **¿Qué descubre pegar <script>alert(1)</script> en un campo y probar?**
   - Si ves el alert: tu app ejecuta código de usuario = XSS confirmado  _(La prueba ácida manual del XSS: si JS injectado corre, tu escape no es suficiente.)_

10. **¿Por qué testear IDOR es tan crítico para endpoints con IDs?**
   - Es la vulnerabilidad web nº1 real: chequear que solo el DUEÑO accede a su recurso por cada request  _(La lección: no confíes en la URL escondida: cada query/id verifica ownership server-side.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Seguridad para Desarrolladores y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Seguridad para Desarrolladores con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
