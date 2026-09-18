# 🎤 Banco de entrevista — Go — El Lenguaje de la Nube

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué ventaja especial tiene el build de Go?**
   - Genera UN binario nativo sin dependencias externas: el despliegue es copiar un archivo  _(Un solo ELF/EXE estático: las imágenes docker de Go pueden pesar 5MB.)_

2. **¿Qué hace := en Go?**
   - Declarar variable nueva con tipo INFERIDO (vs var x int explícita para el init)  _(x := 5 = declarar+inicializar inferido; var para declaraciones sin valor inicial.)_

3. **¿Por qué Go no tiene excepciones para errores esperables?**
   - Diseño deliberado: errores como valores devueltos obligan a manejarlos conscientemente y flujo de control visible  _(En Go el manejo de error no se esconde en catch lejanos: está cara a cara contigo.)_

4. **if err != nil es...**
   - El patrón universal de Go para comprobar y manejar errores devueltos por cada operación fallible  _(Todos los libros lo bromean, todos los proyectos sanos lo escriben sin pereza.)_

5. **¿Qué crea la palabra go delante de una llamada?**
   - Una goroutine: la función corre concurrentemente sin bloquear  _(go f() = paralelo livianísimo: miles concurrentes con MB de RAM, no GB.)_

6. **¿Para qué sirve un channel en Go?**
   - Comunicación tipada y segura entre goroutines: enviar/recibir datos sin locks manuales  _(channels = tubería sincronizada entre tareas concurrentes: el camino GOnativo.)_

7. **¿Qué incluye el paquete net/http de Go?**
   - Servidor HTTP completo en la stdlib: ninguna librería extra para APIs productivas  _(Escuchar y servir HTTP es nativo; por eso Go domina la nube sin framework pesado.)_

8. **¿Qué hace la struct tag `json:"titulo"`?**
   - Mapea el campo entre Go (Titulo) y JSON (titulo) al encodear/decodear automáticamente  _(Las tags gobiernan la serialización: la convención de nombre se configura explícita.)_

9. **¿Qué permite go build + cross-compilation?**
   - Un único binario estático por SO/arquitectura sin dependencias: deployment es 'copiar y correr'  _(produce.exe final: sin JVM/python en el server — eso lo aprecian mucho en operaciones.)_

10. **¿Por qué sync.RWMutex con la slice global en la API?**
   - Lecturas/escrituras concurrentes sobre memoria compartida pueden corromperse: el mutex las sincroniza  _(Varios requests golpean la misma estructura a la vez: sincronización obligatoria o data race.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Go y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Go con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
