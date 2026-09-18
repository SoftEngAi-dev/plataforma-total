# 1. Principios universales: SOLID abreviado útil

> 📚 Curso: **Arquitectura de Software — Diseñar para Crecer** · Lección 1 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
DISEÑO: LAS REGLAS QUE SEPARAN AL SENIOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━
KISS — Keep It Simple: la solución simple gana siempre primero; overengineering = bugs duplicados de infraestructura mental.
DRY — Don't Repeat Yourself: el conocimiento vive UNA vez (función/clase); copiar-pegar = bugs replicados por todos lados.
YAGNI — You Aren't Gonna Need It: no construyas lo que quizás nunca necesites; construye cuando lo piden.
SEPARACIÓN DE RESPONSABILIDADES (el corazón): cada módulo/clase/función hace UNA cosa bien.

SOLID EN 1 FRASE CADA UNO
• S (Single Responsibility): una clase = una razón para cambiar
• O (Open/Closed): abierto a extensión, cerrado a modificación (comportamiento nuevo por código NUEVO, no tocando el viejo probado)
• L (Liskov): subclases sustituyen a sus padres sin romper nada
• I (Interface Segregation): interfaces pequeñas > interfaces gordas forzadas
• D (Dependency Inversion): depender de ABSTRACCIONES (interfaces), no de implementaciones concretas

SINTOMAS DE ARQUITECTURA ENFERMA (smells): función de 200 líneas · clase que hace de todo · import cíclicos · cambiar una cosa rompe otras cinco · tests imposibles → refactoriza.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué propone DRY?
- A) Borrar código
- B) El conocimiento/lógica vive UNA sola vez en el sistema; repetición = inconsistencias cuando cambies un lugar y no otro
- C) Más tests
- D) Más carpetas
### 2. Dependency Inversion en práctica significa...
- A) No depender de nada
- B) Tu lógica depende de INTERFACES/contratos; la implementación concreta se inyecta y puede cambiar (prod↔test)
- C) Java nada más
- D) Inyectar SQL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ El conocimiento/lógica vive UNA sola vez en el sistema; repetición = inconsistencias cuando cambies un lugar y no otro — Copiar es rápido hoy; mantener copias divergentes es lento mañana.
**2.** ✅ Tu lógica depende de INTERFACES/contratos; la implementación concreta se inyecta y puede cambiar (prod↔test) — La pieza clave de testabilidad y arquitectura limpia: invierte quién controla las dependencias.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
