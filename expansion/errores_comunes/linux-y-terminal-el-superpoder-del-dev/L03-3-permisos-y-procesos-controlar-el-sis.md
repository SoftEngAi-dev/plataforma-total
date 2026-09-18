# ⚠️ Errores comunes — 3. Permisos y procesos: controlar el sistema

> Linux y Terminal — El Superpoder del Dev · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Leerlo» → Frente a «chmod +x script.sh permite...» lo fácil es confundirse. **Verdad**: Ejecutarlo directamente (bit de ejecución). Sin +x lo corres como ./script.sh solo con bash script.sh; con +x directo.
- ❌ «Comprimirlo» → Frente a «chmod +x script.sh permite...» lo fácil es confundirse. **Verdad**: Ejecutarlo directamente (bit de ejecución). Sin +x lo corres como ./script.sh solo con bash script.sh; con +x directo.
- ❌ «Siempre primero» → Frente a «¿Cuándo usar kill -9?» lo fácil es confundirse. **Verdad**: Solo cuando kill normal (SIGTERM) falla: -9 no deja limpiar al proceso. SIGTERM pide cortésmente cerrarse (guardar estado); SIGKILL lo aniquila sin aviso.
- ❌ «Para todo» → Frente a «¿Cuándo usar kill -9?» lo fácil es confundirse. **Verdad**: Solo cuando kill normal (SIGTERM) falla: -9 no deja limpiar al proceso. SIGTERM pide cortésmente cerrarse (guardar estado); SIGKILL lo aniquila sin aviso.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
