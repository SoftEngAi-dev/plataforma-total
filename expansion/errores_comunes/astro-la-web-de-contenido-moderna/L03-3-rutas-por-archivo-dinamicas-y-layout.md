# ⚠️ Errores comunes — 3. Rutas por archivo, dinámicas y layouts

> 🚀 Astro — La Web de Contenido Moderna · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «next.config.js» → Frente a «¿Qué combinación crea rutas estáticas tipo /blog/mi-post en Astro?» lo fácil es confundirse. **Verdad**: src/pages/blog/[slug].astro + getStaticPaths. El [param].astro en src/pages + getStaticPaths enumera las rutas a generar en build.
- ❌ «un archivo routes.json» → Frente a «¿Qué combinación crea rutas estáticas tipo /blog/mi-post en Astro?» lo fácil es confundirse. **Verdad**: src/pages/blog/[slug].astro + getStaticPaths. El [param].astro en src/pages + getStaticPaths enumera las rutas a generar en build.
- ❌ «Optimizar imágenes» → Frente a «¿Para qué sirve un layout con <slot /> en Astro?» lo fácil es confundirse. **Verdad**: Envolver páginas repitiendo cabecera y pie, metiendo el contenido dentro. El layout aporta la estructura común y cada página inyecta su contenido en el slot.
- ❌ «Crear endpoints» → Frente a «¿Para qué sirve un layout con <slot /> en Astro?» lo fácil es confundirse. **Verdad**: Envolver páginas repitiendo cabecera y pie, metiendo el contenido dentro. El layout aporta la estructura común y cada página inyecta su contenido en el slot.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
