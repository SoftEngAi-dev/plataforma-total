# ⚠️ Errores comunes — 6. Proyecto final: EDA completo de un dataset público

> Pandas — Excel con Superpoderes en Python · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué verifica 'Restart Kernel & Run All'?» lo fácil es confundirse. **Verdad**: Que tu notebook se ejecute limpio de arriba a abajo en orden — reproducibilidad real de tu análisis. Orden del código más importante: tu análisis debe reproducirse sin celdas corridas a desorden.
- ❌ «Es más rápido» → Frente a «¿Qué verifica 'Restart Kernel & Run All'?» lo fácil es confundirse. **Verdad**: Que tu notebook se ejecute limpio de arriba a abajo en orden — reproducibilidad real de tu análisis. Orden del código más importante: tu análisis debe reproducirse sin celdas corridas a desorden.
- ❌ «Por casualidad» → Frente a «¿Por qué df.groupby('Pclass')['Survived'].mean() da la tasa de supervivencia?» lo fácil es confundirse. **Verdad**: El promedio de una columna 0/1 = la proporción/tasa: mean de binarios es tasa universal. El truco universal de datos: promediar flags 0/1 te da porcentajes directos en una línea.
- ❌ «Es solo moda» → Frente a «¿Por qué df.groupby('Pclass')['Survived'].mean() da la tasa de supervivencia?» lo fácil es confundirse. **Verdad**: El promedio de una columna 0/1 = la proporción/tasa: mean de binarios es tasa universal. El truco universal de datos: promediar flags 0/1 te da porcentajes directos en una línea.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
