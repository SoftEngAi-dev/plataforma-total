# 1. LLMs bajo el capó (en 10 frases)

> 📚 Curso: **IA Moderna y LLMs — Trabajar con Modelos Locales** · Lección 1 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
QUÉ ES REALMENTE UN LLM (SIN MAGIA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Un LLM es una función estadística GIGANTE entrenada para predecir el siguiente token (pedazo de palabra) dado el contexto.
2. Esa simpleza + miles de millones de textos → emergen capacidades: resumir, escribir código, traducir...
3. NO es consciente ni "entiende": genera texto PLAUSIBLE según patrones. Alucinar = inventar con confianza estadística.
4. Contexto = tu prompt + historial (limitado: la ventana de contexto). Lo que está ahí, lo ve; lo que no, no.
5. Temperature: 0 = determinista/preciso; 1+ = más creativo/azaroso.
6. Tokens: cobranse por tokens (~0.75 palabra cada uno en general); modelos grandes = más capaces, más caros/lentos.
7. Correr LOCAL vs CLOUD: Ollama/cor en tu máquina = privado/gratis/offline pero modelos más chicos; APIs (OpenAI etc) = más capaces pero tus datos salen.
8. SYSTEM PROMPT: instrucciones permanentes que configuran al modelo por conversación (esta app lo usa: "responde corto en español").
9. Few-shot: dar 2-3 ejemplos de entrada→salida en el prompt = MUCHO mejor salida (el modelo copia tu formato).
10. La IA amplifica: un experto con IA = cohete; quien no entiende el tema no puede AUDITAR la salida. Por eso primero dominas tú.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo decide un LLM qué escribir?
- A) Pensando
- B) Es una función estadística entrenada en predecir el siguiente token según el contexto dado
- C) Buscando en su base exacta
- D) Debatiendo consigo
### 2. ¿Qué es 'alucinar' en un LLM?
- A) Dormir
- B) Generar información INVETNADA con alta confianza aparente (porque es probabilidad, no base de datos de hechos)
- C) Crashear
- D) Traducir

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Es una función estadística entrenada en predecir el siguiente token según el contexto dado — Estadística aplicada al lenguaje: capacidades emergen, pero no hay comprensión consciente.
**2.** ✅ Generar información INVETNADA con alta confianza aparente (porque es probabilidad, no base de datos de hechos) — Por esto: todo dato factual importante generado por IA se VERIFICA en fuentes reales.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
