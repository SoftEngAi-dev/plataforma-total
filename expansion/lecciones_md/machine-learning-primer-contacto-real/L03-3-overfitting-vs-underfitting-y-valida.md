# 3. Overfitting vs underfitting y validación

> 📚 Curso: **Machine Learning — Primer Contacto Real** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
EL DILEMA CENTRAL: MEMORIZAR VS APRENDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━
• UNDERFIT (falta aprender): muy simple. Fallas en train Y test. Complejidad insuficiente → agrégala.
• OVERFIT (memorizó): muy complejo. Perfecto en train, malo en test. Viene de "exámenes memorizados".

En el día a día: si train 99% pero test 70% → OVERFIT claro → el modelo memorizó tu muestra.

REMEDIOS CONTRA OVERFIT (los que usan los pros)
1. MÁS DATOS (la medicina maestra si puedes)
2. Modelo SIMPLE primero (baseline); solo complica si mejora test
3. REGULARIZACIÓN (penalizar complejidad: Ridge/Lasso en lineales, max_depth en árboles)
4. VALIDACIÓN CRUZADA:
   from sklearn.model_selection import cross_val_score
   scores = cross_val_score(modelo, X, y, cv=5)   → 5 evaluaciones rotando → media y desviación: mucho más robusto que UN solo split

CURVA de aprendizaje: ¿más datos mejoran tu test? si sí, conseguir más datos vale más que ajustar parámetros una semana (reality check útil)
```

---

## 📝 Quiz de la lección

### 1. Train 99%, test 72%. ¿Diagnóstico?
- A) Está perfecto
- B) OVERFIT: memorizó el entrenamiento, no generaliza — modelo demasiado complejo para los datos
- C) Underfit
- D) Mala métrica
### 2. ¿Qué aporta cross_val_score(modelo, X, y, cv=5) sobre un solo split?
- A) Nada
- B) Evalúa 5 veces con particiones rotadas: medida mucho más estable y robusta de tu desempeño real
- C) Solo velocidad
- D) Solo pega

---

## 🔑 Respuestas y explicaciones

**1.** ✅ OVERFIT: memorizó el entrenamiento, no generaliza — modelo demasiado complejo para los datos — La brecha train>>test es el síntoma canónico de sobreajuste.
**2.** ✅ Evalúa 5 veces con particiones rotadas: medida mucho más estable y robusta de tu desempeño real — Un solo split puede tener suerte/mala suerte con qué datos tocaron: la CV promedia esa lotería.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
