# ⚠️ Errores comunes — 3. Los 5 errores clásicos de regex (no sufras estos)

> Expresiones Regulares — El Lenguaje de Patrones · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué arregla .*? frente a .*?» lo fácil es confundirse. **Verdad**: ? lo vuelve LAZY/no-greedy: captura el MÍNIMO posible en vez de todo lo posible. La diferencia entre 'primer cierre que encuentras' y 'último del documento': regex es codiciosa por defecto y se come todo.
- ❌ «Más rápido» → Frente a «¿Qué arregla .*? frente a .*?» lo fácil es confundirse. **Verdad**: ? lo vuelve LAZY/no-greedy: captura el MÍNIMO posible en vez de todo lo posible. La diferencia entre 'primer cierre que encuentras' y 'último del documento': regex es codiciosa por defecto y se come todo.
- ❌ «Siempre ideal» → Frente a «¿Cuándo NO usarías regex?» lo fácil es confundirse. **Verdad**: Para estructuras complejas anidadas como HTML/JSON reales: usa parseadores diseñados, regex se rompe en los bordes. Zawinski: 'ahora tienes dos problemas'. Texto libre ↔ regex; formato estructurado ↔ parser real.
- ❌ «Para logs» → Frente a «¿Cuándo NO usarías regex?» lo fácil es confundirse. **Verdad**: Para estructuras complejas anidadas como HTML/JSON reales: usa parseadores diseñados, regex se rompe en los bordes. Zawinski: 'ahora tienes dos problemas'. Texto libre ↔ regex; formato estructurado ↔ parser real.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
