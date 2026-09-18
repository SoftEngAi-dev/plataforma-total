# 3. Deshacer: checkout, restore, revert, reset (la tabla salvadora)

> 📚 Curso: **Git y GitHub — Tu Historia Nunca Se Pierde** · Lección 3 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
LA MÁQUINA DEL TIEMPO — NIVEL POR NIVEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
¿QUÉ ROMPÍ?                  → SOLUCIÓN
Edité archivo y lo quiero original (sin commitear):
  git restore archivo.py
Preparé con add y no va:
  git restore --staged archivo.py    (saca del stage)
Un commit YA hecho es malo pero quiero conservar historia:
  git revert <hash>                   → commit nuevo que DESHACE (seguro en compartido)
Commits locales NO subidos aún, quiero borrar el último manteniendo cambios en working:
  git reset --soft HEAD~1             → vuelve, cambios siguen preparados
Borrar TODO incluido cambios (peligro):
  git restore . + git reset --hard HEAD   (¡irrecuperable!)

git stash: guarda trabajo a medias y deja limpio el stage
  git stash → trabajas en otra cosa → git stash pop

TABLA DE ORO: seguro compartido = revert · local privado = reset.
Nunca hagas reset --hard ni rebase de ramas YA SUBIDAS que otros usan.
```

---

## 📝 Quiz de la lección

### 1. git revert vs git reset — ¿cuál es seguro en commits compartidos?
- A) reset --hard
- B) revert (crea commit inverso sin reescribir la historia ya publicada)
- C) igual
- D) ninguno
### 2. git stash sirve para...
- A) Borrar todo
- B) Apartar cambios sin commit y retomarlos luego (stash pop)
- C) Subir cambios
- D) Crear rama

---

## 🔑 Respuestas y explicaciones

**1.** ✅ revert (crea commit inverso sin reescribir la historia ya publicada) — Reescribir historia compartida rompe a tus compañeros; revert es la forma polite.
**2.** ✅ Apartar cambios sin commit y retomarlos luego (stash pop) — El cajón rápido: limpio el área, atiendo la urgencia, recupero lo mío.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
