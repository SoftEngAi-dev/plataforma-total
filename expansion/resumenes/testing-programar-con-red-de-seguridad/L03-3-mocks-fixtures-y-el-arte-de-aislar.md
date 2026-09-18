# ⚡ Cheatsheet — 3. Mocks, fixtures y el arte de aislar

> Testing — Programar con Red de Seguridad · Lección 3 · 18/09/2026

## 💡 Idea central
TEST DOBLE: TU LABORATORIO SIN SORPRESAS

## 🧠 Autoexamen (tápate la respuesta)
- **¿Cuándo usar mock?** → Cuando tu función llama a algo EXTERNO (red/BD/tiempo) y quieres probar solo tu lógica con respuestas controladas _(El mock convierte tu entorno en laboratorio: mismos datos, siempre, instantáneo.)_
- **¿Qué reutiliza una fixture de pytest?** → La preparación compartida entre muchos tests (datos de prueba, conexiones, objetos complejos) _(Fixture = DRY aplicado a tests: un usuario demo se define una vez y todos lo usan.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
