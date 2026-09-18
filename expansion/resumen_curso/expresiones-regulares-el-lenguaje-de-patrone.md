# 📕 Resumen maestro — Expresiones Regulares — El Lenguaje de Patrones

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. Regex en una lección: el 80% útil sin dolor
REGEX: PATRONES PARA TEXTOS (DIFÍCIL DE LEER, FÁCIL DE APRENDER) ━━━━━━━━━━━━━━━━━━━━━━━━━━━ ESENCIA (en todos los regex modernos):   .        cualquier carácter (excepto newline) …

## 2. 2. Capturar grupos y.los casos reales: validación y extracción
CAPTURAR SUSTANCIAS (LO QUE BUSCAS EXTRAER) ━━━━━━━━━━━━━━━━━━━━━━━━━━━ GRUPOS CON NOMBRES (legibilidad máxima)   patron = re.compile(r"(?P<usuario>[\w.]+)@(?P<dominio>[\w.]+\.\w+)…

## 3. 3. Los 5 errores clásicos de regex (no sufras estos)
ASÍ SE ROMPE EL REGEX EN PRODUCCIÓN — TUS SALVADOS AQUÍ ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1. ¡GREEDY (codicioso)! .* captura TODO lo que puede.      r"<.*>" sobre "<b>a</b><i>b</i>" matc…

## 4. 4. Proyecto: analizador de logs con regex (uso real)
CONSTRUYE: TU ANALIZADOR DE LOGS REAL ━━━━━━━━━━━━━━━━━━━━━━━━━━━ MISIÓN (90 min): te dieron 10.000 líneas de log de un servidor:   2026-09-18 13:42:15 ERROR usuario=ana metodo=POS…

---
✅ 4 lecciones · 📝 8 preguntas de repaso en quizzes_html/ · tests/