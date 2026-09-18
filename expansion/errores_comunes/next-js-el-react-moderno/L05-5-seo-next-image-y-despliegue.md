# ⚠️ Errores comunes — 5. SEO, next/image y despliegue

> ▲ Next.js — El React Moderno · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Permite GIFs» → Frente a «¿Qué ventaja principal da next/image frente a una <img> normal?» lo fácil es confundirse. **Verdad**: Optimiza tamaño/formato y evita saltos de layout (CLS). Reserva el espacio, sirve webp/avif responsive y carga diferida: métricas Core Web Vitals sanas.
- ❌ «Sube la imagen a la nube» → Frente a «¿Qué ventaja principal da next/image frente a una <img> normal?» lo fácil es confundirse. **Verdad**: Optimiza tamaño/formato y evita saltos de layout (CLS). Reserva el espacio, sirve webp/avif responsive y carga diferida: métricas Core Web Vitals sanas.
- ❌ «Editando public/index.html» → Frente a «¿Cómo defines el <title> y la descripción de una página en el App Router?» lo fácil es confundirse. **Verdad**: export const metadata en page.tsx. metadata por segmento (objeto o generateMetadata async) alimenta <title>, meta y Open Graph.
- ❌ «Con useEffect» → Frente a «¿Cómo defines el <title> y la descripción de una página en el App Router?» lo fácil es confundirse. **Verdad**: export const metadata en page.tsx. metadata por segmento (objeto o generateMetadata async) alimenta <title>, meta y Open Graph.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
