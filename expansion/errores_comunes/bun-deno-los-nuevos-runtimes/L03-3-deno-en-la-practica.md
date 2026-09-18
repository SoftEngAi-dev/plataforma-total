# ⚠️ Errores comunes — 3. Deno en la práctica

> 🍞 Bun & Deno — Los Nuevos Runtimes · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Funciona igual» → Frente a «¿Qué pasa si un script de Deno usa la red sin --allow-net?» lo fácil es confundirse. **Verdad**: Deno lanza PermissionDenied y bloquea la operación. El sandbox de Deno exige permisos explícitos por recurso: seguridad real por defecto.
- ❌ «Lo reporta por email» → Frente a «¿Qué pasa si un script de Deno usa la red sin --allow-net?» lo fácil es confundirse. **Verdad**: Deno lanza PermissionDenied y bloquea la operación. El sandbox de Deno exige permisos explícitos por recurso: seguridad real por defecto.
- ❌ «Solo el runtime» → Frente a «¿Qué herramientas trae Deno integradas sin configuración?» lo fácil es confundirse. **Verdad**: fmt, lint y test (además de compile). deno fmt, deno lint, deno test y deno compile vienen de serie: toolchain todo-en-uno.
- ❌ «Photoshop» → Frente a «¿Qué herramientas trae Deno integradas sin configuración?» lo fácil es confundirse. **Verdad**: fmt, lint y test (además de compile). deno fmt, deno lint, deno test y deno compile vienen de serie: toolchain todo-en-uno.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
