# 3. Tests automáticos: el corazón del CI

> 📚 Curso: **DevOps y CI/CD — De Tu PC a Producción Sin Sudor** · Lección 3 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
SIN TESTS NO HAY CI REAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El trabajo del pipeline es responder: ¿esto sigue funcionando? Solo los tests lo responden sin humanos.

PIRÁMIDE DE TESTS
       ↑ pocos, lentos
    E2E (end-to-end: la app entera real: navegador/HTTP)
   Integración (varios módulos juntos: API + BD)
  Unitarias (muchísimas, rapidísimas: funciones aisladas)
       ↓ muchas, rápidas, baratas

PYTEST MÍNIMO (Python)
  # test_math.py
  def sumar(a, b): return a + b
  def test_sumar(): assert sumar(2, 3) == 5
  pip install pytest ; pytest    → busca test_*.py y corre solo

NODE: node --test nativo o vitest/jest
  test("suma", () => expect(sumar(2,3)).toBe(5));

REGLAS DE ORO
1. Los tests NO tocan servicios externos (usa mocks) → rápidos y confiables
2. Test que a veces falla = peor que ningún test (se ignora)
3. En CI: si un test falla ✗, el pipeline corta y NO se despliega
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué la pirámide tiene más tests unitarios que E2E?
- A) Es bonita
- B) Unitarios = rápidos, estables y baratos; E2E = lentos, frágiles y caros (manténlos pocos)
- C) Unitarios son nuevos
- D) Es convenio
### 2. ¿Qué debe evitar un test unitario?
- A) assert
- B) Tocar red/BD/reloj reales (úsese mocks/fakes) para ser rápido, repetible y confiable
- C) Ejecutarse en CI
- D) Tener nombre test_

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Unitarios = rápidos, estables y baratos; E2E = lentos, frágiles y caros (manténlos pocos) — La base ancha de unit tests cubre lógica; los pocos E2E verifican el cableado.
**2.** ✅ Tocar red/BD/reloj reales (úsese mocks/fakes) para ser rápido, repetible y confiable — Un test que depende del internet es un test que fallará a las 3am cuando menos lo esperas.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
