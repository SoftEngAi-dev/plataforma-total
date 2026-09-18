# ⚠️ Errores comunes — 2. Prompts que funcionan: las 5 recetas

> IA Moderna y LLMs — Trabajar con Modelos Locales · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Gasta más» → Frente a «¿Por qué el few-shot (dar ejemplos input→output) mejora tanto?» lo fácil es confundirse. **Verdad**: El modelo imita el FORMATO Y EL PATRÓN de tus ejemplos en vez de adivinar. 2-3 ejemplos concretos enseñan estilo/estructura mejor que 10 instrucciones abstractas.
- ❌ «Es solo marketing» → Frente a «¿Por qué el few-shot (dar ejemplos input→output) mejora tanto?» lo fácil es confundirse. **Verdad**: El modelo imita el FORMATO Y EL PATRÓN de tus ejemplos en vez de adivinar. 2-3 ejemplos concretos enseñan estilo/estructura mejor que 10 instrucciones abstractas.
- ❌ «'no anda, fix'» → Frente a «¿Cuál prompt funciona mejor para debugging?» lo fácil es confundirse. **Verdad**: Pegar el código + el traceback completo + qué esperabas que pasara. Sin datos concretos el modelo adivina; con contexto real = respuesta de cirujano.
- ❌ «Un emoji» → Frente a «¿Cuál prompt funciona mejor para debugging?» lo fácil es confundirse. **Verdad**: Pegar el código + el traceback completo + qué esperabas que pasara. Sin datos concretos el modelo adivina; con contexto real = respuesta de cirujano.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
