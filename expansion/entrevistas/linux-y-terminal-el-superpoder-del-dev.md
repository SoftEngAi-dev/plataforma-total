# 🎤 Banco de entrevista — Linux y Terminal — El Superpoder del Dev

> 12 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué hace mkdir -p a/b/c?**
   - Crea la ruta completa incluidos padres intermedios sin error  _(Sin -p falla si 'a' no existe; con -p crea todo el camino.)_

2. **rm -r lo que hace peligroso es que...**
   - Linux NO tiene papelera: lo borrado por rm se fue (por eso rm -i o trash tools)  _(Cuidado con rm: la ruta / o comodines mal puestos borran todo sin preguntar.)_

3. **cat log | grep ERROR | wc -l hace...**
   - Cuenta las líneas del log que contienen ERROR (tuberías encadenadas)  _(Filtro → contador: las tuberías componen herramientas con texto crudo.)_

4. **¿Diferencia entre > y >>?**
   - > SOBRESCRIBE el archivo; >> AGREGA al final  _(Confundirlos = perder archivos (factor real de incidentes).)_

5. **chmod +x script.sh permite...**
   - Ejecutarlo directamente (bit de ejecución)  _(Sin +x lo corres como ./script.sh solo con bash script.sh; con +x directo.)_

6. **¿Cuándo usar kill -9?**
   - Solo cuando kill normal (SIGTERM) falla: -9 no deja limpiar al proceso  _(SIGTERM pide cortésmente cerrarse (guardar estado); SIGKILL lo aniquila sin aviso.)_

7. **¿Por qué llaves SSH en vez de contraseña?**
   - Criptografía asimétrica: la privada nunca viaja; contraseñas por red son atacables con fuerza bruta  _(La pública en el server + privada en tu máquina: imposible de robar por sniffing.)_

8. **rsync -avz a/ usuario@IP:~/b/ se usa para...**
   - Sincronizar carpetas remotas eficientemente (solo cambios, comprime, reanuda)  _(El caballo de batalla de backups y despliegues artesanales.)_

9. **¿Por qué siempre "comillas dobles" en variables de bash?**
   - Sin ellas, valores con espacios se rompen en múltiples argumentos (bugs y desastres)  _(rm $f → rm dos cosas si f="mi archivo.txt"; rm "$f" → correcto.)_

10. **set -euo pipefail permite...**
   - Fallar rápido y claramente: el script se detiene ante errores en vez de continuar roto  _(Script que sigue tras error suele causar más daño que uno que para.)_

11. **¿Qué ventaja tiene $fecha=$(date +%F) en el nombre del backup?**
   - Cada respaldo es distinto: nunca sobreescribes el de ayer  _(Backups fechados = historia de restauración; sin fecha solo tienes una copia.)_

12. **crontab -e + '0 21 * * * ./respaldo.sh' hace...**
   - Corre el respaldo automáticamente todos los días a las 21:00  _(cron = programador de tareas de Unix: tu computador trabaja mientras duermes.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Linux y Terminal y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Linux y Terminal con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
