# 📕 Resumen maestro — Git y GitHub — Tu Historia Nunca Se Pierde

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Git mental: qué es un commit
GIT DE VERDAD: 4 IDEAS, NO 50 COMANDOS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1. SNAPSHOT: cada commit es una foto COMPLETA del proyecto (no diferencias). Cada foto apunta a su padre → lí…

## 2. 2. Ramas: el multiverso de tu proyecto
BRANCHES: EXPERIMENTA SIN MIEDO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   git switch -c feature/login      # crear rama y saltar (equivale: checkout -b)   git switch main                  …

## 3. 3. Deshacer: checkout, restore, revert, reset (la tabla salvadora)
LA MÁQUINA DEL TIEMPO — NIVEL POR NIVEL ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ¿QUÉ ROMPÍ?                  → SOLUCIÓN Edité archivo y lo quiero original (sin commitear):   git restore ar…

## 4. 4. GitHub colaboración real: PRs y forks
TRABAJAR CON OTROS SIN PISARSE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ EL CICLO DEL PR (Pull Request) 1. git switch -c feature/quiz-IA 2. trabajas + commits 3. git push -u origin feature/q…

## 5. 5. .gitignore, tags y limpieza: buen ciudadano del repo
LIMPIEZA DE REPO NIVEL PRO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ .gitignore — cosas que NUNCA van a git:   node_modules/          # dependencias instalables   .venv/ __pycache__/    # Py…

## 6. 6. Proyecto final: flujo completo de punta a punta
SIMULA UN EQUIPO REAL EN 4 PASOS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ PRÁCTICA INTEGRAL (30 min, hazlo desde cero) 1. Nace el repo: mkdir miniapp && cd miniapp && git init    → app.py c…

---
✅ 6 lecciones · 📝 12 preguntas de repaso en quizzes_html/ · tests/