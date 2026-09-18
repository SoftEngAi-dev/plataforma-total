# 1. Tests: por qué son parte del código, no un extra

> 📚 Curso: **Testing — Programar con Red de Seguridad** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
EL MINDSET DE PRUEBAS DESDE EL DÍA 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Un test es código que PRUEBA tu otro código automáticamente. Corre en segundos mil veces al día.

POR QUÉ LOS EQUIPOS SERIOS EXIGEN TESTS
• 🛡 RED DE SEGURIDAD: refactorizas sin miedo — si rompiste algo, el test grita ya
• 📐 DOCUMENTACIÓN VIVA: el test muestra cómo se USA la función (mejor que comentarios viejos)
• 🧠 DISEÑO FORZADO: código difícil de testear = código mal acoplado (avisito de diseño temprano)
• 🟢 CI/CD: sin tests no hay despliegue continuo responsable (el pipeline necesita validar solo)

EL CICLO TDD (Test-Driven Development, disciplina opcional pero poderosa)
1. 🔴 RED: escribes UN test que FALLA (la funcionalidad aún no existe)
2. 🟢 GREEN: escribes El MÍNIMO código que lo hace pasar
3. 🔵 REFACTOR: mejoras el código, tests siempre verdes

MANTRA: "No es código hecho hasta que tiene test". Y los tests NO deben depender de red/BD/reloj:
usa MOCKS para que corran sin internet siempre igual (test rápido + confiable).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué te permite refactorizar sin miedo?
- A) Suerte
- B) Una buena suite de tests: si rompes algo al refactor, un test grita al instante
- C) ORM
- D) TypeScript solo
### 2. ¿Por qué un test no debe tocar internet/reloj reales?
- A) Es más rápido
- B) Para ser RÁPIDO, REPETIBLE y CONFIABLE: mismo resultado siempre, en cualquier máquina, sin depender de afuera
- C) Solo en CI
- D) Sin razón

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Una buena suite de tests: si rompes algo al refactor, un test grita al instante — El valor práctico nº1 de una suite: cambiar código con confianza.
**2.** ✅ Para ser RÁPIDO, REPETIBLE y CONFIABLE: mismo resultado siempre, en cualquier máquina, sin depender de afuera — Mocks/fakes sustituyen lo externo: tu test decide el comportamiento externo, no la red.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
