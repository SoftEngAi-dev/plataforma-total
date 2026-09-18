# ⚡ Cheatsheet — 3. Tests automáticos: el corazón del CI

> DevOps y CI/CD — De Tu PC a Producción Sin Sudor · Lección 3 · 18/09/2026

## 💡 Idea central
SIN TESTS NO HAY CI REAL

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué la pirámide tiene más tests unitarios que E2E?** → Unitarios = rápidos, estables y baratos; E2E = lentos, frágiles y caros (manténlos pocos) _(La base ancha de unit tests cubre lógica; los pocos E2E verifican el cableado.)_
- **¿Qué debe evitar un test unitario?** → Tocar red/BD/reloj reales (úsese mocks/fakes) para ser rápido, repetible y confiable _(Un test que depende del internet es un test que fallará a las 3am cuando menos lo esperas.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
