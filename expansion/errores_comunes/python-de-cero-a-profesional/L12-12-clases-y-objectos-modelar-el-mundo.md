# ⚠️ Errores comunes — 12. Clases y objectos: modelar el mundo

> Python — De Cero a Profesional · Lección 12 · Aprender de los errores (propios y ajenos)

- ❌ «Decoración» → Frente a «¿Qué hace self en un método?» lo fácil es confundirse. **Verdad**: Referencia a la instancia actual: sus atributos y métodos. self es cómo el método sabe sobre QUÉ objeto concreto opera.
- ❌ «Importar la clase» → Frente a «¿Qué hace self en un método?» lo fácil es confundirse. **Verdad**: Referencia a la instancia actual: sus atributos y métodos. self es cómo el método sabe sobre QUÉ objeto concreto opera.
- ❌ «Más velocidad» → Frente a «¿Qué gana @dataclass?» lo fácil es confundirse. **Verdad**: init, repr y eq automáticos para clases de datos. Modelos limpios sin boilerplate: escribes los campos y todo lo demás llega gratis.
- ❌ «Herencia» → Frente a «¿Qué gana @dataclass?» lo fácil es confundirse. **Verdad**: init, repr y eq automáticos para clases de datos. Modelos limpios sin boilerplate: escribes los campos y todo lo demás llega gratis.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
