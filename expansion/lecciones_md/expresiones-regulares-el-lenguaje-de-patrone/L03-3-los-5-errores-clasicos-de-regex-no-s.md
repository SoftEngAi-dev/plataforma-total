# 3. Los 5 errores clásicos de regex (no sufras estos)

> 📚 Curso: **Expresiones Regulares — El Lenguaje de Patrones** · Lección 3 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
ASÍ SE ROMPE EL REGEX EN PRODUCCIÓN — TUS SALVADOS AQUÍ
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ¡GREEDY (codicioso)! .* captura TODO lo que puede.
     r"<.*>" sobre "<b>a</b><i>b</i>" matchea DESDE <b> HASTA </i> entero 💀
     Fix: lazy → <.*?> (el ? lo hace contraccible: captura lo mínimo posible)
2. sin FLAGS accesorios:
     re.IGNORECASE (r"python" matcha "PYTHON") · re.MULTILINE (^$ por línea) · re.DOTALL (. incluye newline)
3. Escapado olvidado: el PUNTO literal es \. (sino matchea cualquier char: "2x5" matchearia "2.5" con r"2.5" errado)
   Regla: cuan desperas literales como . ? + * ( ) [ ] { } | \ → anteponer 4. Invalid formats en raw strings (Python): escribe r"\d+" y no "\\d+" → SyntaxWarning in 3.12+
5. Catastrophic backtracking: ((a+)+$) con texto malo = tu CPU al 100% una hora (¡ataque Regex DoS real!)
   Fix: evitar anidamiento innecesario de cuantificadores + probar con strings adversos en regex101

REGLA SABÍA: si tu texto tiene estructura fija conocida (JSON, HTML, dataclasses)... mejor parsea con la librería apropiada, no regex.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué arregla .*? frente a .*?
- A) Nada
- B) ? lo vuelve LAZY/no-greedy: captura el MÍNIMO posible en vez de todo lo posible
- C) Más rápido
- D) Al revés
### 2. ¿Cuándo NO usarías regex?
- A) Siempre ideal
- B) Para estructuras complejas anidadas como HTML/JSON reales: usa parseadores diseñados, regex se rompe en los bordes
- C) Para logs
- D) Para emails

---

## 🔑 Respuestas y explicaciones

**1.** ✅ ? lo vuelve LAZY/no-greedy: captura el MÍNIMO posible en vez de todo lo posible — La diferencia entre 'primer cierre que encuentras' y 'último del documento': regex es codiciosa por defecto y se come todo.
**2.** ✅ Para estructuras complejas anidadas como HTML/JSON reales: usa parseadores diseñados, regex se rompe en los bordes — Zawinski: 'ahora tienes dos problemas'. Texto libre ↔ regex; formato estructurado ↔ parser real.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
