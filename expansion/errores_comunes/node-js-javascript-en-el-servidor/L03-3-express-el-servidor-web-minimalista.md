# ⚠️ Errores comunes — 3. Express: el servidor web minimalista

> Node.js — JavaScript en el Servidor · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Una base de datos» → Frente a «¿Qué es un middleware en Express?» lo fácil es confundirse. **Verdad**: Función que se ejecuta entre la petición y la ruta (JSON, auth, logs...). app.use(express.json()) transforma req.body en datos listos — ejemplo clásico.
- ❌ «Un tipo de error» → Frente a «¿Qué es un middleware en Express?» lo fácil es confundirse. **Verdad**: Función que se ejecuta entre la petición y la ruta (JSON, auth, logs...). app.use(express.json()) transforma req.body en datos listos — ejemplo clásico.
- ❌ «200» → Frente a «¿Qué código HTTP corresponde a 'recurso creado'?» lo fácil es confundirse. **Verdad**: 201. 201 Created: convención para POST exitoso de recursos nuevos.
- ❌ «400» → Frente a «¿Qué código HTTP corresponde a 'recurso creado'?» lo fácil es confundirse. **Verdad**: 201. 201 Created: convención para POST exitoso de recursos nuevos.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
