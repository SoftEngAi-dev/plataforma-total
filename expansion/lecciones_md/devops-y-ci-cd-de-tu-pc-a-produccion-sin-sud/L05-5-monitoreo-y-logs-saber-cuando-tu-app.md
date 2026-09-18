# 5. Monitoreo y logs: saber cuando tu app llora

> 📚 Curso: **DevOps y CI/CD — De Tu PC a Producción Sin Sudor** · Lección 5 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
OBSERVABILIDAD: DEL 'SÍ FUNCIONA' AL 'SÉ CÓMO VA'
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Los 3 pilares:
1. LOGS: qué pasó. Escribe logs estructurados (nivel, timestamp, mensaje).
   docker logs -f contenedor · journalctl -u miapp -f (systemd)
2. MÉTRICAS: cuántas requests/seg, errores %, latencia p95, RAM/CPU.
3. TRACES: recorrido de una petición a través de tu sistema (en micro-servicios).

LOGGING BIEN HECHO (reglas)
• Niveles: DEBUG (desarrollo) → INFO (eventos normales) → WARNING (rarito) → ERROR (fallo)
• JSON structured logs: máquinas los filtran (jq), humanos los leen
• NO loguees secretos ni datos personales (GDPR/sentido común)
• Con timestamp siempre: "ERROR 2026-09-18T13:44 disc-quota"

HERAMIENTAS pro gratuitas para practicar (ojo pesar): Grafana + Prometheus (métricas), Loki (logs), Uptime Kuma (¿sigue arriba?).

Empieza por lo simple: logs claros + un /health endpoint + Uptime Kuma revisando que responde 200 cada minuto. Ya duermes mejor.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué niveles correctos de logs distinguen?
- A) Solo print
- B) DEBUG/INFO/WARNING/ERROR — filtras según la gravedad y el ambiente
- C) Rojo/verde
- D) único nivel
### 2. ¿Qué verifica un endpoint /health?
- A) La base de datos sola
- B) Que la aplicación responde (200) — monitores externos lo sondean periódicamente
- C) Los tests
- D) La red

---

## 🔑 Respuestas y explicaciones

**1.** ✅ DEBUG/INFO/WARNING/ERROR — filtras según la gravedad y el ambiente — En prod corre INFO+; en dev activas DEBUG. El ruido bien dosificado vale oro.
**2.** ✅ Que la aplicación responde (200) — monitores externos lo sondean periódicamente — Healthcheck es el '¿sigues viva?' de toda app desplegada: bases de alertas.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
