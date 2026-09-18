# ⚠️ Errores comunes — 2. Servicios e inyección de dependencias: la joya oculta

> Angular — El Framework Empresarial Completo · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Decoración vacía» → Frente a «¿Qué es @Injectable({ providedIn: 'root' })?» lo fácil es confundirse. **Verdad**: Registra el servicio como singleton inyectable en toda la app (una sola instancia compartida). El servicio vive una vez para toda la app: estado/lógica compartida y centralizada.
- ❌ «Una ruta» → Frente a «¿Qué es @Injectable({ providedIn: 'root' })?» lo fácil es confundirse. **Verdad**: Registra el servicio como singleton inyectable en toda la app (una sola instancia compartida). El servicio vive una vez para toda la app: estado/lógica compartida y centralizada.
- ❌ «Nada» → Frente a «¿En qué se diferencia un Observable de una Promesa?» lo fácil es confundirse. **Verdad**: Emite N valores en el tiempo, es cancelable y componible con operadores; la promesa resuelve UNA vez. RxJS = promesas con esteroides: la columna vertebral de datos en Angular.
- ❌ «Es solo Angular» → Frente a «¿En qué se diferencia un Observable de una Promesa?» lo fácil es confundirse. **Verdad**: Emite N valores en el tiempo, es cancelable y componible con operadores; la promesa resuelve UNA vez. RxJS = promesas con esteroides: la columna vertebral de datos en Angular.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
