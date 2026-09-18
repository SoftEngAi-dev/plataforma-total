# 6. Proyecto: pipeline CI/CD real para tu app

> 📚 Curso: **DevOps y CI/CD — De Tu PC a Producción Sin Sudor** · Lección 6 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
TU PIPELINE DE VERDAD (HOY, en ~5 pasos)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTEXTO: ya tienes app + Dockerfile + tests básicos.

1. CREA .github/workflows/ci.yml:
   - trigger: en push y PR
   - job test: checkout → setup-python → pip install -r requirements.txt → pytest
2. Agrega aunque sea 3 tests unitarios reales a tu app
3. Push: abre repo → pestaña Actions → mira tu CI correr verde. ROMPE un test a propósito → push → rojo. Arréglalo → verde otra vez (esa sensación ES DevOps)
4. Job BUILD: pyinstaller o docker build → upload-artifact → tienes binarios descargables en la pestaña Actions
5. DESPLIEGUE (elije uno):
   a. Tu IRL: Railway/Fly.io/Render: conecta el repo → ellos corren tu Dockerfile tras cada push (despliegue continuo gratis/tier free)
   b. Tu VPS: workflow ssh/rsync + docker compose up -d tras CI verde

LOGRO TOTAL: push a main → tests → imagen → tu app actualizada sola en internet.
Con eso VIVISTE el ciclo que usan los equipos profesionales a diario. Bienvenido.
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué romper un test a propósito en el proyecto?
- A) Por diversión
- B) Verificar que el pipeline REALMENTE falla ante errores (red validate que CI funciona)
- C) Para practicar git
- D) No tiene sentido
### 2. ¿Qué diferencia el despliegue continuo del push manual a un VPS?
- A) El precio
- B) Todo paso manual se automatiza: tras CI verde la app llega sola al usuario, sin intervención humana
- C) Nada cambia
- D) Es solo para grandes empresas

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Verificar que el pipeline REALMENTE falla ante errores (red validate que CI funciona) — Un CI que nunca has visto fallar no es garantía: red/verde/red lo prueba.
**2.** ✅ Todo paso manual se automatiza: tras CI verde la app llega sola al usuario, sin intervención humana — La ausencia de pasos manuales es la ausencia de errores manuales.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
