# 5. Proyecto: suite de tests real para tu calculadora/app

> 📚 Curso: **Testing — Programar con Red de Seguridad** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
CONSTRUYE: CALCULADORA CON TDD REAL (EN VIVO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
RETO TDD ESTRICTO (40-60 min, disciplina pura):
FUNCIONES: sumar, restar, multiplicar, dividir (con error en cero), porcentaje, memoria (M+, MR).
Por cada función: 🔴 test que falla → 🟢 código mínimo → 🔵 refactor.

# test_calculadora.py
from calculadora import Calculadora
import pytest

@pytest.fixture
def calc(): return Calculadora()

def test_suma(calc):
    assert calc.sumar(2, 3) == 5

def test_resta_negativos(calc):
    assert calc.restar(-2, -3) == 1      # ¡bordes!

def test_dividir_por_cero_lanza_error(calc):
    with pytest.raises(ValueError, match="cero"):
        calc.dividir(5, 0)

@pytest.mark.parametrize("total,pct,esperado", [(200, 10, 20), (50, 50, 25)])
def test_porcentaje(calc, total, pct, esperado):
    assert calc.porcentaje(total, pct) == esperado

# calculadora.py — escríbelo SOLO para que los tests pasen

SUITE COMPLETA: pytest -v con todos ✅ + pytest --cov 90%+.
EJERCICIO ESPIRITUAL: agrega una función NUEVA primero escribiendo SU test. Siente TDD en carne propia.
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál secuencia TDD correcta?
- A) Código-test
- B) 🔴 test que falla → 🟢 código mínimo que pase → 🔵 refactor mejorando sin romper el verde
- C) Test después solo
- D) Código+garantizar
### 2. restar(-2, -3) == 1 es un test de...
- A) feliz nomás
- B) CASO BORDE (números negativos): los pros testean fronteras, no solo caminos felices
- C) error
- D) mock

---

## 🔑 Respuestas y explicaciones

**1.** ✅ 🔴 test que falla → 🟢 código mínimo que pase → 🔵 refactor mejorando sin romper el verde — Primero el contrato del comportamiento (test), después el código que lo cumple.
**2.** ✅ CASO BORDE (números negativos): los pros testean fronteras, no solo caminos felices — Los bugs viven en los bordes: tu suite debe patrullarlos siempre.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
