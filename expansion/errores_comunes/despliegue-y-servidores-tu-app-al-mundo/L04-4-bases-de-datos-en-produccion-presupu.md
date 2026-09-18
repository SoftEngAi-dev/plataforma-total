# ⚠️ Errores comunes — 4. Bases de datos en producción: presupuesto mínimo de seriedad

> Despliegue y Servidores — Tu App al Mundo · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Por costo» → Frente a «¿Por qué la base de datos NUNCA se expone directamente a internet?» lo fácil es confundirse. **Verdad**: Ataques automáticos la encontrarían en horas; debe escuchar solo localhost/red interna. Postgres/MySQL abiertos al mundo topan scanners a los minutos: firewall + bind local o red privada.
- ❌ «Por latencia» → Frente a «¿Por qué la base de datos NUNCA se expone directamente a internet?» lo fácil es confundirse. **Verdad**: Ataques automáticos la encontrarían en horas; debe escuchar solo localhost/red interna. Postgres/MySQL abiertos al mundo topan scanners a los minutos: firewall + bind local o red privada.
- ❌ «Está comprimido» → Frente a «¿Qué es un backup 'probado'?» lo fácil es confundirse. **Verdad**: Que REALMENTE restauraste alguna vez y verificaste que funciona. Sin undrill de restauración periodic, el backup puede estar corrupto sin que lo sepas.
- ❌ «Automático» → Frente a «¿Qué es un backup 'probado'?» lo fácil es confundirse. **Verdad**: Que REALMENTE restauraste alguna vez y verificaste que funciona. Sin undrill de restauración periodic, el backup puede estar corrupto sin que lo sepas.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
