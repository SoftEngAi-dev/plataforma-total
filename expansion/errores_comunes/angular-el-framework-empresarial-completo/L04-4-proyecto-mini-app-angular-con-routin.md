# ⚠️ Errores comunes — 4. Proyecto: mini-app Angular con routing

> Angular — El Framework Empresarial Completo · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «En cada componente» → Frente a «¿Dónde debe vivir el estado compartido en Angular?» lo fácil es confundirse. **Verdad**: En un servicio inyectable root: componentes lo inyectan y leen sus signals. Single source of truth en servicio = la pantalla siempre consistente.
- ❌ «En el template» → Frente a «¿Dónde debe vivir el estado compartido en Angular?» lo fácil es confundirse. **Verdad**: En un servicio inyectable root: componentes lo inyectan y leen sus signals. Single source of truth en servicio = la pantalla siempre consistente.
- ❌ «ng-repeat» → Frente a «¿Cuál es el equivalente moderno a *ngFor en Angular 17+?» lo fácil es confundirse. **Verdad**: Bloque de control nativo: @for (item of lista(); track item.id) { ... }. @for/@if en el template: sin imports extra, tracking explícito y más performance.
- ❌ «v-for» → Frente a «¿Cuál es el equivalente moderno a *ngFor en Angular 17+?» lo fácil es confundirse. **Verdad**: Bloque de control nativo: @for (item of lista(); track item.id) { ... }. @for/@if en el template: sin imports extra, tracking explícito y más performance.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
