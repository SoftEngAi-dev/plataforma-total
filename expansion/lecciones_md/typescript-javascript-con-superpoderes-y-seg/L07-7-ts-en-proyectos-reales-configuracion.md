# 7. TS en proyectos reales: configuración y flujo

> 📚 Curso: **TypeScript — JavaScript con Superpoderes y Seguridad** · Lección 7 de 7
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```javascript
DE LOS TIPOS A LA PRODUCCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP
  npm init -y
  npm install --save-dev typescript
  npx tsc --init      → tsconfig.json

TSCONFIG (los 5 que importan)
  "strict": true           ← SIEMPRE; activa todas las protecciones
  "target": "ES2022"       ← JS de salida moderno
  "outDir": "./dist"       ← compilado separado de src
  "rootDir": "./src"
  "noEmitOnError": true    ← si hay errores, no publica

FLUJO
  src/*.ts → npx tsc (watch: npx tsc --watch) → dist/*.js → node dist/app.js
  (y en frontend: Vite/esbuild lo hacen transparente)

CON LIBRERÍAS JS: instala sus tipos
  npm i express && npm i -D @types/express   ← la comunidad tipa casi todo

DISCIPLINA REAL
1. strict desde el día 1 (aflojar después es dolor)
2. Errores de tipo se ARREGLAN; los `as any` se cuentan como deuda técnica
3. Tipos en los límites (APIs, archivos, props) y deja inferir en el interior
```

---

## 📝 Quiz de la lección

### 1. ¿Qué activa "strict": true en tsconfig?
- A) Solo chequeo básico
- B) Una familia de protecciones: null checks, noImplicitAny, etc. — el modo serio de TS
- C) Rápida ejecución
- D) Nada
### 2. ¿Cómo usar tipos con una librería JS como express?
- A) No se puede
- B) npm i -D @types/express (definiciones de tipos de la comunidad)
- C) Reescribirla en TS
- D) Con un plugin

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Una familia de protecciones: null checks, noImplicitAny, etc. — el modo serio de TS — Strict atrapa el grueso de los bugs de tipo. Proyecto profesional sin strict = medio TS.
**2.** ✅ npm i -D @types/express (definiciones de tipos de la comunidad) — @types/* cubre todo el ecosistema popular: tu editor la entiende como si fuera TS nativa.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
