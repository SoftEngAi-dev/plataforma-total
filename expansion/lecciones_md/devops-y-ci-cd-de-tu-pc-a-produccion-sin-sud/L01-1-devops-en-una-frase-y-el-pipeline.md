# 1. DevOps en una frase y el pipeline

> 📚 Curso: **DevOps y CI/CD — De Tu PC a Producción Sin Sudor** · Lección 1 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
DEVOPS: CULTURA + AUTOMATIZACIÓN DE ENTREGAR VALOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
En 2008 los devs escupían código y "ops" sufría en servidores. DevOps unificó: TU construyes, TU lo corres, TU lo mejoras — con tanta AUTOMATIZACIÓN en medio que el humano no interviene.

EL PIPELINE (tubería por la que pasa todo commit)
  código → BUILD (compilar) → TEST (pruebas automáticas) → DEPLOY (al servidor/usuario)
  Si algo rompe: el pipeline se detiene y te avisa. Nadie se entera del bug salvo tú.

CI (Integración Continua): cada push corre build+tests en un runner limpio (GitHub Actions, GitLab CI...)
CD (Entrega/Despliegue Continuo): si CI está verde, se publica solo (o con un botón) a staging/producción.

POR QUÉ IMPORTA A UN DEV SOLO: aunque trabajes solo, mover tu "push → producción" de 30 pasos manuales a 1 pipeline verde es el salto de amateur a profesional. Menos errores, más velocidad, menos miedo a desplegar los viernes.

「Si duele, hazlo más seguido」→ la frecuencia hace pequeños a los problemas.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es CI (Integración Continua)?
- A) Un lenguaje
- B) Automatizar build+tests en cada push para detectar roturas al instante
- C) Un servidor
- D) Integración con bases de datos
### 2. ¿Qué diferencia hay entre entrega y despliegue continuos?
- A) Ninguna
- B) Entrega: listo para publicar con un clic; Despliegue: se publica AUTOMÁTICAMENTE al pasar CI
- C) Despliegue es más lento
- D) Son sinónimos legales

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Automatizar build+tests en cada push para detectar roturas al instante — Commits integrados y probados constantemente: el bug se detecta cuando es pequeño.
**2.** ✅ Entrega: listo para publicar con un clic; Despliegue: se publica AUTOMÁTICAMENTE al pasar CI — Delivery = siempre desplegable (decisión humana); Deployment = se hace solo.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
