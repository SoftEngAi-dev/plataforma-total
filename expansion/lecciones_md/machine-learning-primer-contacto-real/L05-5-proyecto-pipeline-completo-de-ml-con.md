# 5. Proyecto: pipeline completo de ML con datos reales

> 📚 Curso: **Machine Learning — Primer Contacto Real** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
TU PRIMER PROYECTO ML COMPLETO (2 horas)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dataset: Titanic (sns.load_dataset("titanic")) — meta: ¿viaja en esa clase con ese sexo... sobrevives?

  import seaborn as sns, pandas as pd
  from sklearn.model_selection import train_test_split, cross_val_score
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.metrics import accuracy_score

  df = sns.load_dataset("titanic").dropna(subset=["age", "embarked"])
  # FEATURE ENGINEERING básico (la diferencia entre fracasar y funcionar):
  df["sol@"] = (df.sibsp + df.parch == 0).astype(int)
  df = pd.get_dummies(df, columns=["sex", "embarked"], drop_first=True)   # categorías → numérico
  features = ["pclass", "age", "fare", "sol@", "sex_male", "embarked_Q"]
  X, y = df[features], df["survived"]

  X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
  m = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
  m.fit(X_tr, y_tr)
  print(f"Test: {accuracy_score(y_te, m.predict(X_te)):.2%}")        # ~80% típico
  print(f"CV 5-fold: {cross_val_score(m, X, y, cv=5).mean():.2%}")   # valida real

CHECKLIST PRO: EDA previa · NA manejados · get_dummies · baseline vs RF comparados · feature_importances_ leídas · conclusión escrita. Eso es ML honesto de nivel junior sólido.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué hace pd.get_dummies sobre columnas categóricas?
- A) Las borra
- B) Convierte categorías en columnas binarias 0/1 para que el algoritmo procese números
- C) Ordena
- D) CSV
### 2. ¿Qué es FEATURE ENGINEERING en este proyecto?
- A) SQL
- B) CREAR columnas útiles desde las existentes (ej: sol@ si viajas solo): el 40% de tu mejora suele vivir aquí
- C) Hype
- D) GPU

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Convierte categorías en columnas binarias 0/1 para que el algoritmo procese números — Los modelos comen números: género/embarque/categorías → one-hot encoding.
**2.** ✅ CREAR columnas útiles desde las existentes (ej: sol@ si viajas solo): el 40% de tu mejora suele vivir aquí — Pequeñas obviedades transformadas en datos = a veces más valor que elegir otro modelo.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
