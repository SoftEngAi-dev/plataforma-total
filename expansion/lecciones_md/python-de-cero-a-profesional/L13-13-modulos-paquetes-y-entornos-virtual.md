# 13. Módulos, paquetes y entornos virtuales

> 📚 Curso: **Python — De Cero a Profesional** · Lección 13 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
ORGANIZA TU CÓDIGO COMO LOS PROFESIONALES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MÓDULO = un archivo .py. IMPORTA lo que necesitas:
  import math; math.sqrt(2)                    # namespace claro
  from math import sqrt; sqrt(2)               # directo
  import mis_utilidades                         # ¡tus archivos también son módulos!

PAQUETE = carpeta con __init__.py (puede estar vacío):
  proyecto/
    src/
      __init__.py
      tareas.py  (clase Tarea)
      main.py    (from tareas import Tarea — si lo corre como módulo)
  python3 -m src.main        # -m = ejecutar como módulo (los imports funcionan)

if __name__ == "__main__":   ← código que corre SOLO si ejecutas el archivo directo (no al importarlo)

ENTORNOS VIRTUALES (¡obligatorios!)
  python3 -m venv .venv && source .venv/bin/activate
  pip install requests
  pip freeze > requirements.txt

ESTRUCTURA REAL (mínima profesional): src/ + tests/ + README + requirements + .gitignore
```

---

## 📝 Quiz de la lección

### 1. ¿Qué protege if __name__ == '__main__'?
- A) Al socket
- B) El código solo corre al EJECUTAR el archivo, no al importarlo
- C) Los tipos
- D) La memoria
### 2. ¿Por qué python3 -m src.main y no python3 src/main.py?
- A) Es más corto
- B) Con -m, los imports relativos del paquete funcionan; con ruta directa suelen romperse
- C) Es lo mismo
- D) Es más rápido

---

## 🔑 Respuestas y explicaciones

**1.** ✅ El código solo corre al EJECUTAR el archivo, no al importarlo — Permite archivos que son a la vez librería (importar) y script (correr).
**2.** ✅ Con -m, los imports relativos del paquete funcionan; con ruta directa suelen romperse — -m ejecuta como módulo del paquete: los from tareas import resuelven bonito.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
