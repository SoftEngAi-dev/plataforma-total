# 4. Cobertura, TDD práctico y tests de integración

> 📚 Curso: **Testing — Programar con Red de Seguridad** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
MÁS ALLÁ DEL TEST UNITARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
COBERTURA — métrica útil (pero muerte por meta)
  pip install pytest-cov; pytest --cov=miapp --cov-report=term-missing
Te muestra qué líneas/branches corrieron los tests. 80% sano > 100% fanático (puede encubrir asserts débiles).

TDD PRÁCTICO (no dogma, SÍ herramienta)
  Bug reportado → escribe el TEST que FALLA reproduciendo el bug → arréglalo → test pasa → CI verde para siempre.
  (Este flujo vuelve cada bug en un caso de test eterno: jamás devuelve por arte de magia.)

TESTS DE INTEGRACIÓN/E2E — pocos, controlados, vivos
• Integración: varios componenteścon un entorno controlado: API con BD de prueba (docker compose -f test)
• E2E: simular usuario real completo (Playwright/Selenium):
  page.goto() → escribir → click → verificar texto: navegador real automatizado
  En CI corren tras los unitarios (más lentos): estructura 'smoke tests' para lo más crítico.

REGLA DE PIPELINE SANO: unitarios rápidos SIEMPRE · integración ligeros · E2E de lo esencial. Cobertura alta pero tests ÚTILES, no relleno.
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál es la mejor forma de evitar que un bug VUELVA?
- A) Comentarios
- B) Escribir PRIMERO el test que reproduce el bug: queda eternamente verificado en la suite
- C) Code review
- D) Más RAM
### 2. ¿Qué diferencia test E2E de integración?
- A) Ninguna
- B) E2E = flujo de usuario REAL completo (browser/UI); integración = componentes juntos sin UI necesariamente
- C) E2E es más rápido
- D) Integración es frontend

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Escribir PRIMERO el test que reproduce el bug: queda eternamente verificado en la suite — Bug→test rojo→fix→test verde= la regresión muere definitivamente.
**2.** ✅ E2E = flujo de usuario REAL completo (browser/UI); integración = componentes juntos sin UI necesariamente — Pocos E2E (frágiles/lentos pero definitivos): el pico de la pirámide.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
