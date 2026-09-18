# ⚠️ Errores comunes — 3. Ollama: tu LLM local en 3 comandos

> IA Moderna y LLMs — Trabajar con Modelos Locales · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Borra algo» → Frente a «¿Qué hace ollama run llama3.1:8b?» lo fácil es confundirse. **Verdad**: Descarga (si falta) y abre un chat interactivo con el modelo en tu máquina local. Tu LLM privado corriendo offline a los 30 segundos de instalarlo.
- ❌ «Edita código» → Frente a «¿Qué hace ollama run llama3.1:8b?» lo fácil es confundirse. **Verdad**: Descarga (si falta) y abre un chat interactivo con el modelo en tu máquina local. Tu LLM privado corriendo offline a los 30 segundos de instalarlo.
- ❌ «Nada» → Frente a «¿Qué aporta ollama serve respecto a run?» lo fácil es confundirse. **Verdad**: Expone el modelo como API HTTP local (localhost:11434) para que TUS programas lo invoquen. El server convierte tu PC en un mini-OpenAI local: esta app misma le habla así.
- ❌ «Transcription» → Frente a «¿Qué aporta ollama serve respecto a run?» lo fácil es confundirse. **Verdad**: Expone el modelo como API HTTP local (localhost:11434) para que TUS programas lo invoquen. El server convierte tu PC en un mini-OpenAI local: esta app misma le habla así.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
