# 🎤 Banco de entrevista — 🎨 Tailwind CSS — Diseño a Velocidad

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué es el enfoque utility-first de Tailwind?**
   - Componer el diseño con muchas clases de un solo propósito en el HTML  _(Muchas utilidades pequeñas y predecibles que se combinan: el diseño vive junto al marcado.)_

2. **¿Por qué el CSS final en producción con Tailwind es pequeño?**
   - Porque solo se generan las clases que realmente usas  _(El compilador detecta las clases presentes en tus archivos y emite únicamente esas reglas.)_

3. **¿Qué significa la clase md:grid-cols-3?**
   - 3 columnas a partir del breakpoint md (768px) hacia arriba  _(Tailwind es mobile-first: el base es móvil y los prefijos md:/lg: aplican hacia arriba.)_

4. **¿Cómo centras horizontalmente un contenedor con ancho máximo?**
   - con la clase mx-auto (más max-w-* o container)  _(mx-auto reparte el margen lateral; text-center solo alinea texto en línea.)_

5. **¿Cómo haces que un hijo cambie cuando el padre recibe hover?**
   - Con group en el padre y group-hover: en el hijo  _(group marca el contenedor; group-hover:aplica-estilo solo cuando el grupo está en hover.)_

6. **¿Qué hace la clase transition en un botón?**
   - Anima suavemente los cambios de propiedades (color, escala…) entre estados  _(transition + duration-* suaviza hover/active/focus sin escribir @keyframes.)_

7. **En Tailwind v4, ¿dónde defines colores de marca personalizados?**
   - En el bloque @theme de tu archivo CSS  _(@theme genera tokens (p. ej. --color-marca) que se convierten en clases como bg-marca automáticamente.)_

8. **¿Para qué sirve @apply?**
   - Reutilizar un conjunto de utilidades dentro de una clase propia  _(@apply incrusta utilidades en .mi-clase (útil para patrones repetidos), aunque los componentes suelen abstraer mejor.)_

9. **¿Qué es shadcn/ui?**
   - Componentes accesibles (Radix + Tailwind) que copias a tu proyecto y son tuyos  _(No es una dependencia: copia el código del componente a tu repo, con accesibilidad Radix y estilos Tailwind incluidos.)_

10. **¿Qué clase de Tailwind muestra un texto solo a lectores de pantalla?**
   - sr-only  _(sr-only lo oculta visualmente pero mantiene accesibilidad para tecnologías asistivas.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve 🎨 Tailwind CSS y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta 🎨 Tailwind CSS con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
