# ⚡ Cheatsheet — 4. SSH: tu llave a cualquier servidor

> Linux y Terminal — El Superpoder del Dev · Lección 4 · 18/09/2026

## 💡 Idea central
SSH: CONTROL REMOTO CIFRADO, LA HERRAMIENTA

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué llaves SSH en vez de contraseña?** → Criptografía asimétrica: la privada nunca viaja; contraseñas por red son atacables con fuerza bruta _(La pública en el server + privada en tu máquina: imposible de robar por sniffing.)_
- **rsync -avz a/ usuario@IP:~/b/ se usa para...** → Sincronizar carpetas remotas eficientemente (solo cambios, comprime, reanuda) _(El caballo de batalla de backups y despliegues artesanales.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
