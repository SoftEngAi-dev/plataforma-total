# ⚠️ Errores comunes — 2. Componentes Astro: props, slots y estilos con scope

> 🚀 Astro — La Web de Contenido Moderna · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «En el navegador del usuario» → Frente a «¿Dónde se ejecuta el código del frontmatter (---) de un componente Astro?» lo fácil es confundirse. **Verdad**: En el servidor o en build time. El frontmatter corre fuera del cliente; al navegador solo llega el HTML resultante.
- ❌ «En un Web Worker» → Frente a «¿Dónde se ejecuta el código del frontmatter (---) de un componente Astro?» lo fácil es confundirse. **Verdad**: En el servidor o en build time. El frontmatter corre fuera del cliente; al navegador solo llega el HTML resultante.
- ❌ «Siempre globales» → Frente a «¿Cómo aplica por defecto Astro las reglas de un <style> dentro de un componente?» lo fácil es confundirse. **Verdad**: Con scope automático solo a ese componente. Astro hashea las clases para que el estilo no se escape del componente.
- ❌ «Las ignora» → Frente a «¿Cómo aplica por defecto Astro las reglas de un <style> dentro de un componente?» lo fácil es confundirse. **Verdad**: Con scope automático solo a ese componente. Astro hashea las clases para que el estilo no se escape del componente.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
