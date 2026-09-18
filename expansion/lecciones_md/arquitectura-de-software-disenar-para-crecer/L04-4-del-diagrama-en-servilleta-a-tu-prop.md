# 4. Del diagrama en servilleta a tu propia arquitectura

> 📚 Curso: **Arquitectura de Software — Diseñar para Crecer** · Lección 4 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
ARQUITECTAR TU PROYECTO REAL (plática de servilleta a repo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJEMPLO REAL: "App de tareas con recordatorios por email"
PENSAMIENTO POR CAPAS/MÓDULOS (independiente del framework)
1. 🧠 DOMINIO (lógica pura testable): Tarea, Regla("si pasan 24h → vence"), sin importar web
2. 📂 APLICACIÓN (casos de uso): CrearTarea, RecordarVencidas — orquesta dominio+infra
3. 🔌 INFRAESTRUCTURA: repositorio SQLite, servidor web, adaptador email (SMTP/sendgrid)
4. 🌐 ENTREGA: API REST / UI web — llama casos de uso

REGLA DE DEPENDENCIA UNIVERSAL: capas externas dependen de las internas, NUNCA al revés (tu Tarea no sabe de HTTP ni SQL) → lo interno es testeable puro.

  src/
    dominio/tareas.py       (clases puras, sin web ni db)
    aplicacion/casos.py     (usos: CrearTarea, Recordar)
    infra/datos.py          (SQLite), infra/email.py (enviar mail)
    web/api.py              (endpoints que llaman casos)

Prueba mental: ¿puedo testear recordatorio sin servidor? sí ✅ → Buena arquitectura detectada.
Empieza a poner tu código en estas capas en tu próximo proyecto: es la misma arquitectura que en los monolitos sanos Hoy
```

---

## 📝 Quiz de la lección

### 1. ¿Qué ley cumple una buena separación en capas?
- A) Código corto
- B) Las capas INTERNAS (dominio) no conocen las EXTERNAS (web/DB): lo externo se acopla HACIA el negocio, jamás al revés
- C) Más archivos = mejor
- D) ORM
### 2. Un 'caso de uso' (application service) es...
- A) Un SQL
- B) La orquestación de un objetivo de negocio: 'CrearTarea' coordina el dominio con la infraestructura
- C) Un template
- D) CSS

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Las capas INTERNAS (dominio) no conocen las EXTERNAS (web/DB): lo externo se acopla HACIA el negocio, jamás al revés — Invertir la dirección de dependencia = tu lógica de negocio es testeable pura y viva en cualquier envoltorio.
**2.** ✅ La orquestación de un objetivo de negocio: 'CrearTarea' coordina el dominio con la infraestructura — Las APIs públicas internas de tu app: lo que el mundo puede hacer con tu sistema.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
