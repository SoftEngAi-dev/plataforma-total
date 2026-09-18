# ⚠️ Errores comunes — 1. El sistema de archivos y navegación

> Linux y Terminal — El Superpoder del Dev · Lección 1 · Aprender de los errores (propios y ajenos)

- ❌ «Borra a/b/c» → Frente a «¿Qué hace mkdir -p a/b/c?» lo fácil es confundirse. **Verdad**: Crea la ruta completa incluidos padres intermedios sin error. Sin -p falla si 'a' no existe; con -p crea todo el camino.
- ❌ «Cambia permisos» → Frente a «¿Qué hace mkdir -p a/b/c?» lo fácil es confundirse. **Verdad**: Crea la ruta completa incluidos padres intermedios sin error. Sin -p falla si 'a' no existe; con -p crea todo el camino.
- ❌ «existe» → Frente a «rm -r lo que hace peligroso es que...» lo fácil es confundirse. **Verdad**: Linux NO tiene papelera: lo borrado por rm se fue (por eso rm -i o trash tools). Cuidado con rm: la ruta / o comodines mal puestos borran todo sin preguntar.
- ❌ «es root» → Frente a «rm -r lo que hace peligroso es que...» lo fácil es confundirse. **Verdad**: Linux NO tiene papelera: lo borrado por rm se fue (por eso rm -i o trash tools). Cuidado con rm: la ruta / o comodines mal puestos borran todo sin preguntar.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
