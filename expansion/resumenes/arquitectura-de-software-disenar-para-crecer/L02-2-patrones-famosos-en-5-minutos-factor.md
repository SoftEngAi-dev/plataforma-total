# ⚡ Cheatsheet — 2. Patrones famosos en 5 minutos: Factory, Observer, Strategy, Singleton

> Arquitectura de Software — Diseñar para Crecer · Lección 2 · 18/09/2026

## 💡 Idea central
DECISIONES CLÁSICAS QUE CARGAN DE VIDA

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué resuelve Observer?** → Acoplamiento: el emisor publica eventos y los interesados reaccionan sin conocerse entre sí _(Desacopla módulos: agregar email-notification NO toca el módulo de compras.)_
- **¿Cuál antídoto a un if/elif gigante por tipo?** → Strategy/Polymorphism: cada caso es su propia clase/objeto elegida de un registro y llamada uniformemente _(Eliminas el switch monster; añadir un tipo nuevo es código NUEVO, no romper el viejo.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
