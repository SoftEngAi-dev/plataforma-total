# 1. Angular + TypeScript: el opinioniado ganador empresa

> 📚 Curso: **Angular — El Framework Empresarial Completo** · Lección 1 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```typescript
ANGULAR: FRAMEWORK COMPLETO, DECISIONES YA TOMADAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mientras React es "una librería + tú eliges", Angular trae TODO incluido: router, HTTP, formularios, DI, testing. TypeScript OBLIGATORIO. Por eso las empresas grandes lo adoran.

  npm install -g @angular/cli
  ng new miblog --standalone && cd miblog && ng serve   → localhost:4200

TU PRIMER COMPONENTE (component.ts + template inline o aparte)
  import { Component } from "@angular/core";
  @Component({
      selector: "app-saludo",
      standalone: true,
      template: `<h1>Hola, {{ nombre }}!</h1>
                 <button (click)="saludar()">Saludar</button>`,
  })
  export class SaludoComponent {
      nombre = "Ada";
      saludar() { alert("¡Hola desde Angular!"); }
  }

MEMORIA RÁPIDA
• {{ expr }} → interpolación (imprimir en template)
• (click)="fn()" → evento · [prop]="valor" → pasar dato a hijo · [(ngModel)] → doble vía
• *ngIf="cond" · *ngFor="let item of lista" (o el nuevo @if/@for moderno sintaxis v17+)

CLI TODO-PODEROSO: ng generate component usuarios → ng g c usuarios (crea los 3-4 archivos solitos).
```

---

## 📝 Quiz de la lección

### 1. ¿Qué distingue a Angular de React principalmente?
- A) Color
- B) Angular es framework COMPLETO con router/http/form/DI incluidos y TypeScript obligatorio; React es librería de vista + ecosistema a elección
- C) Es más lento
- D) No hay diferencia
### 2. ¿Qué hacen {{ }} y (click) en un template Angular?
- A) JS puro
- B) {{ }} interpola valores al HTML; (evento)="fn()" enlaza eventos a métodos del componente
- C) CSS
- D) Nada

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Angular es framework COMPLETO con router/http/form/DI incluidos y TypeScript obligatorio; React es librería de vista + ecosistema a elección — Batteries-included vs composición libre: dos filosofías válidas según equipo y proyecto.
**2.** ✅ {{ }} interpola valores al HTML; (evento)="fn()" enlaza eventos a métodos del componente — La sintaxis template de Angular: imprimir con {{}} y escuchar con () encadenado a la clase TS.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
