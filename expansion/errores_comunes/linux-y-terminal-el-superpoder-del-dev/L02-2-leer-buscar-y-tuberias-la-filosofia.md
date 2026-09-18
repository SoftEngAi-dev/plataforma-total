# ⚠️ Errores comunes — 2. Leer, buscar y tuberías: la filosofía Unix

> Linux y Terminal — El Superpoder del Dev · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Muestra todo» → Frente a «cat log | grep ERROR | wc -l hace...» lo fácil es confundirse. **Verdad**: Cuenta las líneas del log que contienen ERROR (tuberías encadenadas). Filtro → contador: las tuberías componen herramientas con texto crudo.
- ❌ «Borra errores» → Frente a «cat log | grep ERROR | wc -l hace...» lo fácil es confundirse. **Verdad**: Cuenta las líneas del log que contienen ERROR (tuberías encadenadas). Filtro → contador: las tuberías componen herramientas con texto crudo.
- ❌ «Ninguna» → Frente a «¿Diferencia entre > y >>?» lo fácil es confundirse. **Verdad**: > SOBRESCRIBE el archivo; >> AGREGA al final. Confundirlos = perder archivos (factor real de incidentes).
- ❌ «>> es para errores» → Frente a «¿Diferencia entre > y >>?» lo fácil es confundirse. **Verdad**: > SOBRESCRIBE el archivo; >> AGREGA al final. Confundirlos = perder archivos (factor real de incidentes).

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
