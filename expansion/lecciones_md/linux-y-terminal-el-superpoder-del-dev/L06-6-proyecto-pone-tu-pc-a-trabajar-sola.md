# 6. Proyecto: pone tu PC a trabajar sola

> 📚 Curso: **Linux y Terminal — El Superpoder del Dev** · Lección 6 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
AUTOMATIZA: 3 SCRIPTS DE TU VIDA DIARIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCRIPT 1 — respaldo.sh (el indispensable)
  #!/bin/bash
  set -euo pipefail
  fecha=$(date +%F)
  tar -czf "$HOME/backups/proyectos-$fecha.tar.gz" "$HOME/PlataformaTotal" ~/proyectos 2>/dev/null || true
  echo "✅ Respaldo $fecha listo"

SCRIPT 2 — limpieza.sh (espacio en disco)
  #!/bin/bash
  echo "Temporales grandes:"
  find /tmp -type f -size +50M -exec ls -lh {} \; 2>/dev/null
  read -p "¿Borrar? (s/n) " sn
  [[ "$sn" == s ]] && find /tmp -type f -size +50M -delete && echo "🧹 limpio"

SCRIPT 3 — mi-sistema.sh (tablero rápido)
  #!/bin/bash
  echo "💾 Disco:"; df -h /
  echo "🧠 RAM:"; free -h
  echo "🔥 Top 3 procesos:"; ps aux --sort=-%mem | head -4

AUTOMÁTICO con cron (crontab -e):
  0 21 * * * $HOME/scripts/respaldo.sh >> $HOME/backups/log.txt 2>&1

🎯 La regla del dev senior: si lo haces 3 veces a mano, la 4.ª es un script.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué ventaja tiene $fecha=$(date +%F) en el nombre del backup?
- A) Ninguna
- B) Cada respaldo es distinto: nunca sobreescribes el de ayer
- C) Es obligación del sistema
- D) Comprime más
### 2. crontab -e + '0 21 * * * ./respaldo.sh' hace...
- A) Nada
- B) Corre el respaldo automáticamente todos los días a las 21:00
- C) Borra cron
- D) Abre editor solo

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Cada respaldo es distinto: nunca sobreescribes el de ayer — Backups fechados = historia de restauración; sin fecha solo tienes una copia.
**2.** ✅ Corre el respaldo automáticamente todos los días a las 21:00 — cron = programador de tareas de Unix: tu computador trabaja mientras duermes.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
