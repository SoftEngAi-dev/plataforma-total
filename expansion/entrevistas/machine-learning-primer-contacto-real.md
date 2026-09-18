# 🎤 Banco de entrevista — Machine Learning — Primer Contacto Real

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Cuál es la REGLA SAGRADA del ML?**
   - Evaluar en datos de TEST separados que el modelo nunca vio en entrenamiento  _(Sin test separado solo mides memoria, no capacidad de generalizar.)_

2. **Precio de una casa según m², zona, habitaciones es...**
   - REGRESIÓN: predecir un NÚMERO (continuo), no una categoría  _(Regresión = número; clasificación = etiqueta/categoría. Letra chica que decide tu modelo.)_

3. **¿Qué hacen fit() y predict() en sklearn?**
   - fit aprende de datos de ENTRENAMIENTO; predict va'ven predicciones sobre datos nuevos  _(API universal: instanciar modelo→fit(X_train, y)→predict(X) repite en toda sklearn.)_

4. **¿Para qué sirve la matriz de confusión?**
   - Ver no solo AL error sino QUÉ se confunde con QUÉ: errores específicos por clase  _(Diagonal = aciertos; fuera de diagonal = confusiones específicas que guían mejora.)_

5. **Train 99%, test 72%. ¿Diagnóstico?**
   - OVERFIT: memorizó el entrenamiento, no generaliza — modelo demasiado complejo para los datos  _(La brecha train>>test es el síntoma canónico de sobreajuste.)_

6. **¿Qué aporta cross_val_score(modelo, X, y, cv=5) sobre un solo split?**
   - Evalúa 5 veces con particiones rotadas: medida mucho más estable y robusta de tu desempeño real  _(Un solo split puede tener suerte/mala suerte con qué datos tocaron: la CV promedia esa lotería.)_

7. **¿Qué ventaja práctica tiene max_depth=3?**
   - Limita la complejidad del árbol: techo de cristal al overfit (regularización por construcción)  _(Árbol profundo = reglas sobreajustadas de poquitas muestras; poco profundo generaliza bien.)_

8. **¿Qué te dice feature_importances_?**
   - QUÉ VARIABLES pesan más en las decisiones del modelo: comprensión/explicación del negocio incluida  _("Los 2 mejores predictores son..." directo del bosque: insights accionables.)_

9. **¿Qué hace pd.get_dummies sobre columnas categóricas?**
   - Convierte categorías en columnas binarias 0/1 para que el algoritmo procese números  _(Los modelos comen números: género/embarque/categorías → one-hot encoding.)_

10. **¿Qué es FEATURE ENGINEERING en este proyecto?**
   - CREAR columnas útiles desde las existentes (ej: sol@ si viajas solo): el 40% de tu mejora suele vivir aquí  _(Pequeñas obviedades transformadas en datos = a veces más valor que elegir otro modelo.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Machine Learning y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Machine Learning con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
