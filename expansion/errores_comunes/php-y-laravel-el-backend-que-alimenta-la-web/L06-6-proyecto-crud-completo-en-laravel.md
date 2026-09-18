# ⚠️ Errores comunes — 6. Proyecto: CRUD completo en Laravel

> PHP y Laravel — El Backend Que Alimenta la Web · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué genera Route::resource()» lo fácil es confundirse. **Verdad**: Las 7 rutas CRUD convencionales (index/create/store/show/edit/update/destroy) de golpe. Convención sobre configuración: Laravel asume la estructura estándar de recursos REST.
- ❌ «Vistas» → Frente a «¿Qué genera Route::resource()» lo fácil es confundirse. **Verdad**: Las 7 rutas CRUD convencionales (index/create/store/show/edit/update/destroy) de golpe. Convención sobre configuración: Laravel asume la estructura estándar de recursos REST.
- ❌ «CSS» → Frente a «¿Qué pone el @csrf dentro del <form> de Blade?» lo fácil es confundirse. **Verdad**: Un token anti-CSRF oculto — todo POST sin token es rechazado por Laravel. CSRF protection integrada: solo formularios nacidos en tu app pueden postear.
- ❌ «JavaScript» → Frente a «¿Qué pone el @csrf dentro del <form> de Blade?» lo fácil es confundirse. **Verdad**: Un token anti-CSRF oculto — todo POST sin token es rechazado por Laravel. CSRF protection integrada: solo formularios nacidos en tu app pueden postear.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
