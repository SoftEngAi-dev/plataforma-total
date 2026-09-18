# 4. Árboles de decisión y RandomForest: los caballos de batalla

> 📚 Curso: **Machine Learning — Primer Contacto Real** · Lección 4 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
LOS MODELOS QUE DOMINAN EL MUNDO REAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÁRBOL: reglas si/entonces leíbles (dile a tu jefe "ESPAÑA + saldo alto → compra")
  from sklearn.tree import DecisionTreeClassifier
  arbol = DecisionTreeClassifier(max_depth=3, random_state=42)   # ← FRENO anti-overfit
  arbol.fit(X_train, y_train)
  from sklearn.tree import export_text
  print(export_text(arbol, feature_names=iris.feature_names))  # REGLAS LEGIBLES 🎉

RANDOM FOREST (el upgrade con votación democrática, casi siempre mejorazo)
  from sklearn.ensemble import RandomForestClassifier
  bosque = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42, n_jobs=-1)
  bosque.fit(X_train, y_train)

  importancia = bosque.feature_importances_     # ← Qué FEATURES mandan en las decisiones
  for nombre, imp in sorted(zip(iris.feature_names, importancia), key=lambda x: -x[1]):
      print(f"{nombre}: {imp:.3f}")

POR QUÉ SON LOS FAVORITOS INDUSTRIALES: robustos, piden poca preparación de datos, dan importancias de features explicables. Deep Learning solo gana en imágenes/audio/texto grande; para tablas, los RandomForest/GradientBoosting (XGBoost etc) suelen seguir coronando.

En tu práctica: lineal (baseline) → luego RF → ¿mejoró test? si no, quédate con el simple: interpretabilidad y velocidad ganan.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué ventaja práctica tiene max_depth=3?
- A) Ninguna
- B) Limita la complejidad del árbol: techo de cristal al overfit (regularización por construcción)
- C) Más datos
- D) Más CPU
### 2. ¿Qué te dice feature_importances_?
- A) Velocidad
- B) QUÉ VARIABLES pesan más en las decisiones del modelo: comprensión/explicación del negocio incluida
- C) Cardiología
- D) CSV

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Limita la complejidad del árbol: techo de cristal al overfit (regularización por construcción) — Árbol profundo = reglas sobreajustadas de poquitas muestras; poco profundo generaliza bien.
**2.** ✅ QUÉ VARIABLES pesan más en las decisiones del modelo: comprensión/explicación del negocio incluida — "Los 2 mejores predictores son..." directo del bosque: insights accionables.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
