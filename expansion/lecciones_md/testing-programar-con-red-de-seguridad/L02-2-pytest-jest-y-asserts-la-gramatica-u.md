# 2. Pytest, Jest y asserts: la gramática universal

> 📚 Curso: **Testing — Programar con Red de Seguridad** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
LA GRAMÁTICA DE LAS PRUEBAS (PYTEST COMO EJEMPLO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  # operaciones.py
  def dividir(a, b):
      if b == 0:
          raise ValueError("división por cero")
      return a / b

  # test_operaciones.py (pytest los descubre solos por nombre)
  import pytest
  from operaciones import dividir

  def test_division_normal():
      assert dividir(10, 2) == 5

  def test_division_errores():
      with pytest.raises(ValueError):
          dividir(5, 0)

  @pytest.mark.parametrize("a,b,esperado", [(10,2,5), (9,3,3), (1,4,0.25)])   # tabla 3 casos en 1
  def test_varios(a, b, esperado):
      assert dividir(a, b) == esperado

AAA patrón sagrado de cada test: Arrange (preparar) → Act (actuar) → Assert (verificar).
Un test = UNA afirmación/pregunta específica con nombre descriptivo (test_deberia_fallar_al_reservar_duplicado).

CASOS QUE TESTEAR UN PRO: camino feliz + bordes (vacío, 0, negativos, máximo) + errores (qué pasa si dato malo).
Correr: pytest -v · pytest -k "division" · pytest --cov (cobertura)
```

---

## 📝 Quiz de la lección

### 1. ¿Qué patrón AAA estructura un buen test?
- A) AAA
- B) Arrange (preparar datos) → Act (ejecutar lo probado) → Assert (verificar el resultado)
- C) 3 tests
- D) Atributos
### 2. ¿Qué hace pytest.raises(ValueError) en with?
- A) Lanza error en pytest
- B) Verifica que el código LANZA esa excepción concreta — test del comportamiento de error
- C) Mata el test
- D) Catch

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Arrange (preparar datos) → Act (ejecutar lo probado) → Assert (verificar el resultado) — Estructura legible y consistente: la legibilidad de los tests es deuda evitada.
**2.** ✅ Verifica que el código LANZA esa excepción concreta — test del comportamiento de error — Probar los caminos de error es tan importante (o más) que el camino feliz.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
