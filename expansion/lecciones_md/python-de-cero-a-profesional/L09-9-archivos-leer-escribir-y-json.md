# 9. Archivos: leer, escribir y JSON

> 📚 Curso: **Python — De Cero a Profesional** · Lección 9 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
ARCHIVOS: PERSISTENCIA BÁSICA (Y BONITA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LA FRASE DE LOS PROFESIONALES: with
  with open("notas.txt", "w", encoding="utf-8") as f:
      f.write("línea 1\nlínea 2\n")
  with open("notas.txt", encoding="utf-8") as f:
      texto = f.read()
  with OPEN CIERRA AUTOMÁTICAMENTE aunque explote algo. SIEMPRE úsalo.

MODOS: "r" leer · "w" escribir (BORRA el anterior) · "a" agregar · "r+" ambos · "rb"/"wb" binarios
  encoding="utf-8" EXPLÍCITO siempre (evita acentos rotos entre sistemas)

JSON — el caso de uso n.º 1 real de los archivos:
  import json
  datos = {"nombre": "Ada", "temas": ["py", "js"]}
  with open("datos.json", "w", encoding="utf-8") as f:
      json.dump(datos, f),  # guardar
  with open("datos.json", encoding="utf-8") as f:
      recuperado = json.load(f)      # cargar (dict/listas)

Errores esperables: try/except FileNotFoundError alrededor del open.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué usar with open(...)?
- A) Es más corto
- B) Cierra el archivo automáticamente incluso ante errores
- C) Acelera la lectura
- D) Permite binarios
### 2. ¿Cómo guardar y recuperar un dict en JSON?
- A) write con str()
- B) json.dump() y json.load()
- C) pikcle y unpack
- D) print a archivo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Cierra el archivo automáticamente incluso ante errores — with = context manager: el recurso se libera pase lo que pase.
**2.** ✅ json.dump() y json.load() — json es universal multiplataforma; dicts/listas pasan directo.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
