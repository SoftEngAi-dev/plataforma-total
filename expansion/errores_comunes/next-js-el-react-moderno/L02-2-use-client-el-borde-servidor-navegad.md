# ⚠️ Errores comunes — 2. 'use client': el borde servidor/navegador

> ▲ Next.js — El React Moderno · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Hacer fetch de datos» → Frente a «¿Qué obliga escribir 'use client' al inicio de un componente?» lo fácil es confundirse. **Verdad**: Usar useState, useEffect o manejadores como onClick. Esas APIs son del navegador; sin la directiva el componente se trata como Server Component y falla.
- ❌ «Devolver JSX» → Frente a «¿Qué obliga escribir 'use client' al inicio de un componente?» lo fácil es confundirse. **Verdad**: Usar useState, useEffect o manejadores como onClick. Esas APIs son del navegador; sin la directiva el componente se trata como Server Component y falla.
- ❌ «En la raíz de toda la app» → Frente a «¿Dónde conviene ubicar la directiva 'use client' para optimizar el bundle?» lo fácil es confundirse. **Verdad**: En los componentes hoja interactivos, lo más abajo posible. Cuanto más abajo, menos JS viaja: el resto del árbol permanece como Server Components.
- ❌ «En todos los archivos por igual» → Frente a «¿Dónde conviene ubicar la directiva 'use client' para optimizar el bundle?» lo fácil es confundirse. **Verdad**: En los componentes hoja interactivos, lo más abajo posible. Cuanto más abajo, menos JS viaja: el resto del árbol permanece como Server Components.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
