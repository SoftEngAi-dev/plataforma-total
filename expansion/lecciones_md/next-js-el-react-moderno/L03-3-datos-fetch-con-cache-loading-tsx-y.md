# 3. Datos: fetch con caché, loading.tsx y error.tsx

> 📚 Curso: **▲ Next.js — El React Moderno** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx

En un Server Component pides datos donde los pintas, sin useEffect:
    export default async function Noticias() {
      const res = await fetch("https://api.site.com/noticias",
                              { next: { revalidate: 60 } });  // ISR: 60 s
      const noticias = await res.json();
      return noticias.map(n => <Article key={n.id} {...n} />);
    }

Estrategias de caché de fetch:
   force-cache (por defecto en build)  → estático
   next: { revalidate: N }             → regenera cada N segundos (ISR)
   cache: "no-store"                   → siempre fresco (tiempo real)

UX gratis por convención:
  loading.tsx → se muestra al instante como fallback (Suspense implícito)
  error.tsx   → captura errores del segmento con botón "reintentar"
  generateStaticParams() → pre-genera rutas dinámicas en build

Adiós al spinners-everywhere: el HTML llega con datos; el streaming
envía lo listo primero y el resto cuando termina.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo se cargan datos en un Server Component de Next.js?
- A) Con await fetch directamente en el cuerpo async del componente
- B) Solo con useEffect
- C) Únicamente desde una API externa
- D) Con jQuery
### 2. ¿Para qué sirve loading.tsx en una ruta?
- A) Muestra un fallback al instante mientras el segmento termina de cargar
- B) Bloquea la navegación
- C) Define la página 404
- D) Minifica el JS

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Con await fetch directamente en el cuerpo async del componente — Al ejecutarse en el servidor, hacer await fetch en el componente es la vía natural y eficiente.
**2.** ✅ Muestra un fallback al instante mientras el segmento termina de cargar — Es un boundary de Suspense declarativo: el usuario ve esqueleto/UI de carga sin programarla.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
