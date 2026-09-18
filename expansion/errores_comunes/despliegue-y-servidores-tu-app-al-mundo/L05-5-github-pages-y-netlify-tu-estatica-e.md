# ⚠️ Errores comunes — 5. GitHub Pages y Netlify: tu estática en 5 minutos

> Despliegue y Servidores — Tu App al Mundo · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «src/» → Frente a «¿Qué se sube al hosting estático cuando usas React con Vite?» lo fácil es confundirse. **Verdad**: La carpeta dist/ generada por npm run build (HTMl/CSS/JS puro). El navegador no entiende JSX/TS: el build los compila a estático; eso es lo que se publica.
- ❌ «node_modules/» → Frente a «¿Qué se sube al hosting estático cuando usas React con Vite?» lo fácil es confundirse. **Verdad**: La carpeta dist/ generada por npm run build (HTMl/CSS/JS puro). El navegador no entiende JSX/TS: el build los compila a estático; eso es lo que se publica.
- ❌ «Java» → Frente a «¿Qué añade Netlify sobre un hosting de archivos normal?» lo fácil es confundirse. **Verdad**: Deploy por git push automático + vistas previas por PR + formularios y HTTPS incluidos. Joncy: conectas el repo una vez; cada push redeploya — de hecho tu ya tubiste CD.
- ❌ «Base de datos» → Frente a «¿Qué añade Netlify sobre un hosting de archivos normal?» lo fácil es confundirse. **Verdad**: Deploy por git push automático + vistas previas por PR + formularios y HTTPS incluidos. Joncy: conectas el repo una vez; cada push redeploya — de hecho tu ya tubiste CD.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
