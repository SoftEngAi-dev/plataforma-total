# 8. Funciones: parámetros, return y scope

> 📚 Curso: **Python — De Cero a Profesional** · Lección 8 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
FUNCIONES: CONTRATOS DE UNA LÍNEA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  def area_rectangulo(base, altura):
      '''Devuelve el area.'''        # docstring: tu API documentada
      return base * altura

PARÁMETROS CON PODER
  def precio_con_iva(precio, iva=0.22):          # por defecto al FINAL
      return precio * (1 + iva)
  precio_con_iva(100)        → 122.0
  precio_con_iva(100, 0.10)  → 110.0
  precio_con_iva(iva=0.10, precio=100)   # kwargs: por nombre, orden libre

  def maximo(*numeros):                            # *args: tupla de sobrantes
      return max(numeros)
  def config(**opciones):                          # **kwargs: dict de nombrados
      print(opciones)

RETURN MULTIPLE (devuelve tupla):
  def punto(): return 10, 20
  x, y = punto()                  # desempaquetado

SCOPE: lo asignado dentro es LOCAL; leer globales funciona pero asignarlas requiere `global` (evítala; devuelve valores en su lugar).

Sin return → la función devuelve None.
```

---

## 📝 Quiz de la lección

### 1. def f(a, b=2): — ¿por qué el default va al final?
- A) Le gusta a Python
- B) Los posicionales deben venir primero para no ambiguar la llamada
- C) Velocidad
- D) No hay regla
### 2. Sin return, una función Python devuelve...
- A) 0
- B) cadena vacía
- C) None (¡cuidado al encadenar!)
- D) Error

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Los posicionales deben venir primero para no ambiguar la llamada — f(5) debe ser claro: a=5. Con default primero sería ambiguo.
**2.** ✅ None (¡cuidado al encadenar!) — Caso clásico: olvidas return y luego el resultado es None donde no esperas.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
