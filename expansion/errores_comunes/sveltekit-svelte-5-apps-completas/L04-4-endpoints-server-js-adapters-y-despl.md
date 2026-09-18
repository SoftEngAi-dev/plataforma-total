# ⚠️ Errores comunes — 4. Endpoints +server.js, adapters y despliegue

> 🔥 SvelteKit & Svelte 5 — Apps Completas · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Con una carpeta /api de Next» → Frente a «¿Cómo creas un endpoint JSON en SvelteKit?» lo fácil es confundirse. **Verdad**: Con un archivo +server.js que exporta funciones GET/POST. +server.js en una ruta define handlers HTTP que devuelven json() personalizados.
- ❌ «Con localStorage» → Frente a «¿Cómo creas un endpoint JSON en SvelteKit?» lo fácil es confundirse. **Verdad**: Con un archivo +server.js que exporta funciones GET/POST. +server.js en una ruta define handlers HTTP que devuelven json() personalizados.
- ❌ «adapter-static» → Frente a «¿Qué adapter eliges para desplegar SvelteKit en tu propio contenedor Docker?» lo fácil es confundirse. **Verdad**: adapter-node. adapter-node genera un servidor Node independiente, perfecto para VPS o Docker.
- ❌ «adapter-auto» → Frente a «¿Qué adapter eliges para desplegar SvelteKit en tu propio contenedor Docker?» lo fácil es confundirse. **Verdad**: adapter-node. adapter-node genera un servidor Node independiente, perfecto para VPS o Docker.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
