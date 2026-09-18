# 5. Proyecto: auditoría de seguridad propia

> 📚 Curso: **Seguridad para Desarrolladores — No Seas la Brecha** · Lección 5 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text
AUDITA TU PROPÍA APP (LO QUE HACE UN BLUE TEAM JUNIOR)
━━━━━━━━━━━━━━━━━━━━━━━━━━━
CHECKLIST OPERATIVA (60 min, sobre una app tuya desplegada)
1. CABECERAS: mete tu URL en securityheaders.com → anota qué falta (CSP, HSTS, X-Frame...)
   → agrégalas en tu servidor y vuelve a pasar: meta >= A
2. INPUTS: intenta escribir <script>alert(1)</script> en cada campo/caja
   → si aparece el alert en TUS ojos: HAY XSS. Arregla con escape/sanitización y vuelve a probar SIN alert.
3. IDOR: logueado como user A, cambia la URL/recurso a otro id
   → ¿ves el contenido? Endpoint roto. Corrige: verifica dueño en el servidor, siempre.
4. CONTRASEÑAS: pon 'aaaaa' como contraseña nueva → si ADMITE, no hay política frr
   (juguete lont) Fuerza bruta: 5 intentos cortos → si no hay rate limit, debilidad anotada.
5. DEPENDENCIAS: pip-audit (o npm audit) → lista de paquetes con vulnerabilidad conocida
   → actualiza lo urgente a versiones seguras y re-corre.

BONUS NIVEL+: OWASP ZAP/Burp Suite Community hacen scanning automático gratis sobre tu app local/expuesta.

ENTREGABLE: un informe markdown "auditoría-mi-app.md" con hallazgos (severidad), evidencia y fix aplicado.
Esto = tu primera línea "seguridad práctica" en portafolio/CV — distingue muchísimo.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué descubre pegar <script>alert(1)</script> en un campo y probar?
- A) Nada
- B) Si ves el alert: tu app ejecuta código de usuario = XSS confirmado
- C) El backend
- D) El SEO
### 2. ¿Por qué testear IDOR es tan crítico para endpoints con IDs?
- A) Aburrido
- B) Es la vulnerabilidad web nº1 real: chequear que solo el DUEÑO accede a su recurso por cada request
- C) Backend only
- D) PCI

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Si ves el alert: tu app ejecuta código de usuario = XSS confirmado — La prueba ácida manual del XSS: si JS injectado corre, tu escape no es suficiente.
**2.** ✅ Es la vulnerabilidad web nº1 real: chequear que solo el DUEÑO accede a su recurso por cada request — La lección: no confíes en la URL escondida: cada query/id verifica ownership server-side.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
