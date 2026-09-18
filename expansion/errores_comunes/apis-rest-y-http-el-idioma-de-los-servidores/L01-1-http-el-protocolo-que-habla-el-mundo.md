# ⚠️ Errores comunes — 1. HTTP: el protocolo que habla el mundo

> APIs REST y HTTP — El Idioma de los Servidores · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Ninguna» → Frente a «¿Cuál es la diferencia entre 401 y 403?» lo fácil es confundirse. **Verdad**: 401 = falta autenticación (quién eres); 403 = ya sé quién eres pero NO tienes permiso. Autenticación vs autorización: la confusión más común en APIs.
- ❌ «404» → Frente a «¿Cuál es la diferencia entre 401 y 403?» lo fácil es confundirse. **Verdad**: 401 = falta autenticación (quién eres); 403 = ya sé quién eres pero NO tienes permiso. Autenticación vs autorización: la confusión más común en APIs.
- ❌ «Es lento» → Frente a «¿Qué significa que GET sea idempotente?» lo fácil es confundirse. **Verdad**: Repetirlo N veces tiene el mismo efecto que 1: exige NO cambiar estado por definición REST. GET/PUT/DELETE= idempotentes; POST no: eso decide reintentos seguros en tu cliente.
- ❌ «Es seguro contra hackers» → Frente a «¿Qué significa que GET sea idempotente?» lo fácil es confundirse. **Verdad**: Repetirlo N veces tiene el mismo efecto que 1: exige NO cambiar estado por definición REST. GET/PUT/DELETE= idempotentes; POST no: eso decide reintentos seguros en tu cliente.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
