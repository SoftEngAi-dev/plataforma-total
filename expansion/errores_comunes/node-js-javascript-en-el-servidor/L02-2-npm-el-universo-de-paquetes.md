# ⚠️ Errores comunes — 2. npm: el universo de paquetes

> Node.js — JavaScript en el Servidor · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Porque es secreto» → Frente a «¿Por qué node_modules NUNCA va a git?» lo fácil es confundirse. **Verdad**: Es enorme y reproducible: package.json + package-lock permiten recrearlo con npm install. El manifiesto viaja; el contenido se instala. Así mantienen repos livianos TODOS los equipos.
- ❌ «Por licencias» → Frente a «¿Por qué node_modules NUNCA va a git?» lo fácil es confundirse. **Verdad**: Es enorme y reproducible: package.json + package-lock permiten recrearlo con npm install. El manifiesto viaja; el contenido se instala. Así mantienen repos livianos TODOS los equipos.
- ❌ «Exactamente 4.19.2» → Frente a «¿Qué significa "express": "^4.19.2"?» lo fácil es confundirse. **Verdad**: Cualquier versión 4.x.x compatible desde 4.19.2. ^ permite parches y menores compatibles; el lock file congela la realidad exacta.
- ❌ «Mayor a 5» → Frente a «¿Qué significa "express": "^4.19.2"?» lo fácil es confundirse. **Verdad**: Cualquier versión 4.x.x compatible desde 4.19.2. ^ permite parches y menores compatibles; el lock file congela la realidad exacta.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
