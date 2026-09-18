# 🎤 Banco de entrevista — APIs REST y HTTP — El Idioma de los Servidores

> 8 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Cuál es la diferencia entre 401 y 403?**
   - 401 = falta autenticación (quién eres); 403 = ya sé quién eres pero NO tienes permiso  _(Autenticación vs autorización: la confusión más común en APIs.)_

2. **¿Qué significa que GET sea idempotente?**
   - Repetirlo N veces tiene el mismo efecto que 1: exige NO cambiar estado por definición REST  _(GET/PUT/DELETE= idempotentes; POST no: eso decide reintentos seguros en tu cliente.)_

3. **¿Cómo es una buena URL de API?**
   - /api/tareas (sustantivo plural; la ACCIÓN va en el método HTTP, no en la URL)  _(Recursos=sustantivos; acciones=GET/POST/PATCH/DELETE: esa es la legibilidad REST.)_

4. **¿Por qué responder 201 con el recurso creado en el POST?**
   - El cliente recibe inmediato el objeto recién creado CON su id asignado; sin nueva llamada gratuita  _(El status informa lo ocurrido + la respuesta entrega el valor resultante.)_

5. **¿Qué hace BaseModel de pydantic?**
   - Esquema+validación automática de tus request bodies: si el usuario envía mal, 422 sin escribir código tú  _(TareaIn(titulo: str) garantiza str: errores de formato rechazados de fábrica (esa es la magia atrás de FastAPI).)_

6. **¿Qué dos cosas vienen GRATIS con FastAPI y ningún otro backend básico?**
   - Swagger interactivo en /docs (probar la API desde el navegador) + validación automática  _(Auto-docs + auto-valid: tu API se explica y se respeta sola.)_

7. **¿Por qué testear el cliente CON EL API APAGADA?**
   - El mundo real: redes caen siempre; tu cliente debe manejar errores de conexión con gracia, no un traceback  _(Resiliencia honesta: probar el camino triste es parte del camino profesional.)_

8. **¿Qué hace especial al acceso a /docs de FastAPI?**
   -  Swagger generado automáticamente de tus tipos: probar tu API en vivo desde el navegador, documentación incluida  _(Value real: es tu documentacíon VIVA sin ninguna pieza extra de código your part.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve APIs REST y HTTP y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta APIs REST y HTTP con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
