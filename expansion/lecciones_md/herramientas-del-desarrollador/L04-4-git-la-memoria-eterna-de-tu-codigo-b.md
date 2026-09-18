# 4. Git: la memoria eterna de tu código (básico)

> 📚 Curso: **Herramientas del Desarrollador** · Lección 4 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
GIT EN 10 COMANDOS (flujo mínimo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Git es la máquina del tiempo de tu proyecto. Puntos clave:  lo guardas TÚ con commits; sin commit no hay historia.

  git init                     → nace el repositorio aquí
  git status                   → qué cambió (lo usarás mil veces)
  git add archivo / git add -A  → preparar cambios
  git commit -m "mensaje"       → guardar punto de restauración
  git log --oneline             → ver historia
  git diff                      → qué cambió exactamente
  git checkout -- archivo       → OOPS, deshacer cambios no commiteados
  git branch nombre             → crear rama
  git switch nombre             → cambiar a rama
  git merge otra_rama           → fusionar

LA BUENA COSTUMBRE: commit pequeño y frecuente, mensaje que diga QUÉ cambiaste ("feat: quiz de python", no "cambios").

Cada commit es un punto de restauración. «No se borra nada, todo se adiciona»: con git es literalmente cierto.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace git add antes del commit?
- A) Publica en el servidor
- B) Prepara (stage) los cambios que irán en el próximo commit
- C) Borra cambios
- D) Crea una rama
### 2. ¿Cómo debe ser un buen mensaje de commit?
- A) Largo y detallado siempre
- B) Corto y describe QUÉ cambió y por qué
- C) 'asdf'
- D) Con emojis únicamente

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Prepara (stage) los cambios que irán en el próximo commit — Add prepara; commit guarda el punto en la historia.
**2.** ✅ Corto y describe QUÉ cambió y por qué — Tú futuro (y tu equipo) lo leerán: comunica el cambio.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
