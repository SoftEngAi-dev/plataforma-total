# ⚡ Cheatsheet — 4. Del diagrama en servilleta a tu propia arquitectura

> Arquitectura de Software — Diseñar para Crecer · Lección 4 · 18/09/2026

## 💡 Idea central
ARQUITECTAR TU PROYECTO REAL (plática de servilleta a repo)

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué ley cumple una buena separación en capas?** → Las capas INTERNAS (dominio) no conocen las EXTERNAS (web/DB): lo externo se acopla HACIA el negocio, jamás al revés _(Invertir la dirección de dependencia = tu lógica de negocio es testeable pura y viva en cualquier envoltorio.)_
- **Un 'caso de uso' (application service) es...** → La orquestación de un objetivo de negocio: 'CrearTarea' coordina el dominio con la infraestructura _(Las APIs públicas internas de tu app: lo que el mundo puede hacer con tu sistema.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
