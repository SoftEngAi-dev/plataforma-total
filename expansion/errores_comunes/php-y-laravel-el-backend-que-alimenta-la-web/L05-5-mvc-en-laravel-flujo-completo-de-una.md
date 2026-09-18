# ⚠️ Errores comunes — 5. MVC en Laravel: flujo completo de una petición

> PHP y Laravel — El Backend Que Alimenta la Web · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Nada especial» → Frente a «¿Qué hace Route Model Binding en Laravel?» lo fácil es confundirse. **Verdad**: Inyecta directo el modelo por ID (404 automático si no existe) sin hacer find manual. function show(Tarea $tarea) — el framework busca el id y te da el modelo o 404.
- ❌ «Valida forms» → Frente a «¿Qué hace Route Model Binding en Laravel?» lo fácil es confundirse. **Verdad**: Inyecta directo el modelo por ID (404 automático si no existe) sin hacer find manual. function show(Tarea $tarea) — el framework busca el id y te da el modelo o 404.
- ❌ «Indexar» → Frente a «¿Para qué sirve \$fillable en el modelo?» lo fácil es confundirse. **Verdad**: Anti mass-assignment: lista blanca de campos rellenables vía create/update (evita inyectar campos no previstos). Tarea::create($request->all()) protegido: solo pasa lo autorizado.
- ❌ «Migraciones» → Frente a «¿Para qué sirve \$fillable en el modelo?» lo fácil es confundirse. **Verdad**: Anti mass-assignment: lista blanca de campos rellenables vía create/update (evita inyectar campos no previstos). Tarea::create($request->all()) protegido: solo pasa lo autorizado.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
