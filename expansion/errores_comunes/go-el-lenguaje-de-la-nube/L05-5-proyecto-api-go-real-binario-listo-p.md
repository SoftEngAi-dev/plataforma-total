# ⚠️ Errores comunes — 5. Proyecto: API Go real + binario listo para producción

> Go — El Lenguaje de la Nube · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué permite go build + cross-compilation?» lo fácil es confundirse. **Verdad**: Un único binario estático por SO/arquitectura sin dependencias: deployment es 'copiar y correr'. produce.exe final: sin JVM/python en el server — eso lo aprecian mucho en operaciones.
- ❌ «npm» → Frente a «¿Qué permite go build + cross-compilation?» lo fácil es confundirse. **Verdad**: Un único binario estático por SO/arquitectura sin dependencias: deployment es 'copiar y correr'. produce.exe final: sin JVM/python en el server — eso lo aprecian mucho en operaciones.
- ❌ «Para más RAM» → Frente a «¿Por qué sync.RWMutex con la slice global en la API?» lo fácil es confundirse. **Verdad**: Lecturas/escrituras concurrentes sobre memoria compartida pueden corromperse: el mutex las sincroniza. Varios requests golpean la misma estructura a la vez: sincronización obligatoria o data race.
- ❌ «Es moda» → Frente a «¿Por qué sync.RWMutex con la slice global en la API?» lo fácil es confundirse. **Verdad**: Lecturas/escrituras concurrentes sobre memoria compartida pueden corromperse: el mutex las sincroniza. Varios requests golpean la misma estructura a la vez: sincronización obligatoria o data race.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
