# ⚠️ Errores comunes — 1. Regex en una lección: el 80% útil sin dolor

> Expresiones Regulares — El Lenguaje de Patrones · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Cualquier cosa» → Frente a «¿Qué captura \d{4}-\d{2}-\d{2}?» lo fácil es confundirse. **Verdad**: Formato fecha aproximado: 4 dígitos-guión-2 dígitos-guión-2 dígitos (2026-09-18). Las regex describen patrón → los números reales solo ilustran el formato esperado.
- ❌ «Emails» → Frente a «¿Qué captura \d{4}-\d{2}-\d{2}?» lo fácil es confundirse. **Verdad**: Formato fecha aproximado: 4 dígitos-guión-2 dígitos-guión-2 dígitos (2026-09-18). Las regex describen patrón → los números reales solo ilustran el formato esperado.
- ❌ «Trivia» → Frente a «¿Qué hacen \b y () en regex?» lo fácil es confundirse. **Verdad**: \b enmarca palabra completa ('cat' en 'concatenar' NO matchea con \bcat\b); () crea un GRUPO capturable. Límites y grupos: de patrones sueltos a coincidencias quirúrjicas.
- ❌ «Solo negación» → Frente a «¿Qué hacen \b y () en regex?» lo fácil es confundirse. **Verdad**: \b enmarca palabra completa ('cat' en 'concatenar' NO matchea con \bcat\b); () crea un GRUPO capturable. Límites y grupos: de patrones sueltos a coincidencias quirúrjicas.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
