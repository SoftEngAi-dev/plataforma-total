# 3. Signals: la nueva reactividad fina

> 📚 Curso: **Angular — El Framework Empresarial Completo** · Lección 3 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```typescript
SIGNALS (Angular 16+): ESTADO SIMPLE, SIN ZONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Angular moderno reacciona con signals: contenedores de valor que avisan quién los usa.

  import { signal, computed, effect } from "@angular/core";
  export class ContadorComponent {
      cuenta = signal(0);
      doble = computed(() => this.cuenta() * 2);       // derivado, se recalcula solo

      constructor() {
          effect(() => console.log("cambió:", this.cuenta()));   // efecto al cambiar
      }
      incrementar() { this.cuenta.update(v => v + 1); }  // o .set(10)
  }

EN EL TEMPLATE se leen como función:
  <p>Cuenta: {{ cuenta() }} (doble: {{ doble() }})</p>
  <button (click)="incrementar()">+1</button>

¿POR QUÉ IMPORTA? Antes Angular usaba Zone.js para detectar cambios en TODA la app (pesado).
Signals = detección quirúrgica: solo re-renderiza quien usa ese valor. Más rápido, más predecible, más simple mentalmente. Con v17+ además @if/@for reemplazan *ngIf/*ngFor:

  @if (tareas().length) { <ul>@for (t of tareas(); track t.id) { <li>{{ t.titulo }}</li> }</ul> }
```

---

## 📝 Quiz de la lección

### 1. ¿Qué problema resuelven los signals respecto a Zone.js?
- A) Ninguno
- B) Detección de cambios quirúrgica: solo se actualiza lo que usa el signal, sin escanear toda la app
- C) Sintaxis corta
- D) HTTP
### 2. Un computed() es...
- A) una función async
- B) Un valor DERIVADO de signals que se recalcula automáticamente cuando cambian sus dependencias
- C) Un servicio
- D) CSS

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Detección de cambios quirúrgica: solo se actualiza lo que usa el signal, sin escanear toda la app — Rendimiento por reacción fina: ganancia real en apps grandes y código más claro.
**2.** ✅ Un valor DERIVADO de signals que se recalcula automáticamente cuando cambian sus dependencias — Estado derivado sin lógica manual: defines la relación, Angular mantiene el valor fresco.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
