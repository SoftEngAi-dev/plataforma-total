# 🎤 Banco de entrevista — ▲ Next.js — El React Moderno

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué es un React Server Component en Next.js App Router?**
   - Un componente que se renderiza en el servidor y no envía su JS al cliente  _(Corre en el servidor: puede usar async/await y recursos backend sin exponerlos al navegador.)_

2. **¿Qué archivo crea la ruta /dashboard en el App Router?**
   - app/dashboard/page.tsx  _(En app/, cada carpeta con page.tsx es una ruta; layouts y loading se anidan por segmento.)_

3. **¿Qué obliga escribir 'use client' al inicio de un componente?**
   - Usar useState, useEffect o manejadores como onClick  _(Esas APIs son del navegador; sin la directiva el componente se trata como Server Component y falla.)_

4. **¿Dónde conviene ubicar la directiva 'use client' para optimizar el bundle?**
   - En los componentes hoja interactivos, lo más abajo posible  _(Cuanto más abajo, menos JS viaja: el resto del árbol permanece como Server Components.)_

5. **¿Cómo se cargan datos en un Server Component de Next.js?**
   - Con await fetch directamente en el cuerpo async del componente  _(Al ejecutarse en el servidor, hacer await fetch en el componente es la vía natural y eficiente.)_

6. **¿Para qué sirve loading.tsx en una ruta?**
   - Muestra un fallback al instante mientras el segmento termina de cargar  _(Es un boundary de Suspense declarativo: el usuario ve esqueleto/UI de carga sin programarla.)_

7. **¿Qué es una Server Action?**
   - Una función que corre en el servidor invocable desde la UI sin escribir un endpoint  _(Con 'use server' declaras funciones backend llamables: Next genera el canal seguro automáticamente.)_

8. **¿Qué debes hacer SIEMPRE dentro de una Server Action?**
   - Validar entradas y comprobar permisos  _(El cliente puede enviar cualquier cosa: la action es tu última línea de defensa (zod + auth).)_

9. **¿Qué ventaja principal da next/image frente a una <img> normal?**
   - Optimiza tamaño/formato y evita saltos de layout (CLS)  _(Reserva el espacio, sirve webp/avif responsive y carga diferida: métricas Core Web Vitals sanas.)_

10. **¿Cómo defines el <title> y la descripción de una página en el App Router?**
   - export const metadata en page.tsx  _(metadata por segmento (objeto o generateMetadata async) alimenta <title>, meta y Open Graph.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve ▲ Next.js y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta ▲ Next.js con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
