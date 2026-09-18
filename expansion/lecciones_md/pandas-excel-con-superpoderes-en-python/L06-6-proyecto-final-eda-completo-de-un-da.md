# 6. Proyecto final: EDA completo de un dataset público

> 📚 Curso: **Pandas — Excel con Superpoderes en Python** · Lección 6 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
TU EDA PROFESSIONAL (60-90 MINUTOS, ENTREGABLE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dataset sugerido: Titanic (seaborn: sns.load_dataset("titanic") gratis) o un CSV de datos abiertos de tu país. Jupyter/Colab recomendado (celdas=silverbullet de la narrativa de datos).

ESTRUCTURA DEL NOTEBOOK (documentable, PON POR ESCRITO LO QUE VES)
1. PREGUNTA guía (ej: "¿qué influyó en sobrevivir?") — = 50% del análisis
2. CARGA + PRIMER VISTAZO: shape · dtypes · head · describe · isna.sum
3. LIMPIEZA DOCUMENTADA: df.limpio = df.dropna(subset=[...]) → justificas en una celda Markdown
4. COLUMNAS DERIVADAS: df["familia"] = SibSp + Parch + 1 · categorías útiles
5. ANÁLISIS POR PREGUNTA:
   survival_rate_por_clase = df.groupby("Pclass")["Survived"].mean()
   El group by + value_counts para TODAS tus preguntas
6. 3-5 GRÁFICOS imprescindibles: tasa por sexo (bar) · por clase (bar) · edades (hist) · fare vs survived
7. CONCLUSIÓN: 3 bullets CON NÚMEROS DEFINITIVOS en markdown final

ENTREGABLE: notebook limpio (corre de arriba a abajo: Kernel → Restart & Run All) + README con screenshot y 3 aprendizajes clave.
Este documento es tu primera pieza de portafolio de datos.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué verifica 'Restart Kernel & Run All'?
- A) Nada
- B) Que tu notebook se ejecute limpio de arriba a abajo en orden — reproducibilidad real de tu análisis
- C) Es más rápido
- D) La BIOS
### 2. ¿Por qué df.groupby('Pclass')['Survived'].mean() da la tasa de supervivencia?
- A) Por casualidad
- B) El promedio de una columna 0/1 = la proporción/tasa: mean de binarios es tasa universal
- C) Es solo moda
- D) Sum()

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Que tu notebook se ejecute limpio de arriba a abajo en orden — reproducibilidad real de tu análisis — Orden del código más importante: tu análisis debe reproducirse sin celdas corridas a desorden.
**2.** ✅ El promedio de una columna 0/1 = la proporción/tasa: mean de binarios es tasa universal — El truco universal de datos: promediar flags 0/1 te da porcentajes directos en una línea.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
