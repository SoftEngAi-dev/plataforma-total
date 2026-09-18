# ⚠️ Errores comunes — 5. Clases en TS: private, readonly e implements

> TypeScript — JavaScript con Superpoderes y Seguridad · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Acceso desde任何地方» → Frente a «¿Qué permite una propiedad private?» lo fácil es confundirse. **Verdad**: Solo acceso dentro de la propia clase. Encapsulación: el estado interno solo cambia por métodos controlados.
- ❌ «Solo lectura universal» → Frente a «¿Qué permite una propiedad private?» lo fácil es confundirse. **Verdad**: Solo acceso dentro de la propia clase. Encapsulación: el estado interno solo cambia por métodos controlados.
- ❌ «Copiar código de otra clase» → Frente a «¿Para qué sirve implements?» lo fácil es confundirse. **Verdad**: Obligar a la clase a cumplir el contrato de una interface. El compilador verifica que cumples el contrato — la base de sustituir implementaciones (mocks, DBs).
- ❌ «Importar módulos» → Frente a «¿Para qué sirve implements?» lo fácil es confundirse. **Verdad**: Obligar a la clase a cumplir el contrato de una interface. El compilador verifica que cumples el contrato — la base de sustituir implementaciones (mocks, DBs).

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
