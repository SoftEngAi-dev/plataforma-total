# 4. GitHub colaboración real: PRs y forks

> 📚 Curso: **Git y GitHub — Tu Historia Nunca Se Pierde** · Lección 4 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
TRABAJAR CON OTROS SIN PISARSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EL CICLO DEL PR (Pull Request)
1. git switch -c feature/quiz-IA
2. trabajas + commits
3. git push -u origin feature/quiz-IA
4. En GitHub: New Pull Request → describes QUÉ y PARA QUÉ
5. Revisión (comentarios línea por línea) → ajustas con nuevos commits (se agregan al PR)
6. Aprobado → Merge (squash suele dejar historia limpia) → borrar rama

FORK (repos ajenos/open source): tu copia en TU cuenta → clonas, trabajas, PR al original.
Ignorar repo ajeno + clone = no puedes empujar; fork primero.

REGLAS DE ETIQUETA PRO
• PR pequeño (<400 líneas revisables) · título que dice qué · descripción que dice por qué
• Revisa el PR de otros como le gustaría que revisen el tuyo: al código, no al autor
• main protegida: nadie empuja directo, todo pasa por PR con CI verde

ISSUES = discusión/trabajo pendiente; cierra con "Closes #12" en el PR.
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál es el ciclo correcto de contribución?
- A) push directo a main
- B) rama → commits → push → PR → revisión → merge
- C) fork del compañero
- D) mail con el código
### 2. ¿Cuándo necesitas hacer fork?
- A) Siempre
- B) Cuando el repo no es tuyo/no tienes permiso de push (open source)
- C) Para clonar local
- D) Para borrar

---

## 🔑 Respuestas y explicaciones

**1.** ✅ rama → commits → push → PR → revisión → merge — El PR con revisión es el corazón del trabajo en equipo moderno.
**2.** ✅ Cuando el repo no es tuyo/no tienes permiso de push (open source) — Fork = tu copia en tu cuenta, que permite proponer PR al original.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
