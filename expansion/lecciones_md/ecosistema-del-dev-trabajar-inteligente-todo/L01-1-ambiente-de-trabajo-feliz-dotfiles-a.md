# 1. Ambiente de trabajo feliz: dotfiles, alias y costumbres

> 📚 Curso: **Ecosistema del Dev — Trabajar Inteligente Todos los Días** · Lección 1 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
TU MÁQUINA ACEITADA: 1 HORA SETUP, MESES DE PRODUCTIVIDAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━
ALIAS BASH/ZSH (pon en ~/.bashrc o ~/.zshrc: los TUYOS valen oro)
  alias gs="git status"
  alias ga="git add -A"
  alias gc="git commit -m"
  alias ll="ls -lah"
  alias ..="cd .."; alias ...="cd ../.."

VARIABLES Y PATH: edita tu PATH sin miedo; tu shell config es tan código como tu proyecto (versiona tus dotfiles en GitHub: dotfiles repo = mejora + reproducible).

EDITOR/TMUX/shortcuts: 5 mins diarios a atajos nuevos pagan miles de horas después. Aprende: Ctrl+A/E (inicio/fin línea), Ctrl+U/K (borrar), Ctrl+R (histórico).

AUTOCORRECCIÓN FÍSICA: teclado/silla/monitor altura correcta: programar 40 años es maratón física; dolor de muñeca/espal es la lesión profesional.

CODE STANDARDS GRATIS: Prettier + ESLint (JS) · Black/Ruff (Python) · gofmt incluido → formato automático al guardar = CERO debates de estilo, reviews de lógica real.

TODO.txt o issues mínimas para tu yo del lunes; README por proyecto = tu futuro en tu propio arribol.
```

---

## 📝 Quiz de la lección

### 1. ¿Para qué versionar tus dotfiles en GitHub?
- A) Nada
- B) Tu entorno personal reproducible en cualquier máquina nueva en minutos
- C) Para más stars
- D) Para backups
### 2. ¿Qué problema resuelven Prettier/Black/gofmt automáticos?
- A) Poca RAM
- B) Eliminan discusiones de estilo: el estilo lo decide el configurador, tu equipo discute lógica
- C) Tests
- D) No sirven

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Tu entorno personal reproducible en cualquier máquina nueva en minutos — ~/.bashrc, config de editor, alias...: tu setup como código = ambiente portátil + aprendizaje abierto.
**2.** ✅ Eliminan discusiones de estilo: el estilo lo decide el configurador, tu equipo discute lógica — El estándar a formato compartido elimina debates bikeshedding para reviews de fondo real.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
