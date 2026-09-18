# 2. Tu primer modelo: train/test y accuracy real

> 📚 Curso: **Machine Learning — Primer Contacto Real** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
KNN DE DÍA 1: ML EN 15 LÍNEAS CON SKLEARN
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  from sklearn.model_selection import train_test_split
  from sklearn.neighbors import KNeighborsClassifier
  from sklearn.metrics import accuracy_score, confusion_matrix
  from sklearn.datasets import load_iris

  iris = load_iris()                            # dataset de juguete (flores)
  X, y = iris.data, iris.target                 # X = features (medidas) · y = etiqueta (especie)

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  modelo = KNeighborsClassifier(n_neighbors=3)   # "dime con quién andas"... 3 vecinos votan
  modelo.fit(X_train, y_train)                  # ¡entrena!
  predicciones = modelo.predict(X_test)
  acc = accuracy_score(y_test, predicciones)
  print(f"Precisión: {acc:.2%}")                # ~96%+ en iris
  print(confusion_matrix(y_test, predicciones)) # dónde se equivoca

EL ENTENDIMIENTO > la métrica: pregunta por qué se equivocó (mirar la matriz de confusión).
random_state=42 = reproducible (misma división siempre): estándar de experimentos serios.
fit/predict = la API de sklearn universal: TODOS los modelos responden igual → aprendes uno, sabes todos.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hacen fit() y predict() en sklearn?
- A) Lo contrario
- B) fit aprende de datos de ENTRENAMIENTO; predict va'ven predicciones sobre datos nuevos
- C) Son de pandas
- D) Miden tiempo
### 2. ¿Para qué sirve la matriz de confusión?
- A) Confundir al usuario
- B) Ver no solo AL error sino QUÉ se confunde con QUÉ: errores específicos por clase
- C) Medir tiempo
- D) Gráfica

---

## 🔑 Respuestas y explicaciones

**1.** ✅ fit aprende de datos de ENTRENAMIENTO; predict va'ven predicciones sobre datos nuevos — API universal: instanciar modelo→fit(X_train, y)→predict(X) repite en toda sklearn.
**2.** ✅ Ver no solo AL error sino QUÉ se confunde con QUÉ: errores específicos por clase — Diagonal = aciertos; fuera de diagonal = confusiones específicas que guían mejora.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
