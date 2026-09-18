# 4. Despliegue continuo y entornos

> 📚 Curso: **DevOps y CI/CD — De Tu PC a Producción Sin Sudor** · Lección 4 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
ENTORNOS: DEV → STAGING → PROD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nunca tejes en prod directo. La cadena:
• DEV: tu máquina, rompe sin culpa
• STAGING: réplica de producción para validar (¡misma rama de Docker!)
• PROD: donde vive el usuario real

ESTRATEGIAS DE DESPLIEGUE (de simple a pro)
1. Push directo (hobby): git push → VPS corre git pull + restart
2. Docker compose up en el VPS (simple y sanito)
3. Rolling/Railway/Fly/Render: plataforma que agarra tu Dockerfile y se encarga
4. Blue-Green/Canary (empresas): nueva versión recibe 5% del tráfico primero

VARIABLES DE ENTORNO POR AMBIENTE: misma app/imagen, distinta config (DB dev vs prod) — por eso nunca hardcodeas config: la 12-factor app.

ROLLBACK: cuana algo falla, vuelves rápido. Docker hace esto trivial: la imagen anterior SIGUE ahí: corre la versión vieja otra vez y listo.

CHECKLIST DEPLOY PM: healthcheck endpoint · logs accesibles · rollback practicado · variables de prod seteadas · alertas básicas
```

---

## 📝 Quiz de la lección

### 1. ¿Para qué existe staging?
- A) Cuestión litúrgica
- B) Ambiente IDÉNTICO a producción donde validar antes del deploy real
- C) Para guardar código
- D) Para tests unitarios
### 2. ¿Qué regala Docker al momento de rollback?
- A) Nada
- B) La versión anterior sigue como imagen: vuelves a correr esa y listo, sin reinstalar
- C) Más CPU
- D) Backups de BD

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Ambiente IDÉNTICO a producción donde validar antes del deploy real — Los bugs 'solo-pasan-en-prod' se atrapan en staging.
**2.** ✅ La versión anterior sigue como imagen: vuelves a correr esa y listo, sin reinstalar — Inmutabilidad de imágenes = tiempo de restauración en segundos.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
