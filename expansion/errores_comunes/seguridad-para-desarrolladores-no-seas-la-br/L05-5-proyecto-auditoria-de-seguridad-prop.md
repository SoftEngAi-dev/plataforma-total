# ⚠️ Errores comunes — 5. Proyecto: auditoría de seguridad propia

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué descubre pegar <script>alert(1)</script> en un campo y probar?» lo fácil es confundirse. **Verdad**: Si ves el alert: tu app ejecuta código de usuario = XSS confirmado. La prueba ácida manual del XSS: si JS injectado corre, tu escape no es suficiente.
- ❌ «El backend» → Frente a «¿Qué descubre pegar <script>alert(1)</script> en un campo y probar?» lo fácil es confundirse. **Verdad**: Si ves el alert: tu app ejecuta código de usuario = XSS confirmado. La prueba ácida manual del XSS: si JS injectado corre, tu escape no es suficiente.
- ❌ «Aburrido» → Frente a «¿Por qué testear IDOR es tan crítico para endpoints con IDs?» lo fácil es confundirse. **Verdad**: Es la vulnerabilidad web nº1 real: chequear que solo el DUEÑO accede a su recurso por cada request. La lección: no confíes en la URL escondida: cada query/id verifica ownership server-side.
- ❌ «Backend only» → Frente a «¿Por qué testear IDOR es tan crítico para endpoints con IDs?» lo fácil es confundirse. **Verdad**: Es la vulnerabilidad web nº1 real: chequear que solo el DUEÑO accede a su recurso por cada request. La lección: no confíes en la URL escondida: cada query/id verifica ownership server-side.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
