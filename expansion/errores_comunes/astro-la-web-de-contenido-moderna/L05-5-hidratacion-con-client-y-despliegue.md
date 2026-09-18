# ⚠️ Errores comunes — 5. Hidratación con client:* y despliegue

> 🚀 Astro — La Web de Contenido Moderna · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «client:load» → Frente a «¿Qué directiva hidrata una isla SOLO cuando el usuario la ve en pantalla?» lo fácil es confundirse. **Verdad**: client:visible. client:visible usa IntersectionObserver: cero coste hasta que la isla es visible.
- ❌ «client:only» → Frente a «¿Qué directiva hidrata una isla SOLO cuando el usuario la ve en pantalla?» lo fácil es confundirse. **Verdad**: client:visible. client:visible usa IntersectionObserver: cero coste hasta que la isla es visible.
- ❌ «Un ejecutable .exe» → Frente a «¿Qué produce `astro build` por defecto?» lo fácil es confundirse. **Verdad**: La carpeta dist/ estática lista para cualquier hosting. Salida 100% estática: la subes a cualquier CDN/hosting estático y vuela.
- ❌ «Un contenedor Docker» → Frente a «¿Qué produce `astro build` por defecto?» lo fácil es confundirse. **Verdad**: La carpeta dist/ estática lista para cualquier hosting. Salida 100% estática: la subes a cualquier CDN/hosting estático y vuela.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
