# 🎤 Banco de entrevista — C y C++ — Los Cimientos del Software Moderno

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Por qué aprender C hoy si 'no lo usaré directo'?**
   - Es el substrato real: memoria, punteros y bajo nivel explican el comportamiento de TODOS los demás lenguajes actuales  _('Entender realmente' qué hace tu lenguaje favorito = haber pasado por C.)_

2. **¿Qué hace printf("%d", x)?**
   - Imprime valores donde %d es el placeholder de un entero (y %s string, %f float...)  _(String de formato con marcadores posicionales: el printf-family clásico.)_

3. **¿Qué significa *p cuando p es puntero?**
   - Seguir el puntero: LEER/ESCRIBIR el valor en esa dirección  _(* = dereferenciar; & = sacar dirección. Las dos caras de la memoria manual.)_

4. **¿Qué es una fuga de memoria (memory leak)?**
   - malloc sin free: la memoria reservada nunca se devuelve y el programa crece hasta morir  _(En C/GestiónManual: cada malloc necesita su free — por eso los lenguajes modernos tienen GC/ownership.)_

5. **¿Qué aporta vector<T> de la STL respecto a arrays C?**
   - Array dinámico gestionado: crece solo, sabe su tamaño, sin malloc/free manual  _(vector + string + sort + map = la STL: productividad C++, sin pelear malloc manual.)_

6. **¿Qué es RAII en C++?**
   - Adquisición/liberación de recursos ligada al ciclo de vida de objetos: scope-ended = recurso liberado (origen del modelo que perfecciona Rust)  _(Destructor al salir del bloque: no olvidas liberar; es la contra a los leaks/locks olvidados.)_

7. **¿Cuál es la diferencia .h vs .c en C?**
   - .h declara (interfaz pública) y .c define (implementación): separación contrato/código  _(El header es la 'API' del módulo; main lo incluye sin ver su implementación.)_

8. **¿Qué hace make con un Makefile bien escrito?**
   - Recompila SOLO los archivos cuyos fuentes cambiaron (build incremental con dependencias)  _(Dependencias+reglas: el build incremental nació aquí (todo build system actual lo hereda).)_

9. **¿Qué return values significan en main C?**
   - 0 = éxito; ≠0 = falló (la shell lo lee con $? — parte del protocolo Unix)  _(El exit code es como los programas 'hablan' entre sí en batch/pipes: vital en scripts.)_

10. **¿Por qué fclose(f) explícito importa en C?**
   - Sin cerrar, fopen queda abiertoy puede agotar file descriptors / corrupt data si escribías  _(C no tiene with/auto-cleanup: cada recurso abierto necesita su cierre deliberado.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve C y C++ y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta C y C++ con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
