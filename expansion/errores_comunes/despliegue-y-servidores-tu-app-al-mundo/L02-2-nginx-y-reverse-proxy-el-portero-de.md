# ⚠️ Errores comunes — 2. Nginx y reverse proxy: el portero de tu servidor

> Despliegue y Servidores — Tu App al Mundo · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Borra peticiones» → Frente a «¿Qué hace proxy_pass http://localhost:8000?» lo fácil es confundirse. **Verdad**: Nginx recibe en el 80 público y reenvía internamente a tu app en :8000. Reverse proxy: un solo punto público, muchas apps atrás.
- ❌ «Sube archivos» → Frente a «¿Qué hace proxy_pass http://localhost:8000?» lo fácil es confundirse. **Verdad**: Nginx recibe en el 80 público y reenvía internamente a tu app en :8000. Reverse proxy: un solo punto público, muchas apps atrás.
- ❌ «Es más rápido» → Frente a «¿Por qué es estándar que la app corra en 127.0.0.1:8000 y no exponga su puerto?» lo fácil es confundirse. **Verdad**: Control y seguridad: solo Nginx habla con el mundo; aplica HTTPS, límites y cabeceras en un solo sitio. El perímetro en un punto único de control es higiene de seguridad básica.
- ❌ «Porque sí» → Frente a «¿Por qué es estándar que la app corra en 127.0.0.1:8000 y no exponga su puerto?» lo fácil es confundirse. **Verdad**: Control y seguridad: solo Nginx habla con el mundo; aplica HTTPS, límites y cabeceras en un solo sitio. El perímetro en un punto único de control es higiene de seguridad básica.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
