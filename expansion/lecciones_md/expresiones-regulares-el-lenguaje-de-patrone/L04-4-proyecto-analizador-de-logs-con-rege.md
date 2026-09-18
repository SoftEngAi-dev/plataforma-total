# 4. Proyecto: analizador de logs con regex (uso real)

> 📚 Curso: **Expresiones Regulares — El Lenguaje de Patrones** · Lección 4 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
CONSTRUYE: TU ANALIZADOR DE LOGS REAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━
MISIÓN (90 min): te dieron 10.000 líneas de log de un servidor:
  2026-09-18 13:42:15 ERROR usuario=ana metodo=POST ruta=/api/login ip=187.55.20.10 ms=234

TAREAS
1. PARSEAR CADA LÍNEA a dictado de campos:
   patron = re.compile(
       r"(?P<fecha>\d{4}-\d{2}-\d{2}) (?P<hora>\d{2}:\d{2}:\d{2}) (?P<nivel>\w+) "
       r"usuario=(?P<usuario>\w+) metodo=(?P<metodo>\w+) ruta=(?P<ruta>\S+) "
       r"ip=(?P<ip>[\d.]+) ms=(?P<ms>\d+)"
   )
   datos = [patron.match(linea).groupdict() for linea in log.splitlines() if patron.match(linea)]
2. MÉTRICAS: errores por usuario · p95 de ms · rutas más llamadas (Counter(rutas)) · IPs únicas
3. FILTRAR/EXPORTAR solo las líneas ERROR a un CSV
4. BONUS: valida formato email de una columna en un CSV de clientes
5. REPORTE: un pequeño "log-analisis.md" con 3 hallazgos cuantificados

ESTE SCRIPT es literalmente una herramienta de trabajo real en analistas/SREs: tu primer herramienta 'power-user' construída.
OJO: regex101.com para° probar el patrón sobre 5 líneas muestra antes de correr las 10.000.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace groupdict() sobre un Match?
- A) CSV
- B) Devuelve un dictando con grupos NOMBRADOS para cada campo: linea→estructura lista para pandas/procesar
- C) Error
- D) Orden
### 2. ¿Por qué probar tu regex en regex101 con muestras primero?
- A) Es cool
- B) Detectas backtracking/capturas raras/escapes al instante antes de correr sobre miliones de líneas y romper produción
- C) Por nada
- D) Static

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Devuelve un dictando con grupos NOMBRADOS para cada campo: linea→estructura lista para pandas/procesar — La puente: texto crudo → registro estructurado con nombres del grupo = pipeline real.
**2.** ✅ Detectas backtracking/capturas raras/escapes al instante antes de correr sobre miliones de líneas y romper produción — Iteras el patrón en segundos con explicación en vivo; es la herramienta existente.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
