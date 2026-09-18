# 🎤 Banco de entrevista — JavaScript — De Cero a Experto

> 36 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Dónde corre JavaScript hoy día?**
   - Navegadores, servidores, móviles, desktops y más  _(Con Node y sus derivados, JS es verdaderamente universal.)_

2. **¿Qué imprime en la consola del navegador?**
   - console.log()  _(console.log es el print de JavaScript — tu aliado n.º 1.)_

3. **¿Cuál es la regla moderna para declarar variables?**
   - const por defecto; let solo si reasignas; var nunca  _(const comunica 'esto no cambia': menos sorpresas, bugs más difíciles.)_

4. **¿Qué pasa con const arr = [1]; arr.push(2)?**
   - Funciona: const prohíbe reasignar, no mutar el contenido  _(const congela la REFERENCIA, no el objeto: puedes mutar por dentro.)_

5. **¿Por qué usar === y no ==?**
   - == convierte tipos automáticamente y genera bugs sutiles; === compara valor y tipo  _("5" == 5 da true; con === da false. Predicibilidad > comodidad.)_

6. **¿Qué valor representa la ausencia intencional?**
   - null  _(null = 'vacío a propósito'; undefined = 'aún no se le asignó nada'.)_

7. **¿Qué es una plantilla literal?**
   - Backticks con ${} para interpolar variables/expresiones  _(`Hola ${nombre}` — la forma moderna de construir texto dinámico.)_

8. **Tras let s="hola"; s.toUpperCase(); ¿qué vale s?**
   - "hola" — los strings son inmutables  _(toUpperCase devuelve un NUEVO string; s no cambia salvo que lo reasignes.)_

9. **¿Por qué 0.1 + 0.2 !== 0.3 en JS (y casi todo lenguaje)?**
   - Representación binaria de punto flotante: 0.1 y 0.2 no son exactos en base 2  _(Como 1/3 en decimal, algunos decimales son infinitos en binario. Solución: enteros (centavos) o toFixed.)_

10. **¿Cómo generar un entero aleatorio entre 1 y 6?**
   - Math.floor(Math.random() * 6) + 1  _(random()*6 ∈ [0,6); floor → 0-5; +1 → dado de 1 a 6.)_

11. **¿Cuáles valores son falsy en JS?**
   - false, 0, "", null, undefined, NaN  _(if(x) con x falsy no ejecuta el bloque — revisa esta lista cuando te sorprenda.)_

12. **¿Qué hace nombre ?? "invitado"?**
   - Usa "invitado" SOLO si nombre es null o undefined (no si es "" o 0)  _(?? es el default preciso: || también rechazaría '' y 0 que podrías querer conservar.)_

13. **¿Cuál es la forma moderna recomendada de recorrer un array?**
   - for...of  _(for...of es directo y seguro; for...in es para CLAVES de objetos, no arrays.)_

14. **¿Qué hace continue?**
   - Salta a la siguiente iteración  _(Omite el resto del bloque en esta vuelta y sigue con la próxima.)_

15. **¿Qué devuelve una función sin return?**
   - undefined  _(Sin return explícito, toda función JS devuelve undefined.)_

16. **¿Qué diferencia clave tiene una arrow function?**
   - No tiene su propio this: usa el del contexto que la rodea  _(Crucial en callbacks y objetos: la arrow no 'secuestra' el this como hace function.)_

17. **¿Qué métodos agregan/quitan AL FINAL de un array?**
   - push/pop  _(push y pop operan en el extremo final; shift/unshift al inicio.)_

18. **const b = a (arrays) — ¿qué relación tienen?**
   - Apuntan AL MISMO array: mutar uno muta el otro  _(Los arrays son referencias. Copia real: [...a] o a.slice().)_

19. **¿Qué devuelve [2,4,6].filter(n => n > 3)?**
   - [4, 6]  _(filter conserva los que cumplen la condición.)_

20. **¿Qué hace el segundo argumento de reduce?**
   - Es el valor inicial del acumulador  _(Sin valor inicial, reduce usa el primer elemento — que a veces es sorpresa. Escribe siempre el inicial.)_

21. **¿Qué hace const { nombre } = alumno?**
   - Extrae alumno.nombre en una variable llamada nombre (destructuring)  _(Destructuring: la forma idiomática de extraer propiedades en JS moderno.)_

22. **¿Cuándo usar alumno["nombre"] en vez de alumno.nombre?**
   - Cuando la clave viene de una variable o tiene espacios  _(Los corchetes aceptan expresiones: alumno[variable] resuelve la clave dinámicamente.)_

23. **¿Qué hace JSON.stringify(datos)?**
   - Convierte datos JS en texto JSON para guardar/enviar  _(stringify serializa; parse deserializa. Juntas son el puente de datos.)_

24. **¿Qué pasa si JSON.parse recibe texto mal formado?**
   - Lanza SyntaxError  _(parse es estricto — envuélvelo en try/catch en código serio.)_

25. **¿Qué método es seguro para insertar TEXTO de usuario en la página?**
   - textContent  _(textContent no interpreta HTML: protege contra inyección XSS básica.)_

26. **¿Qué hace el.classList.toggle('activa')?**
   - La añade si no está, la quita si está  _(Toggle = interruptor: perfecto para menús, modos oscuro/claro, etc.)_

27. **¿Por qué e.preventDefault() en el submit de un formulario?**
   - Evita que el navegador recargue la página para procesarlo con JS  _(Sin preventDefault, el formulario navega/recarga y tu lógica JS no corre.)_

28. **¿Qué es delegación de eventos?**
   - Un solo listener en el padre que reacciona según e.target  _(Clave para contenido dinámico: los hijos futuros también funcionan.)_

29. **¿Qué devuelve inmediatamente una función async?**
   - Una promesa  _(async significa 'esto devolverá una promesa'; await desenvuelve su valor.)_

30. **¿Para qué sirve Promise.all?**
   - Esperar varias promesas EN PARALELO y continuar cuando todas terminan  _(Paralelismo de verdad: si son independientes, esperar juntas = mitad del tiempo.)_

31. **¿Cuándo rechaza fetch (lanza error) SIN ayuda tuya?**
   - Solo en errores de red (sin conexión, CORS, DNS)  _(Por eso el patrón: chequear resp.ok y lanzar tu propio error en 4xx/5xx.)_

32. **¿Qué header obliga al enviar JSON con POST?**
   - Content-Type: application/json  _(Sin ese header, muchos servidores no interpretan el body como JSON.)_

33. **¿Qué hace export default frente a export nombrado?**
   - Un solo default por archivo, se importa sin llaves; los nombrados van con llaves exactas  _(import X from... (default) vs import { x } from... (nombrados).)_

34. **¿Qué hace super.completar() en una subclase?**
   - Invoca la versión del método en la clase padre  _(super = acceso a la clase padre: reutilizas y extiendes en vez de reescribir.)_

35. **¿Qué dos llamadas sincronizan la app con localStorage?**
   - parse y stringify de JSON  _(stringify al guardar, parse al cargar: JSON es el puente.)_

36. **¿Por qué delegación de eventos en la lista en vez de listener por li?**
   - Los li se recrean en cada render; un solo listener en el ul sigue funcionando siempre  _(Contenido dinámico = listener en el padre estable, acción según e.target.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve JavaScript y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta JavaScript con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
