# 2. Prompts que funcionan: las 5 recetas

> 📚 Curso: **IA Moderna y LLMs — Trabajar con Modelos Locales** · Lección 2 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
INGENIERÍA DE PROMPTS PARA DEVS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECETA 1 — ROL+CONTEXTO+TAREA+FORMATO
  "Eres un mentor senior de Python. Contexto: app Flask con errores 500.
   Tarea: explícame por qué este decorador rompe y dame el fix paso a paso.
   Formato: causa raíz (1 línea) + explicación + código corregido."
RECETA 2 — EJEMPLOS (few-shot)
  "Convierte a snake_case:
   MiVariable → mi_variable, OtroCoso → otro_coso,
   TuEntrada → "     → rellena perfecto aprendiendo del patrón
RECETA 3 — PENSAR EN VOZ ALTA (chain-of-thought)
  "Resuelve paso a paso y luego la respuesta final" → menos errores en lógica
RECETA 4 — RESTRICCIONES EXPLÍCITAS
  "Sin librerías externas. Máx 20 líneas. Español. Si no sabes, di que no sabes." ← clave anti-alucinación
RECETA 5 — ITERAR COMO CONVERSACIÓN (no como incantación)
  Pide → critica tú → "ese código usa eval: inseguro, reescribe con ast.literal_eval" → mejora y mejora.

PARA CÓDIGO: muestra el CÓDIGO, el ERROR completo y qué esperabas — nunca solo "no funciona" — pega el error real con contexto.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué el few-shot (dar ejemplos input→output) mejora tanto?
- A) Gasta más
- B) El modelo imita el FORMATO Y EL PATRÓN de tus ejemplos en vez de adivinar
- C) Es solo marketing
- D) Nada
### 2. ¿Cuál prompt funciona mejor para debugging?
- A) 'no anda, fix'
- B) Pegar el código + el traceback completo + qué esperabas que pasara
- C) Un emoji
- D) 'mágico'

---

## 🔑 Respuestas y explicaciones

**1.** ✅ El modelo imita el FORMATO Y EL PATRÓN de tus ejemplos en vez de adivinar — 2-3 ejemplos concretos enseñan estilo/estructura mejor que 10 instrucciones abstractas.
**2.** ✅ Pegar el código + el traceback completo + qué esperabas que pasara — Sin datos concretos el modelo adivina; con contexto real = respuesta de cirujano.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
