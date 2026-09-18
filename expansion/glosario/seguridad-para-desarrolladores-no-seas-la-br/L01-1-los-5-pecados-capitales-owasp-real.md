# 📖 Glosario — 1. Los 5 pecados capitales (OWASP real)

> Seguridad para Desarrolladores — No Seas la Brecha · Lección 1 · Términos que debes poder definir sin mirar

- **Broken Access Control: cambiar el ID en la URL y acceder a datos de OTROS usuarios porque el servidor no verifica propiedad** — /perfil/1 → cambias a /perfil/2 y ves datos ajenos si el servidor no checkea dueño.
- **Hash con bcrypt/argon2 + salt: ni siquiera tú (admin) puedes leerlas** — El hash robusto es irreversible y lento a propósito: el que dicen los propios hashes débiles.

✍️ Ejercicio: añade debajo TU propia definición de cada término.
