# 4. Flexbox: layout en una dimensión

> 📚 Curso: **HTML y CSS — Diseño Web Total** · Lección 4 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```html
FLEXBOX: ALINEAR COSAS FÁCIL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  .contenedor {
    display: flex;
    justify-content: center;   /* eje principal (horizontal por defecto) */
    align-items: center;       /* eje cruzado (vertical) */
    gap: 12px;                 /* espacio entre hijos */
  }

PROPIEDADES DEL PADRE (flex container)
• justify-content: flex-start | center | space-between | space-around
• align-items: stretch | center | flex-start | flex-end
• flex-direction: row | column        ← invierte los ejes
• flex-wrap: wrap                      ← permite varias líneas

PROPIEDADES DEL HIJO
• flex: 1            → "crece y reparte el espacio sobrante"
• align-self: ...    → excepción individual

LOS 3 CASOS DE LA VIDA REAL
1. Barra de navegación: space-between + align center
2. Centrar algo perfecto (vertical y horizontal): ambas a center
3. Cards uniformes: wrap + flex:1 en cada una

PRÁCTICA: centra un div con flexbox. Hoy. Es EL examen de CSS doméstico.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué línea centra un elemento horizontal y verticalmente dentro de su padre?
- A) display:block + margin:0
- B) display:flex; justify-content:center; align-items:center
- C) position:center
- D) float:center
### 2. ¿Qué hace flex: 1 en un hijo?
- A) Le da 1px
- B) Lo hace crecer para repartir el espacio sobrante del contenedor
- C) Lo pone primero
- D) Lo oculta

---

## 🔑 Respuestas y explicaciones

**1.** ✅ display:flex; justify-content:center; align-items:center — Flexbox con ambos ejes centrados — el centramiento perfecto ya no es chiste.
**2.** ✅ Lo hace crecer para repartir el espacio sobrante del contenedor — flex-grow/shrink/basis abreviado: típicamente reparte el espacio equitativamente.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
