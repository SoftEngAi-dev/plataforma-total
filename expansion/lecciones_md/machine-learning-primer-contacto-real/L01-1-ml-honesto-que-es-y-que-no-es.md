# 1. ML honesto: qué es y qué NO es

> 📚 Curso: **Machine Learning — Primer Contacto Real** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
MACHINE LEARNING SIN HYPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Definición: programas que aprenden patrones DE LOS DATOS en vez de seguir reglas escritas a mano.
Clásico: escribir "si email tiene 'gratis' → spam". ML: muéstrale 10.000 emails etiquetados y APRENDE él el patrón.

LOS 3 TIPOS GRANDES
1. SUPERVISADO (90% del mundo real): datos con respuesta conocida
   → Clasificación (spam/no spam, fraude/no fraude · respuesta = categoría)
   → Regresión (precio de casa, temperatura · respuesta = número)
2. NO SUPERVISADO: sin respuesta, encuentra estructura
   → Clustering (agrupa clientes parecidos) · Reducción dimensional
3. REFUERZO: aprender por recompensas (juegos, robots) — campo aparte

WORKFLOW REAL (aprende este mapa YA)
  datos → dividir (train/test) → entrenar en train → evaluar en test (datos que el modelo NUNCA vio) → medir → mejorar
La regla SAGRADA: nunca evalúas con datos vistos en entrenamiento (evaluarías memorización, no aprendizaje).

sklearn = tu navaja suiza  (pip install scikit-learn): el estándar para ML clásico.
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál es la REGLA SAGRADA del ML?
- A) Más datos siempre
- B) Evaluar en datos de TEST separados que el modelo nunca vio en entrenamiento
- C) Usar más capas
- D) GPU obligatoria
### 2. Precio de una casa según m², zona, habitaciones es...
- A) clasificación
- B) REGRESIÓN: predecir un NÚMERO (continuo), no una categoría
- C) clustering
- D) visión

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Evaluar en datos de TEST separados que el modelo nunca vio en entrenamiento — Sin test separado solo mides memoria, no capacidad de generalizar.
**2.** ✅ REGRESIÓN: predecir un NÚMERO (continuo), no una categoría — Regresión = número; clasificación = etiqueta/categoría. Letra chica que decide tu modelo.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
