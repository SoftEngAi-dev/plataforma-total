# ⚠️ Errores comunes — 6. Proyecto: pone tu PC a trabajar sola

> Linux y Terminal — El Superpoder del Dev · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «Ninguna» → Frente a «¿Qué ventaja tiene $fecha=$(date +%F) en el nombre del backup?» lo fácil es confundirse. **Verdad**: Cada respaldo es distinto: nunca sobreescribes el de ayer. Backups fechados = historia de restauración; sin fecha solo tienes una copia.
- ❌ «Es obligación del sistema» → Frente a «¿Qué ventaja tiene $fecha=$(date +%F) en el nombre del backup?» lo fácil es confundirse. **Verdad**: Cada respaldo es distinto: nunca sobreescribes el de ayer. Backups fechados = historia de restauración; sin fecha solo tienes una copia.
- ❌ «Nada» → Frente a «crontab -e + '0 21 * * * ./respaldo.sh' hace...» lo fácil es confundirse. **Verdad**: Corre el respaldo automáticamente todos los días a las 21:00. cron = programador de tareas de Unix: tu computador trabaja mientras duermes.
- ❌ «Borra cron» → Frente a «crontab -e + '0 21 * * * ./respaldo.sh' hace...» lo fácil es confundirse. **Verdad**: Corre el respaldo automáticamente todos los días a las 21:00. cron = programador de tareas de Unix: tu computador trabaja mientras duermes.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
