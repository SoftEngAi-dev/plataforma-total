# ⚠️ Errores comunes — 1. Por qué existen: más allá de Node

> 🍞 Bun & Deno — Los Nuevos Runtimes · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Una base de datos» → Frente a «¿Qué incluye Bun además del runtime?» lo fácil es confundirse. **Verdad**: Bundler, test runner y gestor de paquetes. Bun unifica herramientas: bun install, bun test y el bundler vienen de serie, todo muy rápido.
- ❌ «Un editor de código» → Frente a «¿Qué incluye Bun además del runtime?» lo fácil es confundirse. **Verdad**: Bundler, test runner y gestor de paquetes. Bun unifica herramientas: bun install, bun test y el bundler vienen de serie, todo muy rápido.
- ❌ «Ejecuta todo como root» → Frente a «¿Cuál es el principio de seguridad por defecto de Deno?» lo fácil es confundirse. **Verdad**: Permisos explícitos (--allow-net, --allow-read…). Sin --allow-* el código no puede salir de su caja de arena: ideal para scripts de terceros.
- ❌ «Bloquea la red para siempre» → Frente a «¿Cuál es el principio de seguridad por defecto de Deno?» lo fácil es confundirse. **Verdad**: Permisos explícitos (--allow-net, --allow-read…). Sin --allow-* el código no puede salir de su caja de arena: ideal para scripts de terceros.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
