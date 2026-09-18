# 3. Ollama: tu LLM local en 3 comandos

> 📚 Curso: **IA Moderna y LLMs — Trabajar con Modelos Locales** · Lección 3 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
OLLAMA: MODELOS ABIERTOS EN TU MÁQUINA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSTALAR Y PRIMER MODELO
  1. ollama.com → instala (Linux/Mac/Win)
  2. ollama pull llama3.1:8b          (descarga ~5GB primero vez)
  3. ollama run llama3.1:8b           → ¡chat local funcionando offline!

SERVIDOR PARA APPS (como usa esta plataforma):
  ollama serve          → API local en localhost:11434
  curl localhost:11434/api/generate -d '{"model":"llama3.1:8b","prompt":"Hola"}'
  Ollama respeta API tipo OpenAI en /v1 → tus scripts existentes suelen compatir

MODELOS RECOMENDADOS POR CASO (2026, 8GB RAM+)
• Llama 3.1 8B      → mejor general de su clase
• Qwen 2.5 7B       → multilingüe fuertísimo + razonamiento
• Codellama/Qwen-code 7B → evaluar/ayudar código
• Mistral/Gemma pequeños → si tu RAM es limitada (3B corren en laptops modestos)

VENTAJAS LOCALES REALES: privacidad 100% (nada sale de tu PC) · gratis ilimitado · sin internet · aprendes APIs de verdad.
LIMITACIÓN: menos capaces que los gigantes cloud + lentos sin GPU — para el día a día de pruebas suficiente.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace ollama run llama3.1:8b?
- A) Borra algo
- B) Descarga (si falta) y abre un chat interactivo con el modelo en tu máquina local
- C) Edita código
- D) Minar
### 2. ¿Qué aporta ollama serve respecto a run?
- A) Nada
- B) Expone el modelo como API HTTP local (localhost:11434) para que TUS programas lo invoquen
- C) Transcription
- D) Un VPN

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Descarga (si falta) y abre un chat interactivo con el modelo en tu máquina local — Tu LLM privado corriendo offline a los 30 segundos de instalarlo.
**2.** ✅ Expone el modelo como API HTTP local (localhost:11434) para que TUS programas lo invoquen — El server convierte tu PC en un mini-OpenAI local: esta app misma le habla así.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
