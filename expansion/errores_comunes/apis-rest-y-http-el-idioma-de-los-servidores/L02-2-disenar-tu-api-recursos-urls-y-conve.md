# ⚠️ Errores comunes — 2. Diseñar tu API: recursos, URLs y convenciones

> APIs REST y HTTP — El Idioma de los Servidores · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «/api/crearTarea» → Frente a «¿Cómo es una buena URL de API?» lo fácil es confundirse. **Verdad**: /api/tareas (sustantivo plural; la ACCIÓN va en el método HTTP, no en la URL). Recursos=sustantivos; acciones=GET/POST/PATCH/DELETE: esa es la legibilidad REST.
- ❌ «/api/tareas.php» → Frente a «¿Cómo es una buena URL de API?» lo fácil es confundirse. **Verdad**: /api/tareas (sustantivo plural; la ACCIÓN va en el método HTTP, no en la URL). Recursos=sustantivos; acciones=GET/POST/PATCH/DELETE: esa es la legibilidad REST.
- ❌ «Es largo» → Frente a «¿Por qué responder 201 con el recurso creado en el POST?» lo fácil es confundirse. **Verdad**: El cliente recibe inmediato el objeto recién creado CON su id asignado; sin nueva llamada gratuita. El status informa lo ocurrido + la respuesta entrega el valor resultante.
- ❌ «Hype» → Frente a «¿Por qué responder 201 con el recurso creado en el POST?» lo fácil es confundirse. **Verdad**: El cliente recibe inmediato el objeto recién creado CON su id asignado; sin nueva llamada gratuita. El status informa lo ocurrido + la respuesta entrega el valor resultante.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
