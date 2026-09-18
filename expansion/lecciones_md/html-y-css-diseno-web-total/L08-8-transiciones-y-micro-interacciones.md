# 8. Transiciones y micro-interacciones

> 📚 Curso: **HTML y CSS — Diseño Web Total** · Lección 8 de 10
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```html
MOVIMIENTO CON SENTIDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRANSICIONES — la base de todo movimiento suave:
  .tarjeta {
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .tarjeta:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
  }
Sin transition el cambio es brusco; con ella, se interpola.

ANIMACIONES (keyframes) para ciclos:
  @keyframes pulso { 50% { transform: scale(1.05); } }
  .logo { animation: pulso 2s infinite; }

REGLAS DEL MOVIMIENTO PROFESIONAL
1. Anima SOLO transform y opacity (no width/margin: provocan reflow lento)
2. Duraciones 150-300ms para UI — más lento se siente torpe
3. Movimiento = comunicación (hover, feedback, atención), no decoración
4. Respeta prefers-reduced-motion para accesibilidad:
   @media (prefers-reduced-motion: reduce) { * { animation: none; transition: none; } }
```

---

## 📝 Quiz de la lección

### 1. ¿Qué propiedades se deben animar para rendimiento fluido?
- A) width y height
- B) top y left
- C) transform y opacity
- D) margin y padding
### 2. ¿Qué duración se siente natural en micro-interacciones de UI?
- A) 2-3 segundos
- B) 150-300ms
- C) Lo máximo posible
- D) 10 segundos

---

## 🔑 Respuestas y explicaciones

**1.** ✅ transform y opacity — Solo esas dos no provocan reflow/repaint del layout: la GPU las acelera.
**2.** ✅ 150-300ms — Suficiente para percibirse, corto para no frenar.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
