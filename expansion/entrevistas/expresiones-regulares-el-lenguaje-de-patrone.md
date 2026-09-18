# 🎤 Banco de entrevista — Expresiones Regulares — El Lenguaje de Patrones

> 8 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué captura \d{4}-\d{2}-\d{2}?**
   - Formato fecha aproximado: 4 dígitos-guión-2 dígitos-guión-2 dígitos (2026-09-18)  _(Las regex describen patrón → los números reales solo ilustran el formato esperado.)_

2. **¿Qué hacen \b y () en regex?**
   - \b enmarca palabra completa ('cat' en 'concatenar' NO matchea con \bcat\b); () crea un GRUPO capturable  _(Límites y grupos: de patrones sueltos a coincidencias quirúrjicas.)_

3. **¿Qué hace (?P<nombre>...) en Python regex?**
   - Grupo NOMBRADO: extraes por m.group('nombre') en vez de factores posición brittle  _(Regex autocomentados: los nombres documentan cada parte que capturas.)_

4. **¿Qué logra el lookahead (?=.*[A-Z]) en la contraseña?**
   - VERIFICA sin consumir: exige que exista una mayúscula en lo que sigue sin avanzar el cursor  _(Lookaheads = 'debe cumplirse X adelante': validaciones compuestas sin complicar los grupos.)_

5. **¿Qué arregla .*? frente a .*?**
   - ? lo vuelve LAZY/no-greedy: captura el MÍNIMO posible en vez de todo lo posible  _(La diferencia entre 'primer cierre que encuentras' y 'último del documento': regex es codiciosa por defecto y se come todo.)_

6. **¿Cuándo NO usarías regex?**
   - Para estructuras complejas anidadas como HTML/JSON reales: usa parseadores diseñados, regex se rompe en los bordes  _(Zawinski: 'ahora tienes dos problemas'. Texto libre ↔ regex; formato estructurado ↔ parser real.)_

7. **¿Qué hace groupdict() sobre un Match?**
   - Devuelve un dictando con grupos NOMBRADOS para cada campo: linea→estructura lista para pandas/procesar  _(La puente: texto crudo → registro estructurado con nombres del grupo = pipeline real.)_

8. **¿Por qué probar tu regex en regex101 con muestras primero?**
   - Detectas backtracking/capturas raras/escapes al instante antes de correr sobre miliones de líneas y romper produción  _(Iteras el patrón en segundos con explicación en vivo; es la herramienta existente.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Expresiones Regulares y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Expresiones Regulares con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
