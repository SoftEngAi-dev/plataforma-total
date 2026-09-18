# 📕 Resumen maestro — ▲ Next.js — El React Moderno

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. App Router: Server Components por defecto
 Next.js 14/15 con APP ROUTER cambia las reglas: en la carpeta app/, TODOS los componentes son REACT SERVER COMPONENTS salvo que digas lo contrario. Eso significa:   · Se ejecutan …

## 2. 2. 'use client': el borde servidor/navegador
 Cuando necesitas interactividad (useState, useEffect, onClick, contexto, librerías de terceros con eventos), marca el archivo:     "use client";     import { useState } from "reac…

## 3. 3. Datos: fetch con caché, loading.tsx y error.tsx
 En un Server Component pides datos donde los pintas, sin useEffect:     export default async function Noticias() {       const res = await fetch("https://api.site.com/noticias",  …

## 4. 4. Server Actions: mutaciones sin escribir APIs
 Las SERVER ACTIONS son funciones del servidor llamables desde la UI:     // app/actions.ts     "use server";     import { revalidatePath } from "next/cache";     import { z } from…

## 5. 5. SEO, next/image y despliegue
 SEO declarativo por página:     export const metadata = {       title: "Mi tienda — Inicio",       description: "Todo en 24 h",       openGraph: { images: ["/og.png"] },     }; ( …

---
✅ 5 lecciones · 📝 10 preguntas de repaso en quizzes_html/ · tests/