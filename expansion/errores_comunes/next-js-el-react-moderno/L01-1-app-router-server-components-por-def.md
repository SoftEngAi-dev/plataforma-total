# ⚠️ Errores comunes — 1. App Router: Server Components por defecto

> ▲ Next.js — El React Moderno · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Un microservicio» → Frente a «¿Qué es un React Server Component en Next.js App Router?» lo fácil es confundirse. **Verdad**: Un componente que se renderiza en el servidor y no envía su JS al cliente. Corre en el servidor: puede usar async/await y recursos backend sin exponerlos al navegador.
- ❌ «Un Web Worker» → Frente a «¿Qué es un React Server Component en Next.js App Router?» lo fácil es confundirse. **Verdad**: Un componente que se renderiza en el servidor y no envía su JS al cliente. Corre en el servidor: puede usar async/await y recursos backend sin exponerlos al navegador.
- ❌ «pages/dashboard.tsx» → Frente a «¿Qué archivo crea la ruta /dashboard en el App Router?» lo fácil es confundirse. **Verdad**: app/dashboard/page.tsx. En app/, cada carpeta con page.tsx es una ruta; layouts y loading se anidan por segmento.
- ❌ «app/routes/dashboard.ts» → Frente a «¿Qué archivo crea la ruta /dashboard en el App Router?» lo fácil es confundirse. **Verdad**: app/dashboard/page.tsx. En app/, cada carpeta con page.tsx es una ruta; layouts y loading se anidan por segmento.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
