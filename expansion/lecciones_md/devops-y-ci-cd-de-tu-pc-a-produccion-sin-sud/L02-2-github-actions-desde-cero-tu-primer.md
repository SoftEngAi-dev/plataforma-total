# 2. GitHub Actions desde cero: tu primer workflow

> 📚 Curso: **DevOps y CI/CD — De Tu PC a Producción Sin Sudor** · Lección 2 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
ACTIONS: CI/CD GRATIS EN TU REPO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
La estructura: .github/workflows/ci.yml

  name: CI
  on: [push, pull_request]            ← cuándo corre
  jobs:
    test:                             ← un trabajo (varios en paralelo posibles)
      runs-on: ubuntu-latest          ← runner (máquina de GitHub)
      steps:
        - uses: actions/checkout@v4            ← baja tu código
        - uses: actions/setup-python@v5
          with: { python-version: "3.12" }
        - run: pip install -r requirements.txt
        - run: python -m pytest               ← tu suite de tests

CONCEPTOS
• Workflow = el archivo; Job = paralelo aislado; Step = cada comando
• on: eventos (push, PR, cron "0 6 * * *", workflow_dispatch manual...)
• Artefactos: subir resultados (builds, binarios) descargables: actions/upload-artifact@v4

LA MAGIA: este MISMO proyecto incluye workflow que compila los ejecutables de Windows/Mac/Linux en la nube — míralo: es tu ejemplo de la vida real, no teoría.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace runs-on: ubuntu-latest?
- A) Es tu PC
- B) Define la imagen de máquina virtual limpia de GitHub que ejecutará el job
- C) El sistema del repo
- D) Nada
### 2. ¿Dónde debe vivir el archivo del workflow?
- A) en src/
- B) .github/workflows/*.yml
- C) en la raíz
- D) en cualquier lado

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Define la imagen de máquina virtual limpia de GitHub que ejecutará el job — Cada job arranca en una VM limpia; por eso hay que instalar dependencias en los steps.
**2.** ✅ .github/workflows/*.yml — GitHub solo reconoce los workflows en esa ruta exacta.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
