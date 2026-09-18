# 3. Autenticación moderna: sesiones, JWT y OAuth

> 📚 Curso: **Seguridad para Desarrolladores — No Seas la Brecha** · Lección 3 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
LOGIN 2026: 3 FORMAS, TODAS COMPRENDIDAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. SESIONES CLÁSICAS (estado en el SERVIDOR, seguro y sencillo)
   Login → BD guarda session_id → cookie HttpOnly la lleva → cada request la verifica.
   Pros: revocación fácil (borras sesión); Contras: servidor mantiene estado (memoria/Redis).
2. JWT (JSON Web Token, el estado viaja FIRMADO)
   El servidor firma payload + tu secreto: cliente guarda, envía en cada request (Authorization: Bearer ...).
   Estructura: header.payload.signature (¡el payload NO es secreto! es legible base64: mete poco)
   Pros: stateless (escala fácil); Contras: mala revocación (hasta expirar), renewal complejo.
3. OAUTH2 (login con Google/GitHub)
   No implementes tu contraseña si evitas: "Sign in with Google" delega correctamente.
   Flujo: app → alcance autorizado → código → token → perfil del usuario. Úsalo con librerías probadas (NUNCA OAuth casero).

REGLAS SAGRADAS
• Expira JWTs cortos (15min) + refresh tokens seguros
• Nunca en localStorage para JWTs sensibles (XSS te lo roba): cookie HttpOnly mejor
• Rate limiting en /login (5 intentos/min): corta fuerza bruta
```

---

## 📝 Quiz de la lección

### 1. ¿Qué diferencia sesión-clásica de JWT?
- A) Ninguna
- B) Sesión clásica guarda estado en el servidor con ID en cookie; JWT firma y viaja el estado EN EL TOKEN (stateless)
- C) JWT es más seguro
- D) Sesión es para APIs
### 2. ¿Por qué JWT en localStorage es riesgoso?
- A) Es lento
- B) Cualquier XSS puede JavaScript-leerlo y robar identidad; cookie HttpOnly no es legible por JS
- C) No existe
- D) Es ilegal

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Sesión clásica guarda estado en el servidor con ID en cookie; JWT firma y viaja el estado EN EL TOKEN (stateless) — Trade: estado revocable/central vs escalabilidad sin estado ni revocación simple.
**2.** ✅ Cualquier XSS puede JavaScript-leerlo y robar identidad; cookie HttpOnly no es legible por JS — El trade de seguridad: lo que JavaScript toca, un XSS también toca.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
