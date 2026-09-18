# 6. Responsive design: una web para todos los tamaños

> 📚 Curso: **HTML y CSS — Diseño Web Total** · Lección 6 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```html
RESPONSIVE: MOBILE-FIRST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El 60% del tráfico web es móvil. Diseña desde la pantalla chica y escala hacia arriba.

LA LÍNEA OBLIGADA (sin ella el móvil muestra miniatura)
  <meta name="viewport" content="width=device-width, initial-scale=1">

MEDIA QUERIES
  /* Base: escrito para móvil (mobile-first) */
  @media (min-width: 768px) {       /* tablet+ */
    .contenedor { display: flex; }
  }
  @media (min-width: 1024px) {      /* desktop */ }

UNIDADES
• px → solo para bordes/detalle fino
• rem → tipografía/espacios (respeta configuración del usuario: accesibilidad)
• % / fr / vw → layout fluido
• max-width: 1100px + margin:auto → columna de lectura cómoda en pantallas gigantes

IMG responsive gratis: img { max-width: 100%; height: auto; }

TEST: herramientas de desarrollo del navegador (F12) → modo dispositivo. Prueba en 360px de ancho primero.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace la meta etiqueta viewport?
- A) Bloquea el zoom para siempre
- B) Dice al móvil que use el ancho real del dispositivo y no una miniatura
- C) Mejora el SEO
- D) Nada en móviles modernos
### 2. ¿Qué significa mobile-first?
- A) Que movil es más importante que desktop
- B) Escribir el CSS base para móvil y crecer con min-width media queries
- C) Testear solo en móvil
- D) Apps nativas primero

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Dice al móvil que use el ancho real del dispositivo y no una miniatura — Sin ella, el móvil renderiza como si fuera un desktop de 980px y escala.
**2.** ✅ Escribir el CSS base para móvil y crecer con min-width media queries — Base simple en pantalla chica; complejidad progresiva hacia pantallas grandes.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
