# 5. Scripts Bash: automatiza tu propia vida

> 📚 Curso: **Linux y Terminal — El Superpoder del Dev** · Lección 5 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
BASH: TU PRIMER LENGUAJE REAL DE SERVIDOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  #!/bin/bash            ← shebang: qué lo ejecuta (primera línea)
  nombre="Mundo"
  echo "Hola, $nombre"   ← $ para expandir variables

  for f in *.txt; do
      echo "Procesando $f"
  done

  if [ -f config.txt ]; then
      echo "existe"
  else
      echo "no existe"
  fi

  # argumentos: $1 $ or $2 ... · "$@" todos · $# cuántos
  echo "Hola $1"

GUARDA COMO backup.sh, chmod +x, ./backup.sh

CHECKS ÚTILES: -f archivo existe·-d directorio·-z vacío·"$a" == "$b"
COMILLA DOBLA SIEMPRE en variables: echo "$f" (si tiene espacios, sin comillas EXPLOTA)

set -euo pipefail    ← al inicio: que falle el script si algo falla (scripts sanos)

EJEMPLO REAL: backup diario con fecha en el nombre:
  fecha=$(date +%F)
  tar -czf "backup-$fecha.tar.gz" ~/proyectos/
  cron: 0 3 * * * /ruta/backup.sh   (crontab -e → lo corre solo a las 3am)
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué siempre "comillas dobles" en variables de bash?
- A) Son bonitas
- B) Sin ellas, valores con espacios se rompen en múltiples argumentos (bugs y desastres)
- C) Van más rápido
- D) Solo en if
### 2. set -euo pipefail permite...
- A) Depurar
- B) Fallar rápido y claramente: el script se detiene ante errores en vez de continuar roto
- C) Logs bonitos
- D) Correr en paralelo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Sin ellas, valores con espacios se rompen en múltiples argumentos (bugs y desastres) — rm $f → rm dos cosas si f="mi archivo.txt"; rm "$f" → correcto.
**2.** ✅ Fallar rápido y claramente: el script se detiene ante errores en vez de continuar roto — Script que sigue tras error suele causar más daño que uno que para.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
