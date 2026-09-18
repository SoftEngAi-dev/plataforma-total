# ⚠️ Errores comunes — 2. Errores a la vista: el if err != nil filosófico

> Go — El Lenguaje de la Nube · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «No pueden» → Frente a «¿Por qué Go no tiene excepciones para errores esperables?» lo fácil es confundirse. **Verdad**: Diseño deliberado: errores como valores devueltos obligan a manejarlos conscientemente y flujo de control visible. En Go el manejo de error no se esconde en catch lejanos: está cara a cara contigo.
- ❌ «Son lentas» → Frente a «¿Por qué Go no tiene excepciones para errores esperables?» lo fácil es confundirse. **Verdad**: Diseño deliberado: errores como valores devueltos obligan a manejarlos conscientemente y flujo de control visible. En Go el manejo de error no se esconde en catch lejanos: está cara a cara contigo.
- ❌ «un bug» → Frente a «if err != nil es...» lo fácil es confundirse. **Verdad**: El patrón universal de Go para comprobar y manejar errores devueltos por cada operación fallible. Todos los libros lo bromean, todos los proyectos sanos lo escriben sin pereza.
- ❌ «opcional» → Frente a «if err != nil es...» lo fácil es confundirse. **Verdad**: El patrón universal de Go para comprobar y manejar errores devueltos por cada operación fallible. Todos los libros lo bromean, todos los proyectos sanos lo escriben sin pereza.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
