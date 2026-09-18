# ⚠️ Errores comunes — 13. El DOM: convertir HTML en objeto vivo

> JavaScript — De Cero a Experto · Lección 13 · Aprender de los errores (propios y ajenos)

- ❌ «innerHTML» → Frente a «¿Qué método es seguro para insertar TEXTO de usuario en la página?» lo fácil es confundirse. **Verdad**: textContent. textContent no interpreta HTML: protege contra inyección XSS básica.
- ❌ «eval()» → Frente a «¿Qué método es seguro para insertar TEXTO de usuario en la página?» lo fácil es confundirse. **Verdad**: textContent. textContent no interpreta HTML: protege contra inyección XSS básica.
- ❌ «Siempre la añade» → Frente a «¿Qué hace el.classList.toggle('activa')?» lo fácil es confundirse. **Verdad**: La añade si no está, la quita si está. Toggle = interruptor: perfecto para menús, modos oscuro/claro, etc.
- ❌ «Siempre la quita» → Frente a «¿Qué hace el.classList.toggle('activa')?» lo fácil es confundirse. **Verdad**: La añade si no está, la quita si está. Toggle = interruptor: perfecto para menús, modos oscuro/claro, etc.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
