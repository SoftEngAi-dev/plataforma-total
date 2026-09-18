# ⚠️ Errores comunes — 1. Python: instalación y primer programa

> Python — De Cero a Profesional · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Llaves { }» → Frente a «¿Qué delimita los bloques de código en Python?» lo fácil es confundirse. **Verdad**: La indentación (sangría) de 4 espacios. La sangría forzada hace el código universalmente legible — la idea nuclear de Python.
- ❌ «begin/end» → Frente a «¿Qué delimita los bloques de código en Python?» lo fácil es confundirse. **Verdad**: La indentación (sangría) de 4 espacios. La sangría forzada hace el código universalmente legible — la idea nuclear de Python.
- ❌ «int» → Frente a «input() devuelve siempre...» lo fácil es confundirse. **Verdad**: str (hay que convertir con int()/float() para calcular). Fuente clásica de bugs principiantes: '5' + '5' = '55'. Convierte.
- ❌ «float» → Frente a «input() devuelve siempre...» lo fácil es confundirse. **Verdad**: str (hay que convertir con int()/float() para calcular). Fuente clásica de bugs principiantes: '5' + '5' = '55'. Convierte.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
