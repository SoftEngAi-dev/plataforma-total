# ⚠️ Errores comunes — 3. Mantener tu app viva: systemd, pm2 y reinicios

> Despliegue y Servidores — Tu App al Mundo · Lección 3 · Aprender de los errores (propios y ajenos)

- ❌ «Arranca lento» → Frente a «¿Qué hace Restart=always en systemd?» lo fácil es confundirse. **Verdad**: Si el proceso muere, systemd lo vuelve a levantar automáticamente. Con enable (boot) + Restart, tu app sobrevive cuelgues Y reboots sin tocarte el dedo.
- ❌ «Recarga config» → Frente a «¿Qué hace Restart=always en systemd?» lo fácil es confundirse. **Verdad**: Si el proceso muere, systemd lo vuelve a levantar automáticamente. Con enable (boot) + Restart, tu app sobrevive cuelgues Y reboots sin tocarte el dedo.
- ❌ «Sí basta» → Frente a «¿Por qué un proceso 'detached' no basta para producción?» lo fácil es confundirse. **Verdad**: Un pipeline nohup se pierde en reboots y caídas no planificadas; systemd/pm2 vigilan y resucitan. La supervisor de procesos es la diferencia entre hobby y servicio confiable.
- ❌ «Es igual» → Frente a «¿Por qué un proceso 'detached' no basta para producción?» lo fácil es confundirse. **Verdad**: Un pipeline nohup se pierde en reboots y caídas no planificadas; systemd/pm2 vigilan y resucitan. La supervisor de procesos es la diferencia entre hobby y servicio confiable.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
