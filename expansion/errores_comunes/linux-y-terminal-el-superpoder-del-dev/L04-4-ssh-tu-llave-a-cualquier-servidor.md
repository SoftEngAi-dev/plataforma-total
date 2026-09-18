# ⚠️ Errores comunes — 4. SSH: tu llave a cualquier servidor

> Linux y Terminal — El Superpoder del Dev · Lección 4 · Aprender de los errores (propios y ajenos)

- ❌ «Son más cortas» → Frente a «¿Por qué llaves SSH en vez de contraseña?» lo fácil es confundirse. **Verdad**: Criptografía asimétrica: la privada nunca viaja; contraseñas por red son atacables con fuerza bruta. La pública en el server + privada en tu máquina: imposible de robar por sniffing.
- ❌ «Es obligatorio» → Frente a «¿Por qué llaves SSH en vez de contraseña?» lo fácil es confundirse. **Verdad**: Criptografía asimétrica: la privada nunca viaja; contraseñas por red son atacables con fuerza bruta. La pública en el server + privada en tu máquina: imposible de robar por sniffing.
- ❌ «Imprimir» → Frente a «rsync -avz a/ usuario@IP:~/b/ se usa para...» lo fácil es confundirse. **Verdad**: Sincronizar carpetas remotas eficientemente (solo cambios, comprime, reanuda). El caballo de batalla de backups y despliegues artesanales.
- ❌ «Chat remoto» → Frente a «rsync -avz a/ usuario@IP:~/b/ se usa para...» lo fácil es confundirse. **Verdad**: Sincronizar carpetas remotas eficientemente (solo cambios, comprime, reanuda). El caballo de batalla de backups y despliegues artesanales.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
