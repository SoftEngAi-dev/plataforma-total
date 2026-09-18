# ⚠️ Errores comunes — 4. Proyecto: integra IA local en TU app

> IA Moderna y LLMs — Trabajar con Modelos Locales · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Un bug» → Frente a «¿Qué es RAG en términos de este proyecto?» lo fácil es confundirse. **Verdad**: Proveer TUS documentos como contexto en el prompt para que el modelo responda sobre esa realidad, no se invente. Retrieval + Generation: tu modelo responde anclado a fuentes reales que tú le das.
- ❌ «Un garbage collector» → Frente a «¿Qué es RAG en términos de este proyecto?» lo fácil es confundirse. **Verdad**: Proveer TUS documentos como contexto en el prompt para que el modelo responda sobre esa realidad, no se invente. Retrieval + Generation: tu modelo responde anclado a fuentes reales que tú le das.
- ❌ «1.5» → Frente a «¿Qué temperature elegir para resumen fiel de documentos?» lo fácil es confundirse. **Verdad**: Baja (~0.2): salida predecible y fiel; alta solo para creatividad/lluvia de ideas. Temperatura baja = determinista; para hechos/resúmenes siempre frío.
- ❌ «100» → Frente a «¿Qué temperature elegir para resumen fiel de documentos?» lo fácil es confundirse. **Verdad**: Baja (~0.2): salida predecible y fiel; alta solo para creatividad/lluvia de ideas. Temperatura baja = determinista; para hechos/resúmenes siempre frío.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
