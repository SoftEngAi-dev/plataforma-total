# 2. 'use client': el borde servidor/navegador

> 📚 Curso: **▲ Next.js — El React Moderno** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx

Cuando necesitas interactividad (useState, useEffect, onClick, contexto,
librerías de terceros con eventos), marca el archivo:
    "use client";
    import { useState } from "react";
    export default function Buscador({ sugerencias }) {
      const [q, setQ] = useState("");
      return <input value={q} onChange={e => setQ(e.target.value)} />;
    }

Regla de oro: coloca el 'use client' LO MÁS ABAJO POSIBLE en el árbol
(hojas interactivas). La página sigue siendo Server Component, obtiene
datos y pasa props SERIALIZABLES (strings, números, JSON) a los clientes.

Ojo: un Client Component TAMBIÉN se pre-renderiza en el servidor en la
primera carga (html inicial rápido) y luego se hidrata. No es "solo
navegador"; es "servidor + interactividad posterior".

Patrón moderno: server para datos y estructura, client para botones,
formularios, animaciones y estado local.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué obliga escribir 'use client' al inicio de un componente?
- A) Usar useState, useEffect o manejadores como onClick
- B) Hacer fetch de datos
- C) Devolver JSX
- D) Exportar metadata
### 2. ¿Dónde conviene ubicar la directiva 'use client' para optimizar el bundle?
- A) En la raíz de toda la app
- B) En los componentes hoja interactivos, lo más abajo posible
- C) En todos los archivos por igual
- D) En el layout.tsx

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Usar useState, useEffect o manejadores como onClick — Esas APIs son del navegador; sin la directiva el componente se trata como Server Component y falla.
**2.** ✅ En los componentes hoja interactivos, lo más abajo posible — Cuanto más abajo, menos JS viaja: el resto del árbol permanece como Server Components.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
