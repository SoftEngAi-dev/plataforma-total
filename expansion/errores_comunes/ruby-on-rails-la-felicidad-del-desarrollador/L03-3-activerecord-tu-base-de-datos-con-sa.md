# ⚠️ Errores comunes — 3. ActiveRecord: tu base de datos con sabor Ruby

> Ruby on Rails — La Felicidad del Desarrollador · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Decora» → Frente a «¿Qué hace validates :titulo, presence: true?» lo fácil es confundirse. **Verdad**: Rechaza guardar si falta el título; el objeto retorna valid? false con errores. Validaciones a nivel MODELO = defensa total (formulario, API, consola).
- ❌ «Borra» → Frente a «¿Qué hace validates :titulo, presence: true?» lo fácil es confundirse. **Verdad**: Rechaza guardar si falta el título; el objeto retorna valid? false con errores. Validaciones a nivel MODELO = defensa total (formulario, API, consola).
- ❌ «Nada» → Frente a «has_many :posts presupone...» lo fácil es confundirse. **Verdad**: Que la tabla posts tiene columna autor_id (convención Rails que la FK sigue el modelo singular+_id). Por convención no tienes que decírselo: la FK es visible: autor_id.
- ❌ «Que tiene un índice» → Frente a «has_many :posts presupone...» lo fácil es confundirse. **Verdad**: Que la tabla posts tiene columna autor_id (convención Rails que la FK sigue el modelo singular+_id). Por convención no tienes que decírselo: la FK es visible: autor_id.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
