# 16. Proyecto final: tu asistente CLI personal

> 📚 Curso: **Python — De Cero a Profesional** · Lección 16 de 16
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
CONSTRUYE: ASISTENTE CLI COMPLETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Requisitos (todo el curso aplicado):
1. Comandos: nota agregar/lista · tarea agregar/hecha · dado · fecha · exportar
   usando sys.argv o menú
2. Datos en notas.json y tareas.json (json.dump/load) — persistencia real
3. Clases: Nota, Tarea con dataclasses + métodos
4. Errores con try/except específicos (JSON corrupto, input inválido)
5. Fechas con datetime (mostrar "creado hace X días")
6. Formato profesional: f-strings, emojis, líneas guía
7. Módulos: main.py + modelos.py + almacenamiento.py
8. Empaquetado: venv + requirements.txt + README.md

ESTRUCTURA SUGERIDA
  mi-asistente/
    src/main.py        (menú/argparse)
    src/modelos.py     (dataclasses)
    src/datos.py       (load/save JSON)
    notas.json tareas.json (datos del usuario: en .gitignore)
    requirements.txt README.md

GRANDES IDEAS BONUS: conectar a una API (requests al clima) · exportar CSV · tabulate para tablas bonitas.

🏆 Al terminar esto SIN copiar código externo, ya piensas como desarrollador Python.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué separar modelos.py de main.py?
- A) Obligación
- B) Separación de responsabilidades: clases/datos testeables solos, main solo orquesta
- C) Velocidad
- D) Estética
### 2. Un proyecto 'terminado' incluye además del código...
- A) Un PDF
- B) README + requirements + tests básicos + .gitignore
- C) Un servidor
- D) Logo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Separación de responsabilidades: clases/datos testeables solos, main solo orquesta — Cada módulo una razón de cambio; esto es arquitectura en pequeño.
**2.** ✅ README + requirements + tests básicos + .gitignore — Profesional = reproducible y presentable, no solo que corra en tu máquina.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
