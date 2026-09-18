# ⚠️ Errores comunes — 1. Islas: HTML primero, cero JS por defecto

> 🚀 Astro — La Web de Contenido Moderna · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Un enorme bundle de JavaScript» → Frente a «¿Qué envía Astro al navegador por defecto?» lo fácil es confundirse. **Verdad**: Solo HTML + CSS estático (cero JS). Esa es su superpotencia: HTML estático sin JS salvo que añadas islas interactivas.
- ❌ «WebAssembly» → Frente a «¿Qué envía Astro al navegador por defecto?» lo fácil es confundirse. **Verdad**: Solo HTML + CSS estático (cero JS). Esa es su superpotencia: HTML estático sin JS salvo que añadas islas interactivas.
- ❌ «Archivos del servidor» → Frente a «¿Qué son las <islas> de Astro?» lo fácil es confundirse. **Verdad**: Componentes interactivos que se hidratan de forma aislada. Una isla (con client:load/visible…) se hidrata sola: el resto de la página sigue siendo HTML estático.
- ❌ «Rutas dinámicas» → Frente a «¿Qué son las <islas> de Astro?» lo fácil es confundirse. **Verdad**: Componentes interactivos que se hidratan de forma aislada. Una isla (con client:load/visible…) se hidrata sola: el resto de la página sigue siendo HTML estático.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
