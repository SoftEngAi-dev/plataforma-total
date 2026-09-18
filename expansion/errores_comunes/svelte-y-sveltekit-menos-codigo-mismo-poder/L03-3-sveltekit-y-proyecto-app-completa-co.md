# ⚠️ Errores comunes — 3. SvelteKit y proyecto: app completa con rutas

> Svelte y SvelteKit — Menos Código, Mismo Poder · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «CSS» → Frente a «¿Qué hace una función load en +page.server.js?» lo fácil es confundirse. **Verdad**: Corre en el SERVIDOR antes de renderizar y pasa datos a la página (SSR + SEO + sin flicker). Datos en el server, HTML listo al llegar: la app rápida y el SEO contento.
- ❌ «Es un test» → Frente a «¿Qué hace una función load en +page.server.js?» lo fácil es confundirse. **Verdad**: Corre en el SERVIDOR antes de renderizar y pasa datos a la página (SSR + SEO + sin flicker). Datos en el server, HTML listo al llegar: la app rápida y el SEO contento.
- ❌ «Ajax con JS» → Frente a «¿Qué es progressive enhancement con form actions?» lo fácil es confundirse. **Verdad**: El formulario funciona sin JavaScript (POST clásico del servidor, JS solo lo acelera cuando existe). Robustez por diseño: tu app no se rompe si falla/red no carga el bundle JS.
- ❌ «No funciona sin JS» → Frente a «¿Qué es progressive enhancement con form actions?» lo fácil es confundirse. **Verdad**: El formulario funciona sin JavaScript (POST clásico del servidor, JS solo lo acelera cuando existe). Robustez por diseño: tu app no se rompe si falla/red no carga el bundle JS.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
