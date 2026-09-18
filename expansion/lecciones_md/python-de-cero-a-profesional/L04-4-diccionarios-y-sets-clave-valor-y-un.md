# 4. Diccionarios y sets: clave-valor y unicidad

> 📚 Curso: **Python — De Cero a Profesional** · Lección 4 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
DICTS: LA ESTRUCTURA MÁS USADA DE PYTHON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  alumno = {"nombre": "Ada", "edad": 36, "temas": ["py", "js"]}
  alumno["nombre"]        → "Ada"
  alumno.get("email")     → None     (¡sin explotar!)
  alumno.get("email", "sin email")   → valor por defecto
  alumno["ciudad"] = "Londres"       # agregar/actualizar
  del alumno["edad"]
  "nombre" in alumno      → True     (chequea CLAVES)

RECORRER
  for clave, valor in alumno.items(): print(clave, "=", valor)
  .keys() · .values() · .items()

DICT COMPREHENSION
  cuadrados = {n: n**2 for n in range(5)}     → {0:0, 1:1, 2:4, 3:9, 4:16}

SETS: colección SIN duplicados y sin orden — operaciones de conjunto
  set([1,1,2,3])          → {1, 2, 3}         (deduplicar al vuelo)
  {1,2,3} & {2,3,4} → {2, 3}  (intersección) · | unión · - diferencia

JSON ↔ DICT: prácticamente lo mismo → apis y archivos (lo veremos con json).
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué alumno.get('email') en vez de alumno['email']?
- A) Es más rápido
- B) Evita KeyError: devuelve None (o el default) si falta la clave
- C) Es más corto
- D) No hay diferencia
### 2. ¿Para qué usar set([1,1,2,3])?
- A) Ordenar
- B) Eliminar duplicados: {1, 2, 3} (los sets no repiten)
- C) Sumar
- D) Nada útil

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Evita KeyError: devuelve None (o el default) si falta la clave — get = acceso defensivo sin try/except; úsalo cuando la clave puede faltar.
**2.** ✅ Eliminar duplicados: {1, 2, 3} (los sets no repiten) — Deduplicación instantánea + operaciones matemáticas de conjuntos.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
