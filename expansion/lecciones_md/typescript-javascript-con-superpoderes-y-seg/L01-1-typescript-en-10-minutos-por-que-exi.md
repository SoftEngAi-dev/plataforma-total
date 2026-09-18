# 1. TypeScript en 10 minutos: por qué existe

> 📚 Curso: **TypeScript — JavaScript con Superpoderes y Seguridad** · Lección 1 de 7
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
TS: JS + CHEQUEO DE TIPOS ANTES DE EJECUTAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TypeScript es JavaScript con anotaciones que el compilador verifica ANTES de que corras nada. Detecta 40% de bugs típicos sin ejecutar.

  let edad: number = 36;
  edad = "treinta y seis";     // ❌ Error EN EDICIÓN, no en producción

LA MAGIA: todo JS válido es TS válido. Acoges gradualmente.

HERRAMIENTAS
  npm install -g typescript   → tsc archivo.ts → archivo.js
  tsc --init                   → tsconfig.json (configuración del proyecto)

EL TS NUNCA CORRE; el tsc lo CONVIERTE a JS limpio y eso es lo que se ejecuta.
Por eso los builds: TS → compilar → JS → navegador/Node.

ADOPCIÓN: hoy es la norma industrial. React/Angular/Node serio = TypeScript.
Empezar un proyecto nuevo 2026 sin TS es autoinfringirse sufrimiento a mediano plazo.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es TypeScript exactamente?
- A) Un lenguaje distinto a JS
- B) JavaScript + chequeo estático de tipos que se compila a JS puro
- C) Una librería de JS
- D) Un navegador
### 2. ¿Cuándo detecta TypeScript los errores de tipo?
- A) En producción
- B) Al editar/compilar, antes de ejecutar
- C) Nunca
- D) Solo con tests

---

## 🔑 Respuestas y explicaciones

**1.** ✅ JavaScript + chequeo estático de tipos que se compila a JS puro — Superconjunto tipado: corre como JS tras compilar — el navegador jamás ve tipos.
**2.** ✅ Al editar/compilar, antes de ejecutar — Shift-left: el error aparece cuando lo escribes, no cuando el usuario lo encuentra.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
