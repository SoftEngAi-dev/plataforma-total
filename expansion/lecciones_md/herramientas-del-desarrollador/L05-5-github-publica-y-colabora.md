# 5. GitHub: publica y colabora

> 📚 Curso: **Herramientas del Desarrollador** · Lección 5 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
DE TU MÁQUINA AL MUNDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GitHub = git + colaboración + portafolio público.

SETUP (una vez)
  1. Cuenta en github.com
  2. Configura tu identidad: git config --global user.name "Tu Nombre" / user.email tu@correo
  3. Autenticación: token (https) o llave SSH (recomendada, permanente)

SUBIR UN PROYECTO NUEVO
  1. Crea el repo en github.com (vacío, sin README)
  2. git remote add origin git@github.com:usuario/repo.git
  3. git push -u origin main        ← primera vez
  (luego solo: git push)

CICLO DIARIO DE COLABORACIÓN
  git pull        → traer cambios del equipo
  ...trabajas, commiteas...
  git push        → subir tus cambios

También: Issues = tareas; Pull Request = proponer cambios revisables; Actions = CI/CD gratis (esta app lo usa para compilar ejecutables Win/Mac/Linux automáticamente).

🎓 Tu GitHub verde (contribuciones diarias) es hoy casi un CV por sí solo.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace `git push -u origin main`?
- A) Descarga el repo
- B) Sube tus commits y enlaza la rama local con la remota para futuros pushes
- C) Borra el repo remoto
- D) Crea el repositorio en GitHub
### 2. ¿Qué es un Pull Request?
- A) Un ticket de soporte
- B) Proponer cambios de una rama para que otros los revisen antes de fusionar
- C) Un virus
- D) Una forma de borrar ramas

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Sube tus commits y enlaza la rama local con la remota para futuros pushes — El -u solo hace falta la primera vez; después, `git push` a secas.
**2.** ✅ Proponer cambios de una rama para que otros los revisen antes de fusionar — PR = cambio propuesto + revisión + discusión + fusión: la base del trabajo en equipo.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
