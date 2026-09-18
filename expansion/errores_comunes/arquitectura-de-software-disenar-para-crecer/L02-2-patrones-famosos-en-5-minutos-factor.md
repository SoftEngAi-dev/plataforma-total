# ⚠️ Errores comunes — 2. Patrones famosos en 5 minutos: Factory, Observer, Strategy, Singleton

> Arquitectura de Software — Diseñar para Crecer · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Visualización» → Frente a «¿Qué resuelve Observer?» lo fácil es confundirse. **Verdad**: Acoplamiento: el emisor publica eventos y los interesados reaccionan sin conocerse entre sí. Desacopla módulos: agregar email-notification NO toca el módulo de compras.
- ❌ «Bases de datos» → Frente a «¿Qué resuelve Observer?» lo fácil es confundirse. **Verdad**: Acoplamiento: el emisor publica eventos y los interesados reaccionan sin conocerse entre sí. Desacopla módulos: agregar email-notification NO toca el módulo de compras.
- ❌ «más ifs» → Frente a «¿Cuál antídoto a un if/elif gigante por tipo?» lo fácil es confundirse. **Verdad**: Strategy/Polymorphism: cada caso es su propia clase/objeto elegida de un registro y llamada uniformemente. Eliminas el switch monster; añadir un tipo nuevo es código NUEVO, no romper el viejo.
- ❌ «comentarios» → Frente a «¿Cuál antídoto a un if/elif gigante por tipo?» lo fácil es confundirse. **Verdad**: Strategy/Polymorphism: cada caso es su propia clase/objeto elegida de un registro y llamada uniformemente. Eliminas el switch monster; añadir un tipo nuevo es código NUEVO, no romper el viejo.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
