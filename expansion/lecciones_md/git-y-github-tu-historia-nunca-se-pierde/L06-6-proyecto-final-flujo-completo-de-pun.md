# 6. Proyecto final: flujo completo de punta a punta

> 📚 Curso: **Git y GitHub — Tu Historia Nunca Se Pierde** · Lección 6 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
SIMULA UN EQUIPO REAL EN 4 PASOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRÁCTICA INTEGRAL (30 min, hazlo desde cero)
1. Nace el repo: mkdir miniapp && cd miniapp && git init
   → app.py con una función → git add . && git commit -m "feat: hola mundo"
2. Crea repo vacío en github.com → git remote add origin ... → git push -u origin main
3. Flujo rama completa:
   git switch -c feature/despedida → añade función despedir() → commit
   git push -u origin feature/despedida → abre PR en GitHub → léetelo tú mismo como revisor
   → merge por la web → local: git switch main && git pull
4. Libera v0.1: git tag -a v0.1 -m "primera versión" && git push origin v0.1

BONUS REALISMO: vuelve a la rama, cambia la MISMA línea en main y en la rama en dos commits distintos, merge... y resuelve el conflicto a mano. Los conflictos solo se dominan viviéndolos.

SIGUIENTE: este mismo proyecto (plataforma-total) es repo git real con Actions que compilan los 3 ejecutables solos. Míralo: es un ejemplo vivo del curso.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace `git pull` tras hacer merge del PR en la web?
- A) Sube cambios
- B) Trae e integra los cambios del remoto a tu rama local
- C) Borra ramas
- D) Crea un tag
### 2. ¿Por qué practicar un conflicto a posta?
- A) Por sufrimiento
- B) Ver los marcadores <<< y resolverlo a mano desmistifica el conflicto real futuro
- C) No hace falta
- D) Para romperlo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Trae e integra los cambios del remoto a tu rama local — La web integró tu PR; tu main local está vieja hasta que pullas.
**2.** ✅ Ver los marcadores <<< y resolverlo a mano desmistifica el conflicto real futuro — El conflicto es mero texto a decidir: el miedo se cura con práctica.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
