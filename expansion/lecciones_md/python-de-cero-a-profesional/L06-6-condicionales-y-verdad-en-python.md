# 6. Condicionales y verdad en Python

> 📚 Curso: **Python — De Cero a Profesional** · Lección 6 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
IF/ELIF/ELSE — LA SINTAXIS LIMPIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  if edad >= 18:
      print("mayor")
  elif edad >= 13:
      print("adolescente")
  else:
      print("menor")

EXPRESIÓN CONDICIONAL (ternario pythónico):
  mensaje = "mayor" if edad >= 18 else "menor"

VERDAD PYTHONICA (qué vale como True/False)
  Falsy: 0, 0.0, "", [], {}, set(), None, False
  Todo lo demás es truthy → aprovecha:
  if nombre:          # existe y no está vacío
  if not lista:       # lista vacía
  while numero:       # hasta que valga 0

COMPARADORES: == != < > <= >=
CADENADOS (pythónico): 18 <= edad < 65     (rango natural)

LÓGICOS: and · or · not
  if edad >= 18 and tiene_cedula:

⚠ is vs ==: `is` compara IDENTIDAD (mismo objeto); `==` compara VALOR. Con None siempre: if x is None.
```

---

## 📝 Quiz de la lección

### 1. if usuario is None — ¿por qué 'is' y no '=='?
- A) Es más corto
- B) None es singleton: se compara identidad; además is evita métodos __eq__ raros
- C) == no funciona con None
- D) Convención sin razón
### 2. ¿Qué pasa con if [0]?
- A) Es truthy (lista NO vacía aunque contenga 0)
- B) Es falsy
- C) Error
- D) Depende

---

## 🔑 Respuestas y explicaciones

**1.** ✅ None es singleton: se compara identidad; además is evita métodos __eq__ raros — None/True/False → is. Valores → ==
**2.** ✅ Es truthy (lista NO vacía aunque contenga 0) — La verdad está en la ESTRUCTURA (vacía vs no), no en el contenido.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
