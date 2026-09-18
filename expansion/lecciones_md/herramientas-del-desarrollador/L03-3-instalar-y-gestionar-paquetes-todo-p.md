# 3. Instalar y gestionar paquetes (todo por terminal)

> 📚 Curso: **Herramientas del Desarrollador** · Lección 3 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
GESTORES DE PAQUETES: LA TIENDA DE TU STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cada lenguaje tiene el suyo:
• Python → pip    : pip install requests
• Node   → npm    : npm install express
• Sistema(Ubuntu) → apt    : sudo apt install git
• Mac    → brew   : brew install python

PYENV/VIRTUALENV — ¿aislamiento?
pip instala global por defecto y los proyectos chocan entre sí. Solución: un virtualenv por proyecto:
  python3 -m venv .venv
  source .venv/bin/activate    # Windows: .venv\Scripts\activate
  pip install requests
  pip freeze > requirements.txt

El requirements.txt registra tus dependencias → cualquiera puede reproducir tu proyecto:
  pip install -r requirements.txt

Esta app mismo tiene el suyo: es así de universal.
```

---

## 📝 Quiz de la lección

### 1. ¿Para qué sirve un virtualenv en Python?
- A) Acelerar el código
- B) Aislar las dependencias de cada proyecto para que no choquen
- C) Compilar Python más rápido
- D) Ejecutar código remoto
### 2. ¿Qué hace `pip install -r requirements.txt`?
- A) Crea el archivo de dependencias
- B) Instala todas las dependencias registradas del proyecto
- C) Actualiza pip
- D) Desinstala paquetes

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Aislar las dependencias de cada proyecto para que no choquen — Cada proyecto tiene su propio set de paquetes/versions; nunca chocan.
**2.** ✅ Instala todas las dependencias registradas del proyecto — La forma estándar de reproducir el entorno de un proyecto en cualquier máquina.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
