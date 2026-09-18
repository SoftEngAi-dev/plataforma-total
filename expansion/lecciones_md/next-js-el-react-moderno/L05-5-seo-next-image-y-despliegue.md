# 5. SEO, next/image y despliegue

> 📚 Curso: **▲ Next.js — El React Moderno** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx

SEO declarativo por página:
    export const metadata = {
      title: "Mi tienda — Inicio",
      description: "Todo en 24 h",
      openGraph: { images: ["/og.png"] },
    };
( o export async function generateMetadata({ params }) para dinámico ).

next/image optimiza sola: tamaño responsive, formato moderno (webp/avif),
lazy loading y SIN saltos de layout:
    import Image from "next/image";
    <Image src="/hero.jpg" alt="" width={1200} height={600} priority />

next/font carga fuentes sin CLS: import { Inter } from "next/font/google".

DESPLIEGUE:
  · Vercel: git push y listo (creadores de Next).
  · Self-host: next build && next start, o imagen Docker con output:
    "standalone".
  · middleware.ts: auth, redirects e i18n en el edge, antes de la ruta.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué ventaja principal da next/image frente a una <img> normal?
- A) Optimiza tamaño/formato y evita saltos de layout (CLS)
- B) Permite GIFs
- C) Sube la imagen a la nube
- D) Añade filtros Instagram
### 2. ¿Cómo defines el <title> y la descripción de una página en el App Router?
- A) export const metadata en page.tsx
- B) Editando public/index.html
- C) Con useEffect
- D) En el package.json

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Optimiza tamaño/formato y evita saltos de layout (CLS) — Reserva el espacio, sirve webp/avif responsive y carga diferida: métricas Core Web Vitals sanas.
**2.** ✅ export const metadata en page.tsx — metadata por segmento (objeto o generateMetadata async) alimenta <title>, meta y Open Graph.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
