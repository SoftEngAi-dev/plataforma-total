# ⚠️ Errores comunes — 8. Proyecto: app de notas con todo el curso

> React — Interfaces Modernas y Reutilizables · Lección 8 · Aprender de los errores (propios y ajenos)

- ❌ «notas[idx].texto = x» → Frente a «¿Cómo editar una nota inmutablemente en un array de estado?» lo fácil es confundirse. **Verdad**: map que devuelve objeto nuevo {...n, texto: x} solo para el id coincidente. map con spread: reemplazas el objeto con uno NUEVO; referencias nuevas → React entiende y la UI se actualiza.
- ❌ «splice y setState» → Frente a «¿Cómo editar una nota inmutablemente en un array de estado?» lo fácil es confundirse. **Verdad**: map que devuelve objeto nuevo {...n, texto: x} solo para el id coincidente. map con spread: reemplazas el objeto con uno NUEVO; referencias nuevas → React entiende y la UI se actualiza.
- ❌ «fetch + axios» → Frente a «¿Qué dos APIs persisten las notas en esta app?» lo fácil es confundirse. **Verdad**: useState + useEffect dentro de un custom hook useLocalStorage. Estado + efecto que escribe a localStorage: patrón simple, potente y reutilizable.
- ❌ «Redux + thunk» → Frente a «¿Qué dos APIs persisten las notas en esta app?» lo fácil es confundirse. **Verdad**: useState + useEffect dentro de un custom hook useLocalStorage. Estado + efecto que escribe a localStorage: patrón simple, potente y reutilizable.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
