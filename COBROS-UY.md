# 🇺🇾 COBROS EN URUGUAY — Cómo sacar las ganancias con Santander, Prex y MiDinero
### Guía práctica verificada (Septiembre 2026) — complemento de MONETIZACION.md

---

## 0. 🧭 El mapa en 10 segundos

```
VENTAS (Lemon Squeezy, MoR) ──pago 2 veces/mes──►  💰 TU PLATAFORMA DE COBRO
                                                        │
        ┌───────────────────────┬─────────────────────── ┤
        ▼                       ▼                        ▼
   🏦 SANTANDER UY        💳 PAYPAL → PREX UY      (acumular en LS)
   (wire directo,          (la ruta más fácil       hasta montos
    1% + mín $25)           para empezar HOY)        grandes)
        │                       │
        └───────transferencias locales──────────────┘
                        ▼
               📱 MiDinero = PUNTO FINAL DE GASTO
               (NO recibe del exterior directo;
                sí desde cualquier banco UY y MercadoPago)
```

**Resumen brutalmente honesto:** Lemon Squeezy paga a Uruguay **directo a banco** (estás en la lista oficial de países con payout bancario ✔️) o vía **PayPal**. MiDinero no recibe del exterior: es donde *gastás* la plata, no donde la recibís. Prex es el puente más barato y rápido para arrancar.

---

## 1. 📅 Cómo te paga Lemon Squeezy (reglas verificadas)

| Regla | Dato |
|---|---|
| Frecuencia | **2 veces al mes: días 14 y 28** |
| Retención | **13 días** de hold antes de liberar cada venta |
| Mínimo | **U$S 50** acumulados |
| Moneda | USD |
| Payout a **banco** internacional | **1% por payout** (U$S 0 si fuera EE.UU.) |
| Payout a **PayPal** internacional | **3% por payout, TOPE U$S 30** |
| Impuestos de venta (IVA mundial) | Los gestiona ellos como Merchant of Record — vos no te ocupás |
| Estado de la plataforma | Activa, acepta nuevos merchants (Stripe la compró en 2024; existe "Stripe Managed Payments" en preview como sucesor, sin fecha de migración obligatoria — tu `monetizacion.json` te protege: cambiás enlaces sin tocar la app) |

---

## 2. 🛤️ Las 3 rutas, comparadas con números reales

### RUTA A — LS → PayPal → **Prex UY** ⭐ (recomendada para empezar)
La de menor fricción total a costo $0.

| Tramo | Costo verificado |
|---|---|
| LS paga a tu PayPal | 3% **tope U$S 30** por payout |
| Retirás de PayPal a Prex (vinculada) | **U$S 4 + IVA** por retiro (~U$S 2.000 máx por operación, según reportes) |
| Acreditación | Casi **inmediata** |
| **Costo total real** | Payout de $300 ≈ **$13** · payout de $1.000+ ≈ **$34 fijos** (tapes incluidos) |

**Pasos:** PayPal (cuenta gratis, email) → Prex App → "Retiros" → vincular PayPal → retirar. Éxito: plata gastable con tu Mastercard Prex, transferible a Santander o MiDinero.

### RUTA B — LS → **Santander UY** directo (la formal, ideal para montos grandes)
Lemon Squeezy habilita payout bancario a Uruguay.

| Tramo | Costo verificado |
|---|---|
| LS payout bancario internacional | **1%** del payout |
| Santander cobra por recibir giro internacional (SWIFT MT103) | **1,5‰ — MÍNIMO U$S 25 · máximo U$S 130** |
| **Costo total real** | Payout $300 ≈ **$28** · payout $3.000 ≈ **$55** · payout $10.000 ≈ **$230** |

**Datos para configurar el payout en LS:** tu nombre completo (igual al titular de la cuenta), número de cuenta Santander UY (tu caja de ahorro USD), **SWIFT: BSCHUYMMXXX**, dirección del banco (Zabala 1423, Montevideo o la de tu sucursal).

