# 🎤 Banco de entrevista — 💚 Vue 3 — Composition API en Serio

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Cómo incrementas un ref dentro del <script setup>?**
   - contador.value++  _(En el script los refs se manipulan con .value; en el template Vue lo desenvuelve automáticamente.)_

2. **¿Qué tres bloques suele tener un Single File Component?**
   - script, template y style  _(El SFC agrupa lógica (script), vista (template) y estilos (style) en un solo archivo .vue.)_

3. **¿Qué hace computed() en Vue 3?**
   - Calcula un valor derivado con caché, recalculando solo si cambian las dependencias  _(El computed memoriza: si las dependencias no cambian, devuelve el valor cacheado.)_

4. **¿Qué hace v-model en un input?**
   - Enlace bidireccional: el input escribe el estado y el estado actualiza el input  _(v-model azucara value + @input: la vía rápida para formularios.)_

5. **¿Cómo comunica un componente hijo a su padre en Vue?**
   - Emitiendo un evento personalizado con emit()  _(Las props bajan, los eventos suben: el hijo emite, el padre decide qué hacer.)_

6. **¿Para qué sirve provide/inject?**
   - Pasar datos a descendientes lejanos sin retransmitir props intermedias  _(provide publica un valor en el árbol; inject lo consume a cualquier profundidad.)_

7. **¿Cuál es la forma reactiva de compartir estado global en Vue 3 moderno?**
   - Un store de Pinia con defineStore  _(Pinia es el store oficial: central, tipado y con Devtools; window es un hack frágil.)_

8. **En un store de Pinia, ¿qué es un getter?**
   - Un valor derivado del estado con caché (como computed)  _(Los getters son computed del store: se recalculan cuando cambia el estado base.)_

9. **¿Qué carpeta de Nuxt genera las rutas automáticamente?**
   - pages/  _(Cada .vue dentro de pages/ se convierte en ruta sin configurar ningún router.)_

10. **¿Dónde defines endpoints de backend en Nuxt 3?**
   - en server/api/  _(server/api/*.ts son endpoints Node del mismo proyecto, con despliegue integrado vía Nitro.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve 💚 Vue 3 y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta 💚 Vue 3 con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
