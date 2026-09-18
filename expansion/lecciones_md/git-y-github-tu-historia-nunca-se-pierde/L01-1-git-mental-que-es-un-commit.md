# 1. Git mental: qué es un commit

> 📚 Curso: **Git y GitHub — Tu Historia Nunca Se Pierde** · Lección 1 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
GIT DE VERDAD: 4 IDEAS, NO 50 COMANDOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. SNAPSHOT: cada commit es una foto COMPLETA del proyecto (no diferencias). Cada foto apunta a su padre → línea de tiempo.
2. 3 ESTADOS: working (editas) → staging (git add: preparas el paquete) → repository (git commit: foto guardada).
3. BRANCH: un branch es solo un PUNTERO móvil a un commit. Head = dónde está parado tu "tú".
4. GUIAT BÁSICO DIARIO
  git status         → dónde estás (lo-las de cada sesión)
  git add -A         → preparar todo
  git commit -m "feat: sistema de quizzes"   → foto con mensaje
  git log --oneline --graph                  → ver la historia

MENSAJES: imperativo y corto ("agrega login", no "agregado/cambios/x"). Tu yo del martes lo agradece.

SETUP INICIAL (una vez): git config --global user.name "Tu" / user.email. Sin esto git no sabe quién eres.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es un commit en git?
- A) Un diff de cambios
- B) Un snapshot completo del proyecto con puntero al commit padre
- C) Un archivo zip
- D) Un mensaje
### 2. ¿Cuál es el orden del flujo básico?
- A) commit → add
- B) editar → git add → git commit
- C) push → commit
- D) add → status

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Un snapshot completo del proyecto con puntero al commit padre — Cada commit = foto completa; git las deduplica internamente (objetos).
**2.** ✅ editar → git add → git commit — Working → staging (add) → repo (commit). push va aparte al remoto.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
