# 3. Listas y tuplas: colecciones ordenadas

> 📚 Curso: **Python — De Cero a Profesional** · Lección 3 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
LISTAS: EL CABALLITO DE BATALLA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  numeros = [10, 20, 30, 40]
  numeros[0]     → 10
  numeros[-1]    → 40        (índices negativos: desde el final)
  numeros[1:3]   → [20, 30]  (slice: [inicio:fin), fin excluido)
  numeros[::-1]  → invertida

MUTAR (las listas SÍ cambian en el sitio)
  numeros.append(50) · insert(0, 5) · remove(20) (por valor) · pop() · sort()
  len(numeros) · sum(numeros) · max/min

COMPREHENSIONS — la estrella:
  cuadrados = [n ** 2 for n in range(10)]
  pares     = [n for n in numeros if n % 2 == 0]     # con filtro
Equivalente a map+filter en una línea readable.

TUPLAS: listas INMUTABLES entre paréntesis — para datos que no deben cambiar
  coordenada = (-34.9, -56.2)
  lat, lon = coordenada     # desempaquetado
  a, b = b, a               # swap elegante sin variable temporal

¿LISTA O TUPLA? Dinámicas → lista. Fijas/heterogéneas (registros) → tupla.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace numeros[1:3]?
- A) Devuelve 3 elementos
- B) Devuelve los elementos en posiciones 1 y 2 (fin excluido)
- C) Devuelve del 1 al 3 inclusive
- D) Error
### 2. a, b = b, a hace...
- A) Comparar
- B) Intercambiar los valores sin variable temporal (desempaquetado)
- C) Error
- D) Crear una tupla rota

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Devuelve los elementos en posiciones 1 y 2 (fin excluido) — Slices: [inicio:fin) — la mitad de los bugs de principiante vienen del fin excluido.
**2.** ✅ Intercambiar los valores sin variable temporal (desempaquetado) — La derecha se evalúa como tupla completa antes de asignar: el swap pythónico.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
