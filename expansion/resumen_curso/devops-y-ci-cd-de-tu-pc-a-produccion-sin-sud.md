# 📕 Resumen maestro — DevOps y CI/CD — De Tu PC a Producción Sin Sudor

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. DevOps en una frase y el pipeline
DEVOPS: CULTURA + AUTOMATIZACIÓN DE ENTREGAR VALOR ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ En 2008 los devs escupían código y "ops" sufría en servidores. DevOps unificó: TU construyes, TU …

## 2. 2. GitHub Actions desde cero: tu primer workflow
ACTIONS: CI/CD GRATIS EN TU REPO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ La estructura: .github/workflows/ci.yml    name: CI   on: [push, pull_request]            ← cuándo corre   jobs:   …

## 3. 3. Tests automáticos: el corazón del CI
SIN TESTS NO HAY CI REAL ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ El trabajo del pipeline es responder: ¿esto sigue funcionando? Solo los tests lo responden sin humanos.  PIRÁMIDE DE TESTS …

## 4. 4. Despliegue continuo y entornos
ENTORNOS: DEV → STAGING → PROD ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Nunca tejes en prod directo. La cadena: • DEV: tu máquina, rompe sin culpa • STAGING: réplica de producción para vali…

## 5. 5. Monitoreo y logs: saber cuando tu app llora
OBSERVABILIDAD: DEL 'SÍ FUNCIONA' AL 'SÉ CÓMO VA' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Los 3 pilares: 1. LOGS: qué pasó. Escribe logs estructurados (nivel, timestamp, mensaje).    docke…

## 6. 6. Proyecto: pipeline CI/CD real para tu app
TU PIPELINE DE VERDAD (HOY, en ~5 pasos) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ CONTEXTO: ya tienes app + Dockerfile + tests básicos.  1. CREA .github/workflows/ci.yml:    - trigger: en pus…

---
✅ 6 lecciones · 📝 12 preguntas de repaso en quizzes_html/ · tests/