> 💡 **Regla de oro:** por el mínimo de U$S 25 de Santander, **acumulá antes de cobrar**. LS paga 14 y 28 automáticamente al superar U$S 50… conviene esperar a tener **≥ U$S 1.500** para que el tramo bancario pese <2%. (A comparar: la ruta PayPal→Prex queda en $34 fijos arriba de $1.000 — para volúmenes medianos ¡la Ruta A gana!)

### RUTA C — LS → Payoneer → Prex (respaldo)
Prex acepta retiros desde **Payoneer al 2%** (verificado en el centro de ayuda de Prex). Útil si PayPal algún día falla.

---

## 3. 📱 MiDinero — cómo entrar en TU ecosistema

MiDinero **no recibe transferencias internacionales directas** (verificado en su FAQ oficial). Pero es perfecto como **destino final de gasto** porque:

- ✅ Recibe transferencias desde **cualquier banco uruguayo** (Santander incluido) y desde **MercadoPago** → solo das tu **número de cuenta MiDinero** (visible en la App arriba del saldo) y el remitente elige institución **“Midinero”**.
- ✅ Puede recibir/recargar **en dólares** y quedan acreditados en USD.
- ✅ Retiro en efectivo: locales **Redpagos (TuCajero)** o cajeros **Banred** — límite UYU 30.000 o U$S 1.000 cada 24 h.
- **Circuito recomendado:** Prex/Santander → transferencia local → MiDinero → gastar/retirar.

---

## 4. 🏦 Tu Santander — configuración exacta para cobrar

1. Asegurate de tener **caja de ahorro en USD** (Santander la ofrece sin costo extra en la mayoría de los paquetes; pedila por Súpernet/WhatsApp oficial si no la ves).
2. En Lemon Squeezy: `Settings → Payouts → Add bank account` → completá: beneficiario (tu nombre), país Uruguay, moneda USD, nº de cuenta, **SWIFT BSCHUYMMXXX**.
3. Primer payout: Santander puede pedirte **origen de fondos** (normal por cumplimiento) → mostrá el panel de ventas de LS + extractos. Guardá todo: Lemon Squeezy te da facturas de cada order en PDF.
4. Comisiones al recibir: 1,5‰ (mín $25 máx $130) + posible comisión de canje si acreditás USD (~0,175% + IVA reportado por usuarios). Verificá tu contrato vigente en súpernet.

---

## 5. ⚖️ Impuestos (obligatorio, 1 lectura)

- Venta de software/suscripciones al exterior = **exportación de servicios**: exenta de IVA e IRAE si la usás bien (según régimen).
- Opciones reales: **Unipersonal/Monotributo** (facturás y pagás cuota fija baja al empezar) o tributar como persona física (IRPF) según montos.
- **Regla práctica:** hasta tus primeras ~U$S 500-1.000/mes no tomes decisiones; cuando las superes, **1 hora con un contador** (~U$S 50) te deja tranquilo para siempre. Lemon Squeezy te da todos los reportes exportables.

---

## 6. ✅ Checklist final (orden recomendado)

1. ☐ Crear cuenta PayPal (gratis) con el mismo email de Lemon Squeezy.
2. ☐ Verificar **Prex** (video-llamada/DNI) y vincular PayPal desde "Retiros".
3. ☐ Pedir/verificar caja de ahorro USD en Santander + anotar SWIFT **BSCHUYMMXXX**.
4. ☐ En LS: payout principal = **banco Santander** (o PayPal mientras acumulás), secundario = el otro (LS permite cambiar).
5. ☐ Número de cuenta MiDinero anotado para mover plata y gastar.
6. ☐ Cuando llegue el primer payout a Santander: guardar PDF de orders de LS (origen de fondos).
7. ☐ A los ~U$S 500/mes: hora de contador.

> 🎯 **Decisión rápida:** si querés cobrar ya sin pensar: **payout = PayPal** y retirás a Prex por $4. Si ya facturás $2.000+/mes: **payout = Santander** directo y dejás PayPal como backup.
