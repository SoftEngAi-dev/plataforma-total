# ⚠️ Errores comunes — 6. Proyecto: API REST real con Express

> Node.js — JavaScript en el Servidor · Lección 6 · Aprender de los errores (propios y ajenos)

- ❌ «200 y 400» → Frente a «¿Qué códigos HTTP usan POST-crear y 'recurso no encontrado' respectivamente?» lo fácil es confundirse. **Verdad**: 201 y 404. 201 = creado; 404 = not found. La semántica HTTP es el idioma de las APIs.
- ❌ «204 y 500» → Frente a «¿Qué códigos HTTP usan POST-crear y 'recurso no encontrado' respectivamente?» lo fácil es confundirse. **Verdad**: 201 y 404. 201 = creado; 404 = not found. La semántica HTTP es el idioma de las APIs.
- ❌ «Solo desde el navegador» → Frente a «¿Cómo probar un POST sin frontend?» lo fácil es confundirse. **Verdad**: curl / Postman / thunder client: cliente HTTP para probar endpoints. curl/demand-tester cliente es tu amigo backend: probar sin UI es el standard.
- ❌ «Con console.log» → Frente a «¿Cómo probar un POST sin frontend?» lo fácil es confundirse. **Verdad**: curl / Postman / thunder client: cliente HTTP para probar endpoints. curl/demand-tester cliente es tu amigo backend: probar sin UI es el standard.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
