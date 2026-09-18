# 4. SSH: tu llave a cualquier servidor

> 📚 Curso: **Linux y Terminal — El Superpoder del Dev** · Lección 4 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
SSH: CONTROL REMOTO CIFRADO, LA HERRAMIENTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ssh usuario@IP_DEL_SERVIDOR      → entras a otra máquina por terminal (así se administran TODOS los servidores linux del mundo)

LLAVES (adiós contraseñas, más seguro)
  ssh-keygen -t ed25519            → genera par: privada (~/.ssh/id_ed25519, SECRETA) pública (.pub)
  ssh-copy-id usuario@IP           → instala tu pública en el servidor
  # o manual: copia la .pub a ~/.ssh/authorized_keys del server

  Después: ssh usuario@IP entra sin contraseña. Y scp/rsync copian archivos.

COPIAR ARCHIVOS
  scp archivo.zip usuario@IP:/home/usuario/      → subir
  rsync -avz carpeta/ usuario@IP:~/destino/       → sincronizar (solo diferencias, reanudable)

CONFIGS PARA TIPOGRAFÍA CÓMODA (~/.ssh/config)
  Host miserver
      HostName 192.0.2.10
      User ubuntu
  → ssh miserver   (así de corto)

PUERTOS/CHECKS: ssh -p 2222 (puerto no estándar) · el firewall/ufw decide qué entra.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué llaves SSH en vez de contraseña?
- A) Son más cortas
- B) Criptografía asimétrica: la privada nunca viaja; contraseñas por red son atacables con fuerza bruta
- C) Es obligatorio
- D) No hay diferencia
### 2. rsync -avz a/ usuario@IP:~/b/ se usa para...
- A) Imprimir
- B) Sincronizar carpetas remotas eficientemente (solo cambios, comprime, reanuda)
- C) Chat remoto
- D) Ejecutar SQL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Criptografía asimétrica: la privada nunca viaja; contraseñas por red son atacables con fuerza bruta — La pública en el server + privada en tu máquina: imposible de robar por sniffing.
**2.** ✅ Sincronizar carpetas remotas eficientemente (solo cambios, comprime, reanuda) — El caballo de batalla de backups y despliegues artesanales.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
