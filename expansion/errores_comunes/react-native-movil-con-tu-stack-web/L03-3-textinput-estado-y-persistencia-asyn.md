# ⚠️ Errores comunes — 3. TextInput, estado y persistencia (AsyncStorage)

> React Native — Móvil con Tu Stack Web · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «e.target.value» → Frente a «¿Cómo se envía texto controlado en RN vs web?» lo fácil es confundirse. **Verdad**: onChangeText recibe el string directamente: setTexto(nuevoTexto). Mismo patrón controlado, pero el callback te da el texto límpio.
- ❌ «No se puede» → Frente a «¿Cómo se envía texto controlado en RN vs web?» lo fácil es confundirse. **Verdad**: onChangeText recibe el string directamente: setTexto(nuevoTexto). Mismo patrón controlado, pero el callback te da el texto límpio.
- ❌ «Una BD SQL» → Frente a «¿Qué es AsyncStorage?» lo fácil es confundirse. **Verdad**: Almacenamiento clave-valor local (equivalente móvil de localStorage), strings+JSON. Guarda strings; con JSON.stringify/parse persistes objetos entre sesiones de app.
- ❌ «Una nube» → Frente a «¿Qué es AsyncStorage?» lo fácil es confundirse. **Verdad**: Almacenamiento clave-valor local (equivalente móvil de localStorage), strings+JSON. Guarda strings; con JSON.stringify/parse persistes objetos entre sesiones de app.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
