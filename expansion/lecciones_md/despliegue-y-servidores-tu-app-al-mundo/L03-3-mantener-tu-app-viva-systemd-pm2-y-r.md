# 3. Mantener tu app viva: systemd, pm2 y reinicios

> 📚 Curso: **Despliegue y Servidores — Tu App al Mundo** · Lección 3 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
PROCESOS QUE NO MUEREN (TRANQUILAMENTE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cerrar la terminal no mataba tu app? Ahí entra el gestor de procesos.

SYSTEMD (nativo, universal en Linux — recomendado)
  /etc/systemd/system/miapp.service:
  [Unit]
  Description=Mi app
  After=network.target
  [Service]
  ExecStart=/usr/bin/node /home/ubuntu/app/index.js
  WorkingDirectory=/home/ubuntu/app
  Restart=always                      ← si muere, resucita solo
  RestartSec=3
  Environment=NODE_ENV=production
  [Install]
  WantedBy=multi-user.target

  sudo systemctl enable --now miapp   ← inicia ahora y en cada boot
  journalctl -u miapp -f              ← sus logs en vivo

PM2 (alternativa node, con dashboard bonito): pm2 start index.js --name app && pm2 save && pm2 startup
DOCKERers: docker run --restart unless-stopped (el mismo concepto, modo contenedor)

CHECKLIST REANIMACIÓN: reinicio ante caída ✓ reinicio al boot ✓ logs persistentes ✓
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace Restart=always en systemd?
- A) Arranca lento
- B) Si el proceso muere, systemd lo vuelve a levantar automáticamente
- C) Recarga config
- D) Nada importante
### 2. ¿Por qué un proceso 'detached' no basta para producción?
- A) Sí basta
- B) Un pipeline nohup se pierde en reboots y caídas no planificadas; systemd/pm2 vigilan y resucitan
- C) Es igual
- D) Financiero

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Si el proceso muere, systemd lo vuelve a levantar automáticamente — Con enable (boot) + Restart, tu app sobrevive cuelgues Y reboots sin tocarte el dedo.
**2.** ✅ Un pipeline nohup se pierde en reboots y caídas no planificadas; systemd/pm2 vigilan y resucitan — La supervisor de procesos es la diferencia entre hobby y servicio confiable.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
