# 6. Debugging: el arte de encontrar lo que rompiste

> 📚 Curso: **Herramientas del Desarrollador** · Lección 6 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
EL DEPURADOR Y LA CIENCIA DE LOS ERRORES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El debugging es 50% del trabajo real de un programador. Profesionalízate aquí y te separas del 90%.

NIVEL 1 — print/tutela científica
  print("LLEGUÉ AQUÍ", variable)   → y antes de eso: ¿CUÁL era mi hipótesis?
Método: hipótesis → experimento mínimo → resultado → nueva hipótesis.

NIVEL 2 — leer tracebacks DE ABAJO HACIA ARRIBA
  Traceback (most recent call last):
    File "x", line 10, in main ...   ← la ruta
  ZeroDivisionError: division by zero ← TIPO y MENSAJE: empezar aquí
El último frame tuyo suele ser tu código; el mensaje de error ES la pista.

NIVEL 3 — el debugger de verdad
  breakpoint()  (Python)  /  debugger;  (JS)
Controles: siguiente línea, entrar a función, inspeccionar variables, continuar.

REGLA: reproduce el error de forma CONFIABLE antes de intentar arreglarlo. Si no lo puedes reproducir, no entiendes el bug aún.
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo se lee un traceback?
- A) De arriba hacia abajo
- B) De abajo hacia arriba: tipo de error y mensaje primero
- C) Ignorando el mensaje
- D) Solo la primera línea
### 2. ¿Qué debe pasar ANTES de intentar arreglar un bug?
- A) Borrar el código
- B) Reproducir el error de forma confiable
- C) Pedir ayuda en foros
- D) Reescribir todo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ De abajo hacia arriba: tipo de error y mensaje primero — Tipo + mensaje (abajo) te dicen el qué; los frames (arriba) te dicen el dónde.
**2.** ✅ Reproducir el error de forma confiable — Sin reproducción confiable solo estás adivinando.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
