# ⚠️ Errores comunes — 1. Node: sacar JS del navegador

> Node.js — JavaScript en el Servidor · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Un framework» → Frente a «¿Qué es Node.js?» lo fácil es confundirse. **Verdad**: Un runtime que ejecuta JS fuera del navegador (motor V8). Mismo motor V8 de Chrome, liberado para servidores y scripts.
- ❌ «Un editor» → Frente a «¿Qué es Node.js?» lo fácil es confundirse. **Verdad**: Un runtime que ejecuta JS fuera del navegador (motor V8). Mismo motor V8 de Chrome, liberado para servidores y scripts.
- ❌ «npm i esm» → Frente a «¿Cómo activar ES Modules (import/export) en Node?» lo fácil es confundirse. **Verdad**: "type": "module" en package.json (o usar .mjs). Con esa flag, import from 'node:fs/promises' y top-level await funcionan nativamente.
- ❌ «No se puede» → Frente a «¿Cómo activar ES Modules (import/export) en Node?» lo fácil es confundirse. **Verdad**: "type": "module" en package.json (o usar .mjs). Con esa flag, import from 'node:fs/promises' y top-level await funcionan nativamente.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
