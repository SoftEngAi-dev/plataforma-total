# 🎤 Banco de entrevista — Despliegue y Servidores — Tu App al Mundo

> 12 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Cuál es la forma MÁS rápida de publicar una web estática hoy?**
   - GitHub Pages / Netlify: arrastrar la carpeta o conectar el repo, gratis con HTTPS  _(El hoy: no necesitas ni servidor: tu carpeta ya es una web mundial.)_

2. **¿Qué diferencia un VPS de un PaaS?**
   - VPS = tú administras todo (más control y aprendizaje); PaaS = ellos administran, tú solo das el código (menos fricción)  _(Elige VPS para APRENDER sistemas; PaaS para enfocarte en producto.)_

3. **¿Qué hace proxy_pass http://localhost:8000?**
   - Nginx recibe en el 80 público y reenvía internamente a tu app en :8000  _(Reverse proxy: un solo punto público, muchas apps atrás.)_

4. **¿Por qué es estándar que la app corra en 127.0.0.1:8000 y no exponga su puerto?**
   - Control y seguridad: solo Nginx habla con el mundo; aplica HTTPS, límites y cabeceras en un solo sitio  _(El perímetro en un punto único de control es higiene de seguridad básica.)_

5. **¿Qué hace Restart=always en systemd?**
   - Si el proceso muere, systemd lo vuelve a levantar automáticamente  _(Con enable (boot) + Restart, tu app sobrevive cuelgues Y reboots sin tocarte el dedo.)_

6. **¿Por qué un proceso 'detached' no basta para producción?**
   - Un pipeline nohup se pierde en reboots y caídas no planificadas; systemd/pm2 vigilan y resucitan  _(La supervisor de procesos es la diferencia entre hobby y servicio confiable.)_

7. **¿Por qué la base de datos NUNCA se expone directamente a internet?**
   - Ataques automáticos la encontrarían en horas; debe escuchar solo localhost/red interna  _(Postgres/MySQL abiertos al mundo topan scanners a los minutos: firewall + bind local o red privada.)_

8. **¿Qué es un backup 'probado'?**
   - Que REALMENTE restauraste alguna vez y verificaste que funciona  _(Sin undrill de restauración periodic, el backup puede estar corrupto sin que lo sepas.)_

9. **¿Qué se sube al hosting estático cuando usas React con Vite?**
   - La carpeta dist/ generada por npm run build (HTMl/CSS/JS puro)  _(El navegador no entiende JSX/TS: el build los compila a estático; eso es lo que se publica.)_

10. **¿Qué añade Netlify sobre un hosting de archivos normal?**
   - Deploy por git push automático + vistas previas por PR + formularios y HTTPS incluidos  _(Joncy: conectas el repo una vez; cada push redeploya — de hecho tu ya tubiste CD.)_

11. **¿Qué verifica que realmente desplegaste bien?**
   - URL pública + HTTPS (candado) + datos persistiendo + se mantiene tras reinicios  _(Accesibilidad real desde afuera, seguridad básica y persistencia: la trifecta del deploy.)_

12. **¿Por qué documentar el despliegue en el README del proyecto?**
   - URL viva en tu portafolio es la prueba '#1 para recruiters: cualquiera entra y ve tu trabajo andando  _(El link que demuestra es infinitamente más persuasivo que la descripción.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Despliegue y Servidores y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Despliegue y Servidores con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
