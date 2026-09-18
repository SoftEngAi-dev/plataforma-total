# ⚠️ Errores comunes — 1. Los 5 pecados capitales (OWASP real)

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Un hámster» → Frente a «¿Qué es IDOR?» lo fácil es confundirse. **Verdad**: Broken Access Control: cambiar el ID en la URL y acceder a datos de OTROS usuarios porque el servidor no verifica propiedad. /perfil/1 → cambias a /perfil/2 y ves datos ajenos si el servidor no checkea dueño.
- ❌ «Una base de datos» → Frente a «¿Qué es IDOR?» lo fácil es confundirse. **Verdad**: Broken Access Control: cambiar el ID en la URL y acceder a datos de OTROS usuarios porque el servidor no verifica propiedad. /perfil/1 → cambias a /perfil/2 y ves datos ajenos si el servidor no checkea dueño.
- ❌ «Texto plano» → Frente a «¿Cómo se guardan contraseñas correctamente?» lo fácil es confundirse. **Verdad**: Hash con bcrypt/argon2 + salt: ni siquiera tú (admin) puedes leerlas. El hash robusto es irreversible y lento a propósito: el que dicen los propios hashes débiles.
- ❌ «MD5» → Frente a «¿Cómo se guardan contraseñas correctamente?» lo fácil es confundirse. **Verdad**: Hash con bcrypt/argon2 + salt: ni siquiera tú (admin) puedes leerlas. El hash robusto es irreversible y lento a propósito: el que dicen los propios hashes débiles.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
