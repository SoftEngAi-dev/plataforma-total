# ⚠️ Errores comunes — 3. FastAPI: APIs con Python + TypeScript feel

> APIs REST y HTTP — El Idioma de los Servidores · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué hace BaseModel de pydantic?» lo fácil es confundirse. **Verdad**: Esquema+validación automática de tus request bodies: si el usuario envía mal, 422 sin escribir código tú. TareaIn(titulo: str) garantiza str: errores de formato rechazados de fábrica (esa es la magia atrás de FastAPI).
- ❌ «Only types» → Frente a «¿Qué hace BaseModel de pydantic?» lo fácil es confundirse. **Verdad**: Esquema+validación automática de tus request bodies: si el usuario envía mal, 422 sin escribir código tú. TareaIn(titulo: str) garantiza str: errores de formato rechazados de fábrica (esa es la magia atrás de FastAPI).
- ❌ «Nada» → Frente a «¿Qué dos cosas vienen GRATIS con FastAPI y ningún otro backend básico?» lo fácil es confundirse. **Verdad**: Swagger interactivo en /docs (probar la API desde el navegador) + validación automática. Auto-docs + auto-valid: tu API se explica y se respeta sola.
- ❌ «Base de datos» → Frente a «¿Qué dos cosas vienen GRATIS con FastAPI y ningún otro backend básico?» lo fácil es confundirse. **Verdad**: Swagger interactivo en /docs (probar la API desde el navegador) + validación automática. Auto-docs + auto-valid: tu API se explica y se respeta sola.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
