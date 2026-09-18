# 🤖 MODO AGENTE — Despliegue autónomo de la tienda ($0 → primera venta)
### Plataforma Total · Playbook para ejecutar SOLO (usuario) o dar a CUALQUIER agente/IA

> **Filosofía:** hay 3 bloques. El **Bloque A** solo lo puede hacer una PERSONA (crear la cuenta, verificar identidad, poner datos bancarios — por seguridad y KYC nadie lo debe hacer por vos). Los **Bloques B y C** los ejecuta un agente automáticamente: pegás 4 enlaces (o la API key) y el agente termina TODO.

---

## 🔐 REGLA DE SEGURIDAD (léela primero)

| Dato | ¿Se puede pegar a un agente? |
|---|---|
| Enlaces de checkout de tus productos | ✅ Sí (son públicos, van en la web) |
| API key de Lemon Squeezy (Settings → API) | ⚠️ Sí, solo al agente de confianza (es revocable) |
| Claves de licencia de PRUEBA que generes | ✅ Sí |
| **Tu contraseña de Lemon Squeezy / banco / cédula** | ❌ **NUNCA — a nadie, ninguna IA lo necesita** |

---

## 🧑 BLOQUE A — Lo que hace EL HUMANO (~20 min, solo UNA vez)

### A1. Crear la tienda (5 min)
1. Entrá a **https://app.lemonsqueezy.com/register** → email + contraseña (guardá la contraseña en un gestor).
2. Verificá el email, nombre de tienda: `plataforma-total`.
3. `Settings → General`: país **Uruguay**, moneda **USD**.
   - Si te piden **"Website / Product URL"** (para validar que tenés un producto real): ✅ ya existe → usá `https://softengai-dev.github.io/plataforma-total/` (landing + precios) o `…/plataforma-total/app/` (la web app gratis). Ver **WEB-Y-MOVIL.md §4**.
4. `Settings → Payouts`: conectá tu cobro (ver **COBROS-UY.md** → banco Santander SWIFT `BSCHUYMMXXX` o PayPal).

### A2. Crear los 4 productos (10 min, copy-paste exacto)
`Store → Products → + New Product` — en cada uno: **✅ activar "Generate license keys"** y tax category **"Software (SaaS)"**:

| # | Nombre del producto | Tipo | Precio |
|---|---|---|---|
| 1 | `Plataforma Total PRO — Mensual` | **Subscription** (cada 1 mes) | U$S 7.99 |
| 2 | `Plataforma Total PRO — Anual` | **Subscription** (cada 1 año) | U$S 79 |
| 3 | `Plataforma Total PRO — De por vida` | **One-time** | U$S 169 |
| 4 | `Descuento estudiantes −40%` (opcional) | **Discount** cupón `ESTUDIANTE40` | −40% |

*(Los 7 packs temáticos a U$S 24 se crean igual que el #3; la app los trata como PRO. Se pueden agregar después — la app los detecta sola.)*

Al guardar cada producto → botón **Share** → copiá el **Checkout link** (formato `https://plataforma-total.lemonsqueezy.com/checkout/buy/XXXX...`).

### A3. Tu licencia GRATIS (owner) (2 min)
`Store → Discounts → New` → 100% OFF, código `OWNER` → cómprate vos mismo el producto **De por vida** con ese código → **te llega tu clave por email** → en la app: 💎 → pegar → Activar.

### A4. API key (opcional, para que el agente lo TODO automatice)
`Settings → API → + Crear API key` (modo **live**) → pegala al agente.

---

## 🤖 BLOQUE B — Lo que ejecuta EL AGENTE AUTOMÁTICAMENTE

**Entrada:** los 4 checkout links (y/o la API key). Al recibirlos, el agente debe, EN ORDEN:

```bash
# 1. Escribir los enlaces reales en monetizacion.json
#    (checkout_mensual / checkout_anual / checkout_lifetime)
# 2. Commit + push a main → la web #precios y la app los leen solas (cache 24h)
git add monetizacion.json && git commit -m "💰 activar checkout real Lemon Squeezy" && git push
# 3. Verificación end-to-end SIN pagar:
#    - web: abrir https://softengai-dev.github.io/plataforma-total/#precios → los botones apuntan a LS
#    - app: instalar limpio → abrir curso PRO → paywall muestra planes → botón abre checkout real
#    - clave OWNER de A3 → activa y desbloquea los 32 cursos (prueba real del paywall)
# 4. Smoke-test de venta (opcional): compra de prueba en modo test de LS con tarjeta 4242
```

✅ **Criterio de DONE:** un usuario nuevo descarga el ZIP, abre un curso PRO, paga, recibe su clave en el email, la pega en la app y queda desbloqueado — SIN que el humano toque nada más.

---

## 📣 BLOQUE C — Lanzamiento (✅ ASSETS YA GENERADOS en `marketing/`)

Todo el material está **listo y commiteado** — tras el Bloque B solo hay que publicar:

1. ✅ **Landing SEO**: `docs/index.html` ya incluye #cursos-seo (47 cursos indexables) + FAQ + JSON-LD.
2. ✅ **Artículo** en `marketing/LANZAMIENTO-DEVTO.md` — publicar en Dev.to/Medium/LinkedIn el día 0.
3. ✅ **Posts comunidades** en `marketing/REDDIT-Y-COMUNIDADES.md` (con regla 9:1 y respuestas tipo).
4. ✅ **3 guiones TikTok/Shorts** en `marketing/TIKTOKS.md` (cadencia 2-3/semana).
5. ✅ **Product Hunt kit** en `marketing/PRODUCT-HUNT.md` (lanzar martes/miércoles 00:01 PT).
6. ✅ **Kit afiliados 30%** en `marketing/KIT-AFILIADOS.md` (activar en LS → invitar 5 creadores).
7. Índice y orden de ejecución: `marketing/README-LANZAMIENTO.md`.
8. Reporte al dueño con: checklist ✅/❌ por punto y próximos experimentos de conversión.

---

## 🧾 PROMPT LISTO PARA PEGAR A CUALQUIER AGENTE

```
Sos mi agente de despliegue. Contexto: repo github.com/SoftEngAi-dev/plataforma-total (rama main).
La app ya tiene paywall (15 cursos gratis, 32 PRO) y lee checkout links de
https://raw.githubusercontent.com/SoftEngAi-dev/plataforma-total/main/monetizacion.json
Mis enlaces de Lemon Squeezy son:
- mensual: PEGAR_AQUI
- anual: PEGAR_AQUI
- lifetime: PEGAR_AQUI
(+) API key live: PEGAR_AQUI (revocable)
Ejecutá el BLOQUE B completo de MODO-AGENTE.md (actualizar JSON, push, verificación
end-to-end incl. activación con mi clave OWNER: PEGAR_AQUI), luego el BLOQUE C puntos 1-5.
Reportame un checklist final ✅/❌. No pidas NUNCA contraseñas ni datos bancarios.
```
