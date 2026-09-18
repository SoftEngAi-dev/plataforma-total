# 🎤 Banco de entrevista — Pandas — Excel con Superpoderes en Python

> 12 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué devuelve datos[datos['edad'] > 40]?**
   - Filas del DataFrame donde la condición booleana es verdadera  _(Boolean indexing: la forma panda de decir 'WHERE edad > 40'.)_

2. **¿Cuándo usar datos.loc vs datos.iloc?**
   - loc: por ETIQUETA/condición; iloc: por POSICIÓN de entero  _(loc[[2,3], ['a']] por nombre; iloc[0:2, 0] por posición. Ambos según el índice.)_

3. **¿Qué hace df.isna().sum()?**
   - Cuenta valores faltantes POR COLUMNA: la primera revisión de salud de un dataset  _(Antes de analizar: ¿cuántos huecos hay y dónde? Ahí decides tu estrategia de limpieza.)_

4. **¿fillna con la mediana vs dropna?**
   - fillna conserva todas las filas imputando un valor neutro; dropna las elimina — depende del caso  _(Poquitas filas → drop; muchas → imputar. La mediana es robusta a outliers.)_

5. **¿Qué hace df['categoria'].value_counts()?**
   - Cuenta frecuencia de cada valor: la vía rápida de 'top categorías' sin SQL  _(El one-liner favorito: en 1 llamada tienes el panorama categorial más común.)_

6. **pd.merge(a, b, on='id', how='left') se comporta como...**
   - LEFT JOIN de SQL: todas las filas de 'a' + datos de 'b' cuando hay coincidencia en id  _(merge=JOIN entre DataFrames por clave; how decide qué filas sobreviven.)_

7. **¿Qué permite df['fecha'].dt.month después de to_datetime?**
   - Extraer partes de fecha (mes/año/día/nombre) VECTORIZADO sobre toda la columna  _(El accesor .dt convierte fechas en datos analizables: estacionalidad, agrupar por mes...)_

8. **df['email'].str.contains('silva', na=False) — ¿por qué na=False?**
   - contains con NA devuelve NA y rompe filtros booleanos: na=False lo maneja seguro  _(Detalle que evita un error común al filtrar strings con valores faltantes.)_

9. **¿Cuál gráfico muestra relación entre dos numéricos?**
   - scatterplot: cada punto una observación - revela correlaciones, clusters y outliers de un vistazo  _(Dispersión = radiografía de relaciones: la intuición primera de cualquier análisis bivariado.)_

10. **¿Qué revela un boxplot por categoría que un promedio no?**
   - Distribución completa y OUTLIERS por grupo: el promedio solo cuenta la historia central  _(Dos categorías con el mismo mean pueden tener varianzas y outliers mundialmente distintos.)_

11. **¿Qué verifica 'Restart Kernel & Run All'?**
   - Que tu notebook se ejecute limpio de arriba a abajo en orden — reproducibilidad real de tu análisis  _(Orden del código más importante: tu análisis debe reproducirse sin celdas corridas a desorden.)_

12. **¿Por qué df.groupby('Pclass')['Survived'].mean() da la tasa de supervivencia?**
   - El promedio de una columna 0/1 = la proporción/tasa: mean de binarios es tasa universal  _(El truco universal de datos: promediar flags 0/1 te da porcentajes directos en una línea.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Pandas y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Pandas con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
