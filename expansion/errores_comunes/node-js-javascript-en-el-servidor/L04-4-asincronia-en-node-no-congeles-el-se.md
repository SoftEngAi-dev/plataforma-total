# ⚠️ Errores comunes — 4. Asincronía en Node: no congeles el servidor

> Node.js — JavaScript en el Servidor · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Es más lento» → Frente a «¿Por qué prohibir readFileSync en un servidor (salvo arranque)?» lo fácil es confundirse. **Verdad**: Bloquea el único hilo de Node: TODOS los usuarios esperan. El event loop único detenido = servidor congelado para todos.
- ❌ «Está deprecado» → Frente a «¿Por qué prohibir readFileSync en un servidor (salvo arranque)?» lo fácil es confundirse. **Verdad**: Bloquea el único hilo de Node: TODOS los usuarios esperan. El event loop único detenido = servidor congelado para todos.
- ❌ «Por su nombre» → Frente a «¿Cómo reconoce Express un middleware de errores?» lo fácil es confundirse. **Verdad**: Tiene exactamente 4 parámetros (err, req, res, next). La firma de 4 argumentos es el contrato; se registra DESPUÉS de las rutas.
- ❌ «Está primero» → Frente a «¿Cómo reconoce Express un middleware de errores?» lo fácil es confundirse. **Verdad**: Tiene exactamente 4 parámetros (err, req, res, next). La firma de 4 argumentos es el contrato; se registra DESPUÉS de las rutas.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
