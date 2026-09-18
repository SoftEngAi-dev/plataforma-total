# 📕 Resumen maestro — JavaScript — De Cero a Experto

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. JavaScript: el lenguaje que está en todas partes
JS: DE NAVEGADOR A TODAS PARTES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Nació en 10 días en 1995. Hoy corre en: navegadores, servidores (Node), móviles, desktops, satélites.  TU PRIMER CÓD…

## 2. 2. Variables: let, const y por qué var quedó atrás
LET Y CONST (y olvida var por ahora) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   const nombre = "Ada";       // NO se puede reasignar. EL POR DEFECTO.   let edad = 36;              // reasig…

## 3. 3. Tipos de datos y operadores
LOS 8 TIPOS QUE IMPORTAN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ PRIMITIVOS: string, number, boolean, undefined, null, bigint, symbol   "hola" · 42 · 3.14 · true · undefined (no asignado) …

## 4. 4. Strings: la caja de herramientas del texto
TEXTO COMO DATO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   const nombre = "Ada Lovelace";  PLANTILLAS LITERALES (backticks): las usarás siempre   `Hola ${nombre}, tienes ${2026 - 1815} años…

## 5. 5. Números, mate y errores clásicos
NÚMEROS Y SUS TRAMPAS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Un solo tipo number para enteros y decimales (punto flotante de 64 bits).    const precio = 19.99;   Math.round(precio)     → …

## 6. 6. Condicionales: if, else y el operador ternario
DECISIONES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   if (edad >= 18) {     acceso = "permitido";   } else if (edad >= 13) {     acceso = "con tutor";   } else {     acceso = "denegado";   …

## 7. 7. Bucles: for, while y recorrer colecciones
REPETICIÓN CONTROLADA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ FOR clásico (control total):   for (let i = 0; i < 5; i++) { console.log(i); }  FOR...OF (elementos de un array, EL RECOMENDAD…

## 8. 8. Funciones y arrow functions: el corazón de JS
FUNCIONES: HAY 3 SABORES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1. Declarada (con hoisting: puedes llamarla antes de definirla)   function sumar(a, b) { return a + b; }  2. Expresada   co…

## 9. 9. Arrays: la colección reina
ARRAYS: LISTAS ORDENADAS DE CUALQUIER COSA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   const numeros = [10, 20, 30];   numeros[0]         → 10   numeros.length     → 3  AGREGAR/QUITAR extrem…

## 10. 10. map, filter, reduce: programar sin bucles
EL TRÍO FUNCIONAL (ÚSALOS SIEMPRE QUE PUEDAS) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   const nums = [1, 2, 3, 4, 5];  MAP — transformar cada elemento (mismo largo):   nums.map(n => n * 10…

## 11. 11. Objetos: diccionarios con superpoderes
OBJETOS: CLAVE → VALOR ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   const alumno = {     nombre: "Ada",     edad: 36,     cursos: ["JS", "Python"],     saludar() { return `Hola, soy ${this.no…

## 12. 12. JSON: el idioma universal de los datos
JSON: DE TEXTO A DATOS Y VUELTA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ JSON (JavaScript Object Notation) es EL formato para mover datos entre sistemas: APIs, archivos, bases de datos.  SE…

## 13. 13. El DOM: convertir HTML en objeto vivo
DOM: EL HTML COMO OBJETOS MANIPULABLES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ El navegador convierte tu HTML en un árbol de objetos: el DOM. JS lo lee y lo MODIFICA en vivo.  SELECCIONAR …

## 14. 14. Eventos: la web reacciona
EVENTOS: LISTENERS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   const boton = document.querySelector("#agregar");   boton.addEventListener("click", () => {     console.log("¡Clickeaste!");   …

## 15. 15. Asincronía: setTimeout, promesas y async/await
ASINCRONÍA: NO BLOQUEAR LA FIESTA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ JS corre en un solo hilo. Las operaciones lentas (red, disco, timers) NO deben congelar la página. Solución: asinc…

## 16. 16. fetch: hablar con APIs del mundo
FETCH: CLIENTE DE APIS EN 10 LÍNEAS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ GET (leer):   const resp = await fetch("https://api.github.com/users/octocat");   if (!resp.ok) throw new Error(…

## 17. 17. Clases y módulos: código a escala
ESTRUCTURA CUANDO CRECE EL PROYECTO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ CLASES (plantillas de objetos con comportamiento)   class Tarea {     constructor(titulo) {       this.titulo = …

## 18. 18. Proyecto final: aplicación completa de tareas (DOM + eventos + JSON)
CONSTRUYE: GESTOR DE TAREAS COMPLETO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Todo el curso condensado en UNA app. Sin frameworks. Para tu portafolio.  MVP (versión mínima, 2 pomodoros) 1. …

---
✅ 18 lecciones · 📝 36 preguntas de repaso en quizzes_html/ · tests/