# ⚠️ Errores comunes — 4. Frameworks modernos y despliegue edge

> 🍞 Bun & Deno — Los Nuevos Runtimes · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Rails» → Frente a «¿Qué framework corre el MISMO código en Deno, Bun, Node y workers del edge?» lo fácil es confundirse. **Verdad**: Hono. Hono es ultraligero y multi-runtime: una API escrita una vez despliega en todos los runtimes.
- ❌ «Django» → Frente a «¿Qué framework corre el MISMO código en Deno, Bun, Node y workers del edge?» lo fácil es confundirse. **Verdad**: Hono. Hono es ultraligero y multi-runtime: una API escrita una vez despliega en todos los runtimes.
- ❌ «Un gestor de paquetes» → Frente a «¿Qué es Fresh?» lo fácil es confundirse. **Verdad**: El framework de islas para Deno, sin paso de build. Fresh aplica arquitectura de islas (como Astro) sobre Deno con Preact: cero build, súper rápido.
- ❌ «Un bundler» → Frente a «¿Qué es Fresh?» lo fácil es confundirse. **Verdad**: El framework de islas para Deno, sin paso de build. Fresh aplica arquitectura de islas (como Astro) sobre Deno con Preact: cero build, súper rápido.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
