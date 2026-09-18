# 3. Microservicios vs monolito: decisión de adultos

> 📚 Curso: **Arquitectura de Software — Diseñar para Crecer** · Lección 3 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
DÓNDE VIVEN LAS APPS SERIAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
MONOLITO BIEN ESTRUCTURADO (modular monolith): un solo despliegue, llamadas internas baratas, debug fácil.
 Microservicios (múltiples apps hablando por red/API) benefician a EQUIPOS GRANDES/Idependencia de escala/prod deploy.

LA VERDAD HONESTA 2026: la mayoría de startups DEBERÍAN empezar con un monolito modular (ex: Django monolito = Instagram soportó bulto millones de usuarios).

CUÁNDO MICROSERVICIOS TIENEN SENTIDO
• equipos que necesitan desplegar sin pisarse (independencia de equipos primera razón sincera)
• escalado diferenciado: el checkout necesita x100 el email-worker
• fallos aislados: un servicio caído no tumba los demás
COSTOS MICROSERVICIOS SINCEROS: red (latencia), distributed transactions, logs entre servicios, despliegue complejo, observabilidad...

REGLA: empieza monolito MODULAR (módulos con límites claros internos); si creces, extrae módulos calientes a servicios uno a uno. Netflix fue directo a micro porque era el tamaño y el equipo, no por definición."Repítelo": microservicios no son un estado objetivo; son una resposta orgániica a la escала.
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál es la mayor ventaja real del monolito modular para una startup?
- A) Hype
- B) Velocidad: un despliegue, llamadas internas sin red, debug y refactors baratos mientras el equipo es pequeño
- C) La nube
- D) GraphQL
### 2. ¿Cuál costo fijo traen los microservicios que no existe en un monolito?
- A) Ninguno
- B) Distribución: red entre servicios, transacciones complejas, logs distribuidos, deployment/orquestación
- C) CPU
- D) SQL

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Velocidad: un despliegue, llamadas internas sin red, debug y refactors baratos mientras el equipo es pequeño — El tiempo al mercado es el recurso: el monlito bien diseñado desperdicia menos meses iniciales.
**2.** ✅ Distribución: red entre servicios, transacciones complejas, logs distribuidos, deployment/orquestación — Cada petición que antes era una llamada local pasa a ser una operación de red que puede fallar.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
