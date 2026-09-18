# 🎤 Banco de entrevista — 🚀 Astro — La Web de Contenido Moderna

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué envía Astro al navegador por defecto?**
   - Solo HTML + CSS estático (cero JS)  _(Esa es su superpotencia: HTML estático sin JS salvo que añadas islas interactivas.)_

2. **¿Qué son las <islas> de Astro?**
   - Componentes interactivos que se hidratan de forma aislada  _(Una isla (con client:load/visible…) se hidrata sola: el resto de la página sigue siendo HTML estático.)_

3. **¿Dónde se ejecuta el código del frontmatter (---) de un componente Astro?**
   - En el servidor o en build time  _(El frontmatter corre fuera del cliente; al navegador solo llega el HTML resultante.)_

4. **¿Cómo aplica por defecto Astro las reglas de un <style> dentro de un componente?**
   - Con scope automático solo a ese componente  _(Astro hashea las clases para que el estilo no se escape del componente.)_

5. **¿Qué combinación crea rutas estáticas tipo /blog/mi-post en Astro?**
   - src/pages/blog/[slug].astro + getStaticPaths  _(El [param].astro en src/pages + getStaticPaths enumera las rutas a generar en build.)_

6. **¿Para qué sirve un layout con <slot /> en Astro?**
   - Envolver páginas repitiendo cabecera y pie, metiendo el contenido dentro  _(El layout aporta la estructura común y cada página inyecta su contenido en el slot.)_

7. **¿Qué valida el esquema zod de una Content Collection?**
   - El frontmatter de cada Markdown durante el build  _(Si un post incumple el esquema, el build falla: contenido corrupto nunca llega a producción.)_

8. **¿Cómo obtienes todas las entradas de la colección blog?**
   - getCollection('blog')  _(getCollection devuelve las entradas tipadas; con entry.render() obtienes el HTML.)_

9. **¿Qué directiva hidrata una isla SOLO cuando el usuario la ve en pantalla?**
   - client:visible  _(client:visible usa IntersectionObserver: cero coste hasta que la isla es visible.)_

10. **¿Qué produce `astro build` por defecto?**
   - La carpeta dist/ estática lista para cualquier hosting  _(Salida 100% estática: la subes a cualquier CDN/hosting estático y vuela.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve 🚀 Astro y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta 🚀 Astro con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
