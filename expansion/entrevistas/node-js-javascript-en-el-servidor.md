# 🎤 Banco de entrevista — Node.js — JavaScript en el Servidor

> 12 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué es Node.js?**
   - Un runtime que ejecuta JS fuera del navegador (motor V8)  _(Mismo motor V8 de Chrome, liberado para servidores y scripts.)_

2. **¿Cómo activar ES Modules (import/export) en Node?**
   - "type": "module" en package.json (o usar .mjs)  _(Con esa flag, import from 'node:fs/promises' y top-level await funcionan nativamente.)_

3. **¿Por qué node_modules NUNCA va a git?**
   - Es enorme y reproducible: package.json + package-lock permiten recrearlo con npm install  _(El manifiesto viaja; el contenido se instala. Así mantienen repos livianos TODOS los equipos.)_

4. **¿Qué significa "express": "^4.19.2"?**
   - Cualquier versión 4.x.x compatible desde 4.19.2  _(^ permite parches y menores compatibles; el lock file congela la realidad exacta.)_

5. **¿Qué es un middleware en Express?**
   - Función que se ejecuta entre la petición y la ruta (JSON, auth, logs...)  _(app.use(express.json()) transforma req.body en datos listos — ejemplo clásico.)_

6. **¿Qué código HTTP corresponde a 'recurso creado'?**
   - 201  _(201 Created: convención para POST exitoso de recursos nuevos.)_

7. **¿Por qué prohibir readFileSync en un servidor (salvo arranque)?**
   - Bloquea el único hilo de Node: TODOS los usuarios esperan  _(El event loop único detenido = servidor congelado para todos.)_

8. **¿Cómo reconoce Express un middleware de errores?**
   - Tiene exactamente 4 parámetros (err, req, res, next)  _(La firma de 4 argumentos es el contrato; se registra DESPUÉS de las rutas.)_

9. **¿Por qué los secretos van en variables de entorno y no en el código?**
   - Para no publicarlos en git y poder variarlos por entorno (dev/prod)  _(Código público + secretos = filtración. .env + .gitignore es la norma; nunca commitees el .env.)_

10. **¿Qué aporta separar app.js de index.js (listen)?**
   - Puedes importar y TESTEAR la app sin abrir puerto; separa configuración de ejecución  _(La app testeable se exporta sin listen; en tests corren peticiones contra ella con supertest.)_

11. **¿Qué códigos HTTP usan POST-crear y 'recurso no encontrado' respectivamente?**
   - 201 y 404  _(201 = creado; 404 = not found. La semántica HTTP es el idioma de las APIs.)_

12. **¿Cómo probar un POST sin frontend?**
   - curl / Postman / thunder client: cliente HTTP para probar endpoints  _(curl/demand-tester cliente es tu amigo backend: probar sin UI es el standard.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Node.js y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Node.js con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
