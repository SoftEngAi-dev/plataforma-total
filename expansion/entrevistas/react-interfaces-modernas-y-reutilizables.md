# 🎤 Banco de entrevista — React — Interfaces Modernas y Reutilizables

> 16 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué es JSX?**
   - Sintaxis que escribe HTML dentro de JS y llama funciones de React para construir el DOM  _(JSX describe la UI; Babel/Vite lo convierte en llamadas a funciones.)_

2. **¿Qué son las props?**
   - Los datos que un componente recibe de su padre (parámetros del componente)  _(Componente = función; props = sus argumentos. Comunicación de padre a hijo.)_

3. **¿Por qué setTareas([...tareas, nueva]) y no tareas.push(nueva)?**
   - React detecta cambios por REFERENCIA: hay que pasarle un array NUEVO o no re-renderiza  _(Inmutabilidad: nueva referencia = señal de re-render. push muta en silencio.)_

4. **¿Qué forma de actualización de estado es segura con valores previos?**
   - setCuenta(c => c + 1)  _(La forma funcional garantiza trabajar sobre el estado más reciente (clicks encolados).)_

5. **¿Qué prop requiere React al mapear elementos y por qué?**
   - key: identidad estable entre renders para emparejar el DOM correctamente  _(La key es DNI, no apellido: el índice del map cambia y traiciona con listas dinámicas.)_

6. **¿Cómo renderizar condicionalmente en JSX?**
   - Operador &&, ternario, o variable calculada ANTES del return  _(JSX admite expresiones, no sentencias: la lógica va en expresiones o antes del return.)_

7. **¿Qué significa input 'controlado'?**
   - Su value viene del estado y onChange lo actualiza: el estado es la fuente de verdad  _(Estado ↔ input en bucle controlado. React manda; el DOM obedece.)_

8. **¿Cómo sabe el hijo que debe agregar una tarea si el estado está arriba?**
   - Llama a una función que el padre le pasó por props (onAgregar)  _(Datos bajan por props; cambios suben ejecutando callbacks que bajaron por props.)_

9. **¿Cuándo se ejecuta useEffect(fn, [])?**
   - Una vez al montar el componente  _(Array vacío = sin dependencias: solo el montaje. La limpieza corre al desmontar.)_

10. **¿Para qué sirve la función de limpieza del efecto?**
   - Cancelar trabajo pendiente (fetch, timers, subscripciones) antes de re-ejecutar o desmontar  _(Evita race conditions y fugas: la respuesta tardía de un fetch viejo no pisa la nueva.)_

11. **¿Cuándo llegar a Context?**
   - Cuando muchos componentes a mucha profundidad necesitan el mismo dato (tema, usuario, idioma)  _(Context resuelve prop-drilling global; estado local y composición resuelven la mayoría de los casos.)_

12. **¿Qué reglas tienen los hooks (useState, useEffect, customs)?**
   - Top-level del componente, sin loops/ifs, nombres use*  _(El orden fijo de llamadas es cómo React empareja hook con celda de estado: romperlo = caos.)_

13. **¿Qué 3 estados mínimos modelan cualquier fetch en UI?**
   - cargando, error, datos  _(Con esos tres discriminas exáctamente qué pintar: spinner, mensaje de error o contenido.)_

14. **¿Por qué la bandera 'cancelado' en el efecto de fetch?**
   - Evita que una respuesta tardía actualice estado de un componente desmontado (warning + race)  _(En StrictMode y navegación rápida los componentes se montan/desmontan: la guardia lo hace robusto.)_

15. **¿Cómo editar una nota inmutablemente en un array de estado?**
   - map que devuelve objeto nuevo {...n, texto: x} solo para el id coincidente  _(map con spread: reemplazas el objeto con uno NUEVO; referencias nuevas → React entiende y la UI se actualiza.)_

16. **¿Qué dos APIs persisten las notas en esta app?**
   - useState + useEffect dentro de un custom hook useLocalStorage  _(Estado + efecto que escribe a localStorage: patrón simple, potente y reutilizable.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve React y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta React con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
