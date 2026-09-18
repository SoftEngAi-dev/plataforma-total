# ⚠️ Errores comunes — 12. JSON: el idioma universal de los datos

> JavaScript — De Cero a Experto · Lección 12 · Aprender de los errores (propios y ajenos)

- ❌ «Lee un archivo» → Frente a «¿Qué hace JSON.stringify(datos)?» lo fácil es confundirse. **Verdad**: Convierte datos JS en texto JSON para guardar/enviar. stringify serializa; parse deserializa. Juntas son el puente de datos.
- ❌ «Valida el JSON» → Frente a «¿Qué hace JSON.stringify(datos)?» lo fácil es confundirse. **Verdad**: Convierte datos JS en texto JSON para guardar/enviar. stringify serializa; parse deserializa. Juntas son el puente de datos.
- ❌ «Devuelve null» → Frente a «¿Qué pasa si JSON.parse recibe texto mal formado?» lo fácil es confundirse. **Verdad**: Lanza SyntaxError. parse es estricto — envuélvelo en try/catch en código serio.
- ❌ «Devuelve el texto igual» → Frente a «¿Qué pasa si JSON.parse recibe texto mal formado?» lo fácil es confundirse. **Verdad**: Lanza SyntaxError. parse es estricto — envuélvelo en try/catch en código serio.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
