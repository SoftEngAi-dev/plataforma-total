# ⚠️ Errores comunes — 5. .gitignore, tags y limpieza: buen ciudadano del repo

> Git y GitHub — Tu Historia Nunca Se Pierde · Lección 5 · Aprender de los errores (propios y ajenos)

- ❌ «Es pequeño» → Frente a «¿Por qué .env va al .gitignore SIEMPRE?» lo fácil es confundirse. **Verdad**: Contiene secretos (claves, tokens) que jamás deben quedar en la historia pública. Un secreto subido = filtrado para siempre, aunque lo borres después: hay que rotar la credencial.
- ❌ «Porque git no los soporta» → Frente a «¿Por qué .env va al .gitignore SIEMPRE?» lo fácil es confundirse. **Verdad**: Contiene secretos (claves, tokens) que jamás deben quedar en la historia pública. Un secreto subido = filtrado para siempre, aunque lo borres después: hay que rotar la credencial.
- ❌ «Un archivo» → Frente a «¿Qué es un tag v1.0 en git?» lo fácil es confundirse. **Verdad**: Una marca permanente sobre un commit: la forma de publicar releases/versiones. Los tags señalan hitos estables; son referencia para despliegues.
- ❌ «Una rama» → Frente a «¿Qué es un tag v1.0 en git?» lo fácil es confundirse. **Verdad**: Una marca permanente sobre un commit: la forma de publicar releases/versiones. Los tags señalan hitos estables; son referencia para despliegues.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
