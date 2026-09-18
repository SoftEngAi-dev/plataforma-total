# ⚠️ Errores comunes — 4. Laravel: el framework que enamora

> PHP y Laravel — El Backend Que Alimenta la Web · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Un lenguaje» → Frente a «¿Qué es Eloquent?» lo fácil es confundirse. **Verdad**: El ORM de Laravel: cada tabla es un Modelo y trabajas datos como objetos php (save, where, all). Eloquent convierte SQL en interacción con objetos: Tarea::where('hecha', false)->get().
- ❌ «Un motor de vistas» → Frente a «¿Qué es Eloquent?» lo fácil es confundirse. **Verdad**: El ORM de Laravel: cada tabla es un Modelo y trabajas datos como objetos php (save, where, all). Eloquent convierte SQL en interacción con objetos: Tarea::where('hecha', false)->get().
- ❌ «Nada» → Frente a «¿Qué incluye la sintaxis {{ $x }} en Blade que la hace segura?» lo fácil es confundirse. **Verdad**: Escapa HTML automáticamente (anti-XSS por defecto). {!! !!} imprime crudo e inseguro; {{ }} es lo normal y escapeado.
- ❌ «Español» → Frente a «¿Qué incluye la sintaxis {{ $x }} en Blade que la hace segura?» lo fácil es confundirse. **Verdad**: Escapa HTML automáticamente (anti-XSS por defecto). {!! !!} imprime crudo e inseguro; {{ }} es lo normal y escapeado.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
