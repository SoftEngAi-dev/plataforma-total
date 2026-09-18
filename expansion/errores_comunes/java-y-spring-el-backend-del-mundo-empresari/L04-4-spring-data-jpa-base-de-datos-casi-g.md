# ⚠️ Errores comunes — 4. Spring Data JPA: base de datos casi gratis

> Java y Spring — El Backend del Mundo Empresarial · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Nada» → Frente a «¿Qué hace JpaRepository con findByHechaFalse()?» lo fácil es confundirse. **Verdad**: Spring Data genera la query automáticamente a partir del NOMBRE del método (derivada por convención). Query derivation: nombras bien el método, la query existe sin escribirla.
- ❌ «SQL manual» → Frente a «¿Qué hace JpaRepository con findByHechaFalse()?» lo fácil es confundirse. **Verdad**: Spring Data genera la query automáticamente a partir del NOMBRE del método (derivada por convención). Query derivation: nombras bien el método, la query existe sin escribirla.
- ❌ «Decoración» → Frente a «¿Qué papel tiene @Entity?» lo fácil es confundirse. **Verdad**: Marca la clase como tabla de BD manejada por el ORM (cada instancia = fila). El mapeo objeto-relacional (ORM): objetos Java ↔ filas SQL.
- ❌ «Seguridad» → Frente a «¿Qué papel tiene @Entity?» lo fácil es confundirse. **Verdad**: Marca la clase como tabla de BD manejada por el ORM (cada instancia = fila). El mapeo objeto-relacional (ORM): objetos Java ↔ filas SQL.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
