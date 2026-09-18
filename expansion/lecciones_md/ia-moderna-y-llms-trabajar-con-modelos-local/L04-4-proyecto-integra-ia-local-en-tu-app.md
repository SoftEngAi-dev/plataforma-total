# 4. Proyecto: integra IA local en TU app

> 📚 Curso: **IA Moderna y LLMs — Trabajar con Modelos Locales** · Lección 4 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
CONSTRUYE: ASISTENTE DE ESTUDIO CON TU OLLAMA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
PYTHON PRÁCTICO (5 minutos de código útil):
  import requests
  def preguntar(pregunta, modelo="llama3.1:8b"):
      r = requests.post("http://localhost:11434/api/generate", json={
          "model": modelo,
          "prompt": f"Eres mentor de programación. Responde corto y con ejemplo.\n\nPregunta: {pregunta}",
          "stream": False,
      }, timeout=120)
      return r.json()["response"]
  print(preguntar("¿qué es un diccionario en Python?"))

PROYECTO COMPLETO (para tu portafolio):
1. lee un archivo de texto (tus apuntes de una materia)
2. parte el texto en trozos de ~500 palabras
3. para cada chunk: preguntar(f"Resume y genera UNA pregunta de examen sobre:\n{chunk}")
4. junta los resúmenes + las preguntas en UN solo manual-estudio markdown
5. salida: estudio.md con resumen por sección + quiz consolidado al final

VARIANTE PODEROSA (RAG mental): pegas documentación oficial como contexto al SYSTEM prompt y el modelo responde SOLO a partir de esos textos = menos alucinación (mismo principio que RAG profesional con embeddings).

REGLA PRO: temperature 0.2 para tareas de resumen/responder datos (consistencia), 0.8 para lluvia de ideas.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es RAG en términos de este proyecto?
- A) Un bug
- B) Proveer TUS documentos como contexto en el prompt para que el modelo responda sobre esa realidad, no se invente
- C) Un garbage collector
- D) Red local
### 2. ¿Qué temperature elegir para resumen fiel de documentos?
- A) 1.5
- B) Baja (~0.2): salida predecible y fiel; alta solo para creatividad/lluvia de ideas
- C) 100
- D) Ninguna

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Proveer TUS documentos como contexto en el prompt para que el modelo responda sobre esa realidad, no se invente — Retrieval + Generation: tu modelo responde anclado a fuentes reales que tú le das.
**2.** ✅ Baja (~0.2): salida predecible y fiel; alta solo para creatividad/lluvia de ideas — Temperatura baja = determinista; para hechos/resúmenes siempre frío.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
