# 🎤 Banco de entrevista — Git y GitHub — Tu Historia Nunca Se Pierde

> 12 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué es un commit en git?**
   - Un snapshot completo del proyecto con puntero al commit padre  _(Cada commit = foto completa; git las deduplica internamente (objetos).)_

2. **¿Cuál es el orden del flujo básico?**
   - editar → git add → git commit  _(Working → staging (add) → repo (commit). push va aparte al remoto.)_

3. **¿Qué es un merge conflict?**
   - Dos ramas editaron las mismas líneas: git te pide elegir manualmente entre marcadores <<<<  _(Los conflictos son decisiones pendientes, no errores: resuelves, add, commit.)_

4. **¿Por qué ramas cortas de 1-3 días?**
   - Cambios pequeños = conflictos raros y merges simples; la rama eterna deviene imposible de integrar  _(La integración continua empieza por ramas efímeras.)_

5. **git revert vs git reset — ¿cuál es seguro en commits compartidos?**
   - revert (crea commit inverso sin reescribir la historia ya publicada)  _(Reescribir historia compartida rompe a tus compañeros; revert es la forma polite.)_

6. **git stash sirve para...**
   - Apartar cambios sin commit y retomarlos luego (stash pop)  _(El cajón rápido: limpio el área, atiendo la urgencia, recupero lo mío.)_

7. **¿Cuál es el ciclo correcto de contribución?**
   - rama → commits → push → PR → revisión → merge  _(El PR con revisión es el corazón del trabajo en equipo moderno.)_

8. **¿Cuándo necesitas hacer fork?**
   - Cuando el repo no es tuyo/no tienes permiso de push (open source)  _(Fork = tu copia en tu cuenta, que permite proponer PR al original.)_

9. **¿Por qué .env va al .gitignore SIEMPRE?**
   - Contiene secretos (claves, tokens) que jamás deben quedar en la historia pública  _(Un secreto subido = filtrado para siempre, aunque lo borres después: hay que rotar la credencial.)_

10. **¿Qué es un tag v1.0 en git?**
   - Una marca permanente sobre un commit: la forma de publicar releases/versiones  _(Los tags señalan hitos estables; son referencia para despliegues.)_

11. **¿Qué hace `git pull` tras hacer merge del PR en la web?**
   - Trae e integra los cambios del remoto a tu rama local  _(La web integró tu PR; tu main local está vieja hasta que pullas.)_

12. **¿Por qué practicar un conflicto a posta?**
   - Ver los marcadores <<< y resolverlo a mano desmistifica el conflicto real futuro  _(El conflicto es mero texto a decidir: el miedo se cura con práctica.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Git y GitHub y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Git y GitHub con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
