# ⚠️ Errores comunes — 5. Express + estructura real + variables de entorno

> Node.js — JavaScript en el Servidor · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Por velocidad» → Frente a «¿Por qué los secretos van en variables de entorno y no en el código?» lo fácil es confundirse. **Verdad**: Para no publicarlos en git y poder variarlos por entorno (dev/prod). Código público + secretos = filtración. .env + .gitignore es la norma; nunca commitees el .env.
- ❌ «Porque .env es más rápido» → Frente a «¿Por qué los secretos van en variables de entorno y no en el código?» lo fácil es confundirse. **Verdad**: Para no publicarlos en git y poder variarlos por entorno (dev/prod). Código público + secretos = filtración. .env + .gitignore es la norma; nunca commitees el .env.
- ❌ «Nada útil» → Frente a «¿Qué aporta separar app.js de index.js (listen)?» lo fácil es confundirse. **Verdad**: Puedes importar y TESTEAR la app sin abrir puerto; separa configuración de ejecución. La app testeable se exporta sin listen; en tests corren peticiones contra ella con supertest.
- ❌ «Es solo estética» → Frente a «¿Qué aporta separar app.js de index.js (listen)?» lo fácil es confundirse. **Verdad**: Puedes importar y TESTEAR la app sin abrir puerto; separa configuración de ejecución. La app testeable se exporta sin listen; en tests corren peticiones contra ella con supertest.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
