# ⚠️ Errores comunes — 4. Proyecto: API REST completa+cliente que la consume

> APIs REST y HTTP — El Idioma de los Servidores · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Por castigo» → Frente a «¿Por qué testear el cliente CON EL API APAGADA?» lo fácil es confundirse. **Verdad**: El mundo real: redes caen siempre; tu cliente debe manejar errores de conexión con gracia, no un traceback. Resiliencia honesta: probar el camino triste es parte del camino profesional.
- ❌ «Sin motivo» → Frente a «¿Por qué testear el cliente CON EL API APAGADA?» lo fácil es confundirse. **Verdad**: El mundo real: redes caen siempre; tu cliente debe manejar errores de conexión con gracia, no un traceback. Resiliencia honesta: probar el camino triste es parte del camino profesional.
- ❌ «Nada especial» → Frente a «¿Qué hace especial al acceso a /docs de FastAPI?» lo fácil es confundirse. **Verdad**:  Swagger generado automáticamente de tus tipos: probar tu API en vivo desde el navegador, documentación incluida. Value real: es tu documentacíon VIVA sin ninguna pieza extra de código your part.
- ❌ «Caché» → Frente a «¿Qué hace especial al acceso a /docs de FastAPI?» lo fácil es confundirse. **Verdad**:  Swagger generado automáticamente de tus tipos: probar tu API en vivo desde el navegador, documentación incluida. Value real: es tu documentacíon VIVA sin ninguna pieza extra de código your part.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
