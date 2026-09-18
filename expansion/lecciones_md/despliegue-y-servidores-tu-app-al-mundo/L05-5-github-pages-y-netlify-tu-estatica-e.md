# 5. GitHub Pages y Netlify: tu estática en 5 minutos

> 📚 Curso: **Despliegue y Servidores — Tu App al Mundo** · Lección 5 de 6
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```bash
PUBLICA TU PRIMERA WEB HOY MISMO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
A) GITHUB PAGES (desde tu repo)
1. Repo con index.html en la raíz
2. Settings → Pages → Source: "Deploy from a branch" → main / root
3. 1-2 minutos: https://tuusuario.github.io/turepo/
   Dominio propio: pestaña Pages → Custom domain + CNAME en tu registrador.

B) NETLIFY (aún más magia)
   Arrastra tu carpeta al panel de netlify.com → URL instantánea con HTTPS.
   O conecta GitHub: cada git push republica solo (¡CI/CD de regalo!).
   Formularios gratis sin backend; build command si usas Vite/React: npm run build, publish: dist.

REACT/VITE EN PÁGINA ESTÁTICA
  npm run build → genera carpeta dist de puro estático → esa sube (no el código fuente).
  En GitHub Pages con pakage.json puedes usar workflow para build automático.

DOMINIO propio entre todas: CNAME para www/dominio secundario; A/ALIAS a la IP para el raíz. Propagación: minutos a horas (paciencia).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué se sube al hosting estático cuando usas React con Vite?
- A) src/
- B) La carpeta dist/ generada por npm run build (HTMl/CSS/JS puro)
- C) node_modules/
- D) package.json
### 2. ¿Qué añade Netlify sobre un hosting de archivos normal?
- A) Java
- B) Deploy por git push automático + vistas previas por PR + formularios y HTTPS incluidos
- C) Base de datos
- D) SSH

---

## 🔑 Respuestas y explicaciones

**1.** ✅ La carpeta dist/ generada por npm run build (HTMl/CSS/JS puro) — El navegador no entiende JSX/TS: el build los compila a estático; eso es lo que se publica.
**2.** ✅ Deploy por git push automático + vistas previas por PR + formularios y HTTPS incluidos — Joncy: conectas el repo una vez; cada push redeploya — de hecho tu ya tubiste CD.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
