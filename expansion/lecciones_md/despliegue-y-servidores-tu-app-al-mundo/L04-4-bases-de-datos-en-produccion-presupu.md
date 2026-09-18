# 4. Bases de datos en producción: presupuesto mínimo de seriedad

> 📚 Curso: **Despliegue y Servidores — Tu App al Mundo** · Lección 4 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
DATOS EN PROD: ALGUNOS PRECEPTOS DUROS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
DONDE PONER LA BD
• Hobby/practicar: SQLite en volumen persistente funciona PERFECTO (miles de apps reales la usan)
• Apps mayores: PostgreSQL (administrada si prefieres no sudarte: Neon/AWS RDS/Supabase; o en tu VPS en Docker con volumen)

REGLAS NO NEGOCIABLES
1. BACKUPS AUTOMÁTICOS, PROBADOS (un backup no restaurado no es backup)
     pg_dump miapp | gzip > backup-$(date +%F).sql.gz    (cron diario)
2. La BD NO se expone al internet público: bind a localhost o red privada, siempre
3. Usuarios con privilegios MÍNIMOS: tu app no usa el usuario root/postgres
4. Contraseña fuerte y EN VARIABLES DE ENTORNO (nunca en el código)
5. SSL/TLS si atraviesa redes (proveedores gestionados lo incluyen)

FIREWALL — la ley del mínimo:
  sudo ufw allow OpenSSH && sudo ufw allow 'Nginx Full' && sudo ufw enable
  (solo 22 y 80/443 abiertos. La BD queda inaccesible desde fuera. Así debe ser.)
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué la base de datos NUNCA se expone directamente a internet?
- A) Por costo
- B) Ataques automáticos la encontrarían en horas; debe escuchar solo localhost/red interna
- C) Por latencia
- D) Está bien exponerla
### 2. ¿Qué es un backup 'probado'?
- A) Está comprimido
- B) Que REALMENTE restauraste alguna vez y verificaste que funciona
- C) Automático
- D) Está en la nube

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Ataques automáticos la encontrarían en horas; debe escuchar solo localhost/red interna — Postgres/MySQL abiertos al mundo topan scanners a los minutos: firewall + bind local o red privada.
**2.** ✅ Que REALMENTE restauraste alguna vez y verificaste que funciona — Sin undrill de restauración periodic, el backup puede estar corrupto sin que lo sepas.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
