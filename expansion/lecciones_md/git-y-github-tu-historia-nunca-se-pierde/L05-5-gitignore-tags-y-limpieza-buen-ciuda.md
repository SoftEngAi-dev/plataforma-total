# 5. .gitignore, tags y limpieza: buen ciudadano del repo

> 📚 Curso: **Git y GitHub — Tu Historia Nunca Se Pierde** · Lección 5 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
LIMPIEZA DE REPO NIVEL PRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
.gitignore — cosas que NUNCA van a git:
  node_modules/          # dependencias instalables
  .venv/ __pycache__/    # Python
  .env                   # SECRETOS (la regla de vida)
  dist/ build/           # compilados
  *.log .DS_Store ejecutable/

⚠ Si ya subiste un secreto: eliminarlo en un nuevo commit NO basta (queda en historia) → rota la credencial y usa git filter-repo o BFG.

TAGS (versiones)
  git tag -a v1.0 -m "primera versión estable"
  git push origin --tags
  GitHub los presenta como "Releases" con binarios adjuntos.

README.md: el escaparate. Qué hace + cómo instalar + cómo usar + screenshot. Sin README casi nadie mira tu repo.

LICENCIA: MIT (permisiva) / GPL (copyleft). Sin licencia, legalmente nadie puede usar tu código.

GitHub Actions (CI): .github/workflows/*.yml — corre tests/build en cada push automáticamente, gratis.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué .env va al .gitignore SIEMPRE?
- A) Es pequeño
- B) Contiene secretos (claves, tokens) que jamás deben quedar en la historia pública
- C) Porque git no los soporta
- D) Por estilo
### 2. ¿Qué es un tag v1.0 en git?
- A) Un archivo
- B) Una marca permanente sobre un commit: la forma de publicar releases/versiones
- C) Una rama
- D) Un issue

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Contiene secretos (claves, tokens) que jamás deben quedar en la historia pública — Un secreto subido = filtrado para siempre, aunque lo borres después: hay que rotar la credencial.
**2.** ✅ Una marca permanente sobre un commit: la forma de publicar releases/versiones — Los tags señalan hitos estables; son referencia para despliegues.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
