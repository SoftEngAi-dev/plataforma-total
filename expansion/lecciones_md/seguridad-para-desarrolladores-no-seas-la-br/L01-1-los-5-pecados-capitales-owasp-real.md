# 1. Los 5 pecados capitales (OWASP real)

> 📚 Curso: **Seguridad para Desarrolladores — No Seas la Brecha** · Lección 1 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
SEGURIDAD SIN PARANOIA: LO QUE ROMPE EL MUNDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
OWASP Top 10 (las vulnerabilidades MÁS explotadas del mundo, estudiadas en datos reales)
TUS 5 QUE CAUSAN EL 90% DEL DAÑO:

1. 🔓 BROKEN ACCESS CONTROL — cualquiera accede a lo que no debe:
   /admin solo con @login_required NO BASTA: chequea ROL en cada endpoint.
   /api/usuarios/123/expediente → ¿verificás que soy DUEÑO del 123? (IDOR: cambiar el id en la URL y ver datos ajenos)
2. 💉 INYECCIÓN (SQL/Command): datos del usuario interpretados como código.
   "SELECT * WHERE name = '" + input + "'" → ' OR '1'='1 -- destruye login. Prepared statements SIEMPRE.
3. 🍪 FALLAS DE AUTENTICACIÓN: contraseñas en texto plano en la BD (¡!), sesiones que no expiran, sin límite de intentos.
   Contraseñas: hash con bcrypt/argon2 (NUNCA MD5/SHA1 plano).
4. ⚙️ MISCONFIG: debug=True en producción, errores con stacktrace a usuarios, headers por defecto, puertos abiertos de más.
5. 📦 DEPENDENCIAS VULNERABLES: npm install viejo con CVEs abiertas.
   pip-audit / npm audit / dependabot → actualiza lo que instalas.

PRINCIPIO RECTOR: NUNCA CONFIAR EN DATOS DEL USUARIO (entrada = potencial ataque hasta demostrar lo contrario).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es IDOR?
- A) Un hámster
- B) Broken Access Control: cambiar el ID en la URL y acceder a datos de OTROS usuarios porque el servidor no verifica propiedad
- C) Una base de datos
- D) Un virus
### 2. ¿Cómo se guardan contraseñas correctamente?
- A) Texto plano
- B) MD5
- C) Hash con bcrypt/argon2 + salt: ni siquiera tú (admin) puedes leerlas
- D) Base64

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Broken Access Control: cambiar el ID en la URL y acceder a datos de OTROS usuarios porque el servidor no verifica propiedad — /perfil/1 → cambias a /perfil/2 y ves datos ajenos si el servidor no checkea dueño.
**2.** ✅ Hash con bcrypt/argon2 + salt: ni siquiera tú (admin) puedes leerlas — El hash robusto es irreversible y lento a propósito: el que dicen los propios hashes débiles.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
