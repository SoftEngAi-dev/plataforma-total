# ⚠️ Errores comunes — 9. Archivos: leer, escribir y JSON

> Python — De Cero a Profesional · Lección 9 · Aprender de los errores (propios y ajenos)

- ❌ «Es más corto» → Frente a «¿Por qué usar with open(...)?» lo fácil es confundirse. **Verdad**: Cierra el archivo automáticamente incluso ante errores. with = context manager: el recurso se libera pase lo que pase.
- ❌ «Acelera la lectura» → Frente a «¿Por qué usar with open(...)?» lo fácil es confundirse. **Verdad**: Cierra el archivo automáticamente incluso ante errores. with = context manager: el recurso se libera pase lo que pase.
- ❌ «write con str()» → Frente a «¿Cómo guardar y recuperar un dict en JSON?» lo fácil es confundirse. **Verdad**: json.dump() y json.load(). json es universal multiplataforma; dicts/listas pasan directo.
- ❌ «pikcle y unpack» → Frente a «¿Cómo guardar y recuperar un dict en JSON?» lo fácil es confundirse. **Verdad**: json.dump() y json.load(). json es universal multiplataforma; dicts/listas pasan directo.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
