# 5. Visualización rápida y detección de historias

> 📚 Curso: **Pandas — Excel con Superpoderes en Python** · Lección 5 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```python
GRÁFICOS AL INSTANTE: LA HISTORIA EMERGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━
  import matplotlib.pyplot as plt            (pip install matplotlib)
  df["total"].hist(bins=30); plt.show()     → distribución (¿normal? ¿sesgada?)
  df.plot(x="fecha", y="total"); plt.show() → líneas temporal
  df.groupby("categoria")["total"].sum().plot.bar(); plt.show()
  df.plot.scatter(x="precio", y="cantidad"); plt.show()  → relación entre variables
  df.boxplot(column="total", by="categoria"); plt.show() → comparar distribuciones

MATPLOTLIB DETALLES DE CALIDAD
  plt.title("Ventas mensuales 2026"); plt.xlabel("Mes"); plt.ylabel("Total")
  plt.tight_layout(); plt.savefig("grafico.png", dpi=150)   → exportar escala

SEABORN (estadístico bonito, cascarón sobre matplotlib) — opcional nivel up:
  import seaborn as sns
  sns.histplot(df["total"], kde=True)
  sns.scatterplot(data=df, x="precio", y="cantidad", hue="categoria")
  sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")   → correlaciones

REGLA DEL ANALISTA: grafica ANTES de modelar. Un boxplot revela más en un vistazo que diez resúmenes numéricos.
```

---

## 📝 Quiz de la lección

### 1. ¿Cuál gráfico muestra relación entre dos numéricos?
- A) bar
- B) scatterplot: cada punto una observación - revela correlaciones, clusters y outliers de un vistazo
- C) histograma
- D) pie
### 2. ¿Qué revela un boxplot por categoría que un promedio no?
- A) Nada
- B) Distribución completa y OUTLIERS por grupo: el promedio solo cuenta la historia central
- C) Solo máximo
- D) Solo skew

---

## 🔑 Respuestas y explicaciones

**1.** ✅ scatterplot: cada punto una observación - revela correlaciones, clusters y outliers de un vistazo — Dispersión = radiografía de relaciones: la intuición primera de cualquier análisis bivariado.
**2.** ✅ Distribución completa y OUTLIERS por grupo: el promedio solo cuenta la historia central — Dos categorías con el mismo mean pueden tener varianzas y outliers mundialmente distintos.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
