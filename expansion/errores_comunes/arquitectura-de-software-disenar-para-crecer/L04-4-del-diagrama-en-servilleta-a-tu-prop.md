# ⚠️ Errores comunes — 4. Del diagrama en servilleta a tu propia arquitectura

> Arquitectura de Software — Diseñar para Crecer · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Código corto» → Frente a «¿Qué ley cumple una buena separación en capas?» lo fácil es confundirse. **Verdad**: Las capas INTERNAS (dominio) no conocen las EXTERNAS (web/DB): lo externo se acopla HACIA el negocio, jamás al revés. Invertir la dirección de dependencia = tu lógica de negocio es testeable pura y viva en cualquier envoltorio.
- ❌ «Más archivos = mejor» → Frente a «¿Qué ley cumple una buena separación en capas?» lo fácil es confundirse. **Verdad**: Las capas INTERNAS (dominio) no conocen las EXTERNAS (web/DB): lo externo se acopla HACIA el negocio, jamás al revés. Invertir la dirección de dependencia = tu lógica de negocio es testeable pura y viva en cualquier envoltorio.
- ❌ «Un SQL» → Frente a «Un 'caso de uso' (application service) es...» lo fácil es confundirse. **Verdad**: La orquestación de un objetivo de negocio: 'CrearTarea' coordina el dominio con la infraestructura. Las APIs públicas internas de tu app: lo que el mundo puede hacer con tu sistema.
- ❌ «Un template» → Frente a «Un 'caso de uso' (application service) es...» lo fácil es confundirse. **Verdad**: La orquestación de un objetivo de negocio: 'CrearTarea' coordina el dominio con la infraestructura. Las APIs públicas internas de tu app: lo que el mundo puede hacer con tu sistema.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
