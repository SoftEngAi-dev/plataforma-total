# ⚠️ Errores comunes — 5. Nuxt 3: Vue full-stack

> 💚 Vue 3 — Composition API en Serio · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «routes/» → Frente a «¿Qué carpeta de Nuxt genera las rutas automáticamente?» lo fácil es confundirse. **Verdad**: pages/. Cada .vue dentro de pages/ se convierte en ruta sin configurar ningún router.
- ❌ «views/» → Frente a «¿Qué carpeta de Nuxt genera las rutas automáticamente?» lo fácil es confundirse. **Verdad**: pages/. Cada .vue dentro de pages/ se convierte en ruta sin configurar ningún router.
- ❌ «en la carpeta pages/» → Frente a «¿Dónde defines endpoints de backend en Nuxt 3?» lo fácil es confundirse. **Verdad**: en server/api/. server/api/*.ts son endpoints Node del mismo proyecto, con despliegue integrado vía Nitro.
- ❌ «en un Express aparte obligatorio» → Frente a «¿Dónde defines endpoints de backend en Nuxt 3?» lo fácil es confundirse. **Verdad**: en server/api/. server/api/*.ts son endpoints Node del mismo proyecto, con despliegue integrado vía Nitro.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
