# ⚡ Cheatsheet — 3. Signals: la nueva reactividad fina

> Angular — El Framework Empresarial Completo · Lección 3 · 18/09/2026

## 💡 Idea central
SIGNALS (Angular 16+): ESTADO SIMPLE, SIN ZONES

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué problema resuelven los signals respecto a Zone.js?** → Detección de cambios quirúrgica: solo se actualiza lo que usa el signal, sin escanear toda la app _(Rendimiento por reacción fina: ganancia real en apps grandes y código más claro.)_
- **Un computed() es...** → Un valor DERIVADO de signals que se recalcula automáticamente cuando cambian sus dependencias _(Estado derivado sin lógica manual: defines la relación, Angular mantiene el valor fresco.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
