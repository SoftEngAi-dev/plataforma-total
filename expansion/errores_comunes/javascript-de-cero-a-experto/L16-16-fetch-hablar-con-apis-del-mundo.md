# ⚠️ Errores comunes — 16. fetch: hablar con APIs del mundo

> JavaScript — De Cero a Experto · Lección 16 · Aprender de los errores (propios y ajenos)

- ❌ «En cualquier error HTTP 4xx/5xx» → Frente a «¿Cuándo rechaza fetch (lanza error) SIN ayuda tuya?» lo fácil es confundirse. **Verdad**: Solo en errores de red (sin conexión, CORS, DNS). Por eso el patrón: chequear resp.ok y lanzar tu propio error en 4xx/5xx.
- ❌ «Siempre que resp.ok es false» → Frente a «¿Cuándo rechaza fetch (lanza error) SIN ayuda tuya?» lo fácil es confundirse. **Verdad**: Solo en errores de red (sin conexión, CORS, DNS). Por eso el patrón: chequear resp.ok y lanzar tu propio error en 4xx/5xx.
- ❌ «Accept» → Frente a «¿Qué header obliga al enviar JSON con POST?» lo fácil es confundirse. **Verdad**: Content-Type: application/json. Sin ese header, muchos servidores no interpretan el body como JSON.
- ❌ «Authorization» → Frente a «¿Qué header obliga al enviar JSON con POST?» lo fácil es confundirse. **Verdad**: Content-Type: application/json. Sin ese header, muchos servidores no interpretan el body como JSON.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
