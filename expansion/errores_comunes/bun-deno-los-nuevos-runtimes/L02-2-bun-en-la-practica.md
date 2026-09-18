# ⚠️ Errores comunes — 2. Bun en la práctica

> 🍞 Bun & Deno — Los Nuevos Runtimes · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «npm test» → Frente a «¿Qué comando ejecuta los tests integrados de Bun?» lo fácil es confundirse. **Verdad**: bun test. bun test incluye runner con API estilo Jest (describe/test/expect), sin instalar nada.
- ❌ «bun check» → Frente a «¿Qué comando ejecuta los tests integrados de Bun?» lo fácil es confundirse. **Verdad**: bun test. bun test incluye runner con API estilo Jest (describe/test/expect), sin instalar nada.
- ❌ «Con http.createServer solamente» → Frente a «¿Cómo levanta Bun un servidor HTTP sin Express?» lo fácil es confundirse. **Verdad**: Con Bun.serve({ fetch }). Bun.serve es el servidor nativo de alto rendimiento con handlers fetch estándar Web.
- ❌ «Con nginx» → Frente a «¿Cómo levanta Bun un servidor HTTP sin Express?» lo fácil es confundirse. **Verdad**: Con Bun.serve({ fetch }). Bun.serve es el servidor nativo de alto rendimiento con handlers fetch estándar Web.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
