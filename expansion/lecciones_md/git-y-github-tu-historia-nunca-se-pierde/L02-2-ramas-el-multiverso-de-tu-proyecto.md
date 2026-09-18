# 2. Ramas: el multiverso de tu proyecto

> 📚 Curso: **Git y GitHub — Tu Historia Nunca Se Pierde** · Lección 2 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
BRANCHES: EXPERIMENTA SIN MIEDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  git switch -c feature/login      # crear rama y saltar (equivale: checkout -b)
  git switch main                  # volver
  git branch                       # listar locales
  git merge feature/login          # desde main: integrar la rama
  git branch -d feature/login      # borrar rama ya integrada

MERGE sin conflicto: git avanza el puntero (fast-forward) o crea commit de merge.
CONFLICTO (mismo lugar editado en ambas ramas):
  <<<<<<< HEAD
  tu versión
  =======
  la versión de la rama
  >>>>>>> feature/login
Editas a mano, dejas lo correcto, git add, git commit. NO ES UN ERROR: es git pidiéndote decidir.

FLUJO DE TRABAJO DIARIO
1. main limpio y estable
2. rama por cada cosa nueva (feature/quiz-python, fix/bug-login)
3. trabajas, commiteas, merge, borras la rama

DISCIPLINA: ramas CORTAS (1-3 días); ramas largas = merges de terror.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es un merge conflict?
- A) Git roto
- B) Dos ramas editaron las mismas líneas: git te pide elegir manualmente entre marcadores <<<<
- C) Un virus
- D) Pérdida de datos
### 2. ¿Por qué ramas cortas de 1-3 días?
- A) Por estética
- B) Cambios pequeños = conflictos raros y merges simples; la rama eterna deviene imposible de integrar
- C) Git tiene límite
- D) Es solo sugerencia

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Dos ramas editaron las mismas líneas: git te pide elegir manualmente entre marcadores <<<< — Los conflictos son decisiones pendientes, no errores: resuelves, add, commit.
**2.** ✅ Cambios pequeños = conflictos raros y merges simples; la rama eterna deviene imposible de integrar — La integración continua empieza por ramas efímeras.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
