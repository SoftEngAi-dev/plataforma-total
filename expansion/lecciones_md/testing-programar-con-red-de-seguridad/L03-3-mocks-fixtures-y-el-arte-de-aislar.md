# 3. Mocks, fixtures y el arte de aislar

> 📚 Curso: **Testing — Programar con Red de Seguridad** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
TEST DOBLE: TU LABORATORIO SIN SORPRESAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
MOCK = simular lo externo (API, email, BD, hora) para probar SOLO lo tuyo.
  from unittest.mock import patch, MagicMock
  def clima_ciudad(ciudad):
      r = requests.get(f"https://api.clima/{ciudad}")
      return r.json()["temp"]

  @patch("miapp.requests.get")                       # interceptamos la llamada a la red
  def test_clima(mock_get):
      mock_get.return_value.json.return_value = {"temp": 25}   # el "clima" del laboratorio
      assert clima_ciudad("Montevideo") == 25
Ahora el test corre sin internet, sin API real, siempre igual. ESO es el punto.

FIXTURES (pytest): preparación compartida sin repetir
  import pytest
  @pytest.fixture
  def usuario_demo():
      return {"nombre": "Ada", "edad": 36}
  def test_nombre(usuario_demo):
      assert usuario_demo["nombre"] == "Ada"
  # scope="module" si lo costoso (BD demo) se crea UNA vez por módulo

NIVELES de test doubles: stub (devuelve fijo) · mock (registra llamadas: verifica QUÉ llamaste) · fake (implementación de juguete: BD en memoria)
```

---

## 📝 Quiz de la lección

### 1. ¿Cuándo usar mock?
- A) Siempre
- B) Cuando tu función llama a algo EXTERNO (red/BD/tiempo) y quieres probar solo tu lógica con respuestas controladas
- C) Nunca
- D) Solo restaurar
### 2. ¿Qué reutiliza una fixture de pytest?
- A) Nada
- B) La preparación compartida entre muchos tests (datos de prueba, conexiones, objetos complejos)
- C) El modal
- D) Docker

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Cuando tu función llama a algo EXTERNO (red/BD/tiempo) y quieres probar solo tu lógica con respuestas controladas — El mock convierte tu entorno en laboratorio: mismos datos, siempre, instantáneo.
**2.** ✅ La preparación compartida entre muchos tests (datos de prueba, conexiones, objetos complejos) — Fixture = DRY aplicado a tests: un usuario demo se define una vez y todos lo usan.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
