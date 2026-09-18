# ⚠️ Errores comunes — 3. Datos: fetch con caché, loading.tsx y error.tsx

> ▲ Next.js — El React Moderno · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Solo con useEffect» → Frente a «¿Cómo se cargan datos en un Server Component de Next.js?» lo fácil es confundirse. **Verdad**: Con await fetch directamente en el cuerpo async del componente. Al ejecutarse en el servidor, hacer await fetch en el componente es la vía natural y eficiente.
- ❌ «Únicamente desde una API externa» → Frente a «¿Cómo se cargan datos en un Server Component de Next.js?» lo fácil es confundirse. **Verdad**: Con await fetch directamente en el cuerpo async del componente. Al ejecutarse en el servidor, hacer await fetch en el componente es la vía natural y eficiente.
- ❌ «Bloquea la navegación» → Frente a «¿Para qué sirve loading.tsx en una ruta?» lo fácil es confundirse. **Verdad**: Muestra un fallback al instante mientras el segmento termina de cargar. Es un boundary de Suspense declarativo: el usuario ve esqueleto/UI de carga sin programarla.
- ❌ «Define la página 404» → Frente a «¿Para qué sirve loading.tsx en una ruta?» lo fácil es confundirse. **Verdad**: Muestra un fallback al instante mientras el segmento termina de cargar. Es un boundary de Suspense declarativo: el usuario ve esqueleto/UI de carga sin programarla.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
