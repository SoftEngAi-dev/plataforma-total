# ⚠️ Errores comunes — 5. Monitoreo y logs: saber cuando tu app llora

> DevOps y CI/CD — De Tu PC a Producción Sin Sudor · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Solo print» → Frente a «¿Qué niveles correctos de logs distinguen?» lo fácil es confundirse. **Verdad**: DEBUG/INFO/WARNING/ERROR — filtras según la gravedad y el ambiente. En prod corre INFO+; en dev activas DEBUG. El ruido bien dosificado vale oro.
- ❌ «Rojo/verde» → Frente a «¿Qué niveles correctos de logs distinguen?» lo fácil es confundirse. **Verdad**: DEBUG/INFO/WARNING/ERROR — filtras según la gravedad y el ambiente. En prod corre INFO+; en dev activas DEBUG. El ruido bien dosificado vale oro.
- ❌ «La base de datos sola» → Frente a «¿Qué verifica un endpoint /health?» lo fácil es confundirse. **Verdad**: Que la aplicación responde (200) — monitores externos lo sondean periódicamente. Healthcheck es el '¿sigues viva?' de toda app desplegada: bases de alertas.
- ❌ «Los tests» → Frente a «¿Qué verifica un endpoint /health?» lo fácil es confundirse. **Verdad**: Que la aplicación responde (200) — monitores externos lo sondean periódicamente. Healthcheck es el '¿sigues viva?' de toda app desplegada: bases de alertas.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
