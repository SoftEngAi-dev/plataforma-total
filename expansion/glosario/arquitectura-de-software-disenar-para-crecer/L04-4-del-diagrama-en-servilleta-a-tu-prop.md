# 📖 Glosario — 4. Del diagrama en servilleta a tu propia arquitectura

> Arquitectura de Software — Diseñar para Crecer · Lección 4 · Términos que debes poder definir sin mirar

- **Las capas INTERNAS (dominio) no conocen las EXTERNAS (web/DB): lo externo se acopla HACIA el negocio, jamás al revés** — Invertir la dirección de dependencia = tu lógica de negocio es testeable pura y viva en cualquier envoltorio.
- **La orquestación de un objetivo de negocio: 'CrearTarea' coordina el dominio con la infraestructura** — Las APIs públicas internas de tu app: lo que el mundo puede hacer con tu sistema.

✍️ Ejercicio: añade debajo TU propia definición de cada término.
