# 3. Permisos y procesos: controlar el sistema

> 📚 Curso: **Linux y Terminal — El Superpoder del Dev** · Lección 3 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
QUIÉN PUEDE QUÉ + QUÉ ESTÁ CORRIENDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERMISOS: -rwxr-xr--
  r(4) leer · w(2) escribir · x(1) ejecutar | dueño / grupo / otros
  chmod +x script.sh        → hacerlo ejecutable
  chmod 644 archivo         → típico para archivos (dueño rw, resto r)
  chmod 755 carpeta/script
  chown usuario:grupo archivo   → cambiar dueño (con sudo)

PROCESOS
  ps aux | grep python          → buscar procesos
  top / htop                    → monitor en vivo (q sale)
  kill <PID>                    → terminar amable (SIGTERM)
  kill -9 <PID>                 → matar a la fuerza (plan B)
  comando &                     → correr en segundo plano
  jobs · fg %1                  → traer al frente

SERVICIOS (systemd, en la mayoría de distros)
  sudo systemctl status/start/stop/enable miapp   → correr apps permanentes (musculo de servidores)
```

---

## 📝 Quiz de la lección

### 1. chmod +x script.sh permite...
- A) Leerlo
- B) Ejecutarlo directamente (bit de ejecución)
- C) Comprimirlo
- D) Imprimirlo
### 2. ¿Cuándo usar kill -9?
- A) Siempre primero
- B) Solo cuando kill normal (SIGTERM) falla: -9 no deja limpiar al proceso
- C) Para todo
- D) Jamás

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Ejecutarlo directamente (bit de ejecución) — Sin +x lo corres como ./script.sh solo con bash script.sh; con +x directo.
**2.** ✅ Solo cuando kill normal (SIGTERM) falla: -9 no deja limpiar al proceso — SIGTERM pide cortésmente cerrarse (guardar estado); SIGKILL lo aniquila sin aviso.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
