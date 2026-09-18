# ⚠️ Errores comunes — 15. Python para datos: tu primer análisis real

> Python — De Cero a Profesional · Lección 15 · Aprender de los errores (propios y ajenos)

- ❌ «Lee JSON» → Frente a «¿Qué hace csv.DictReader?» lo fácil es confundirse. **Verdad**: Convierte cada fila del CSV en un dict usando el encabezado como claves. fila['precio'] directo — parseo CSV robusto con nada instalado.
- ❌ «Escribe CSV» → Frente a «¿Qué hace csv.DictReader?» lo fácil es confundirse. **Verdad**: Convierte cada fila del CSV en un dict usando el encabezado como claves. fila['precio'] directo — parseo CSV robusto con nada instalado.
- ❌ «Filtra filas» → Frente a «df.groupby('producto')['total'].sum() hace...» lo fácil es confundirse. **Verdad**: Agrupa por producto y suma el total de cada grupo. El GROUP BY de SQL, estilo pandas: resumir categorías en 1 línea.
- ❌ «Ordena por producto» → Frente a «df.groupby('producto')['total'].sum() hace...» lo fácil es confundirse. **Verdad**: Agrupa por producto y suma el total de cada grupo. El GROUP BY de SQL, estilo pandas: resumir categorías en 1 línea.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
