# 🎤 Banco de entrevista — IA Moderna y LLMs — Trabajar con Modelos Locales

> 8 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Cómo decide un LLM qué escribir?**
   - Es una función estadística entrenada en predecir el siguiente token según el contexto dado  _(Estadística aplicada al lenguaje: capacidades emergen, pero no hay comprensión consciente.)_

2. **¿Qué es 'alucinar' en un LLM?**
   - Generar información INVETNADA con alta confianza aparente (porque es probabilidad, no base de datos de hechos)  _(Por esto: todo dato factual importante generado por IA se VERIFICA en fuentes reales.)_

3. **¿Por qué el few-shot (dar ejemplos input→output) mejora tanto?**
   - El modelo imita el FORMATO Y EL PATRÓN de tus ejemplos en vez de adivinar  _(2-3 ejemplos concretos enseñan estilo/estructura mejor que 10 instrucciones abstractas.)_

4. **¿Cuál prompt funciona mejor para debugging?**
   - Pegar el código + el traceback completo + qué esperabas que pasara  _(Sin datos concretos el modelo adivina; con contexto real = respuesta de cirujano.)_

5. **¿Qué hace ollama run llama3.1:8b?**
   - Descarga (si falta) y abre un chat interactivo con el modelo en tu máquina local  _(Tu LLM privado corriendo offline a los 30 segundos de instalarlo.)_

6. **¿Qué aporta ollama serve respecto a run?**
   - Expone el modelo como API HTTP local (localhost:11434) para que TUS programas lo invoquen  _(El server convierte tu PC en un mini-OpenAI local: esta app misma le habla así.)_

7. **¿Qué es RAG en términos de este proyecto?**
   - Proveer TUS documentos como contexto en el prompt para que el modelo responda sobre esa realidad, no se invente  _(Retrieval + Generation: tu modelo responde anclado a fuentes reales que tú le das.)_

8. **¿Qué temperature elegir para resumen fiel de documentos?**
   - Baja (~0.2): salida predecible y fiel; alta solo para creatividad/lluvia de ideas  _(Temperatura baja = determinista; para hechos/resúmenes siempre frío.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve IA Moderna y LLMs y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta IA Moderna y LLMs con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
