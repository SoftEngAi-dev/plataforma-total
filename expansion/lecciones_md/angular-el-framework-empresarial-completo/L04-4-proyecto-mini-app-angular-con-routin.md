# 4. Proyecto: mini-app Angular con routing

> 📚 Curso: **Angular — El Framework Empresarial Completo** · Lección 4 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```typescript
CONSTRUYE: APP DE TAREAS ANGULAR COMPLETA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ng new tareasapp --standalone --routing && cd tareasapp
2. MODELO + SERVICIO: interface Tarea { id: number; titulo: string; hecha: boolean }
   TareasService (root) con signal privado + métodos: todas(), agregar(t), alternar(id), borrar(id)
3. COMPONENTE LISTA (ng g c lista):
   <ul>@for (t of servicio.tareas(); track t.id) {
     <li (click)="servicio.alternar(t.id)" [class.hecha]="t.hecha">{{ t.titulo }}</li>
   }</ul>
4. COMPONENTE FORM: template-driven con [(ngModel)] o mejor ReactiveForms:
   formControl + (ngSubmit)="agregar()" → servicio.agregar(...) → reset campo
5. ROUTING (app.routes.ts):
   { path: "", component: ListaComponent }, { path: "detalle/:id", component: DetalleComponent }
   Lee el param: route = inject(ActivatedRoute); route.snapshot.params["id"]
6. ng serve → app completa. ng build → carpeta dist/ (estático desplegable en Netlify/Pages)

CHECKLIST ARQUITECTURA SAÑA
• Estado solo en el servicio (signal) · componentes tontos que lo leen · rutas por pantalla
• Test gratis: ng test corre Jasmine/Karma ya configurados
```

---

## 📝 Quiz de la lección

### 1. ¿Dónde debe vivir el estado compartido en Angular?
- A) En cada componente
- B) En un servicio inyectable root: componentes lo inyectan y leen sus signals
- C) En el template
- D) En localStorage
### 2. ¿Cuál es el equivalente moderno a *ngFor en Angular 17+?
- A) ng-repeat
- B) Bloque de control nativo: @for (item of lista(); track item.id) { ... }
- C) v-for
- D) map

---

## 🔑 Respuestas y explicaciones

**1.** ✅ En un servicio inyectable root: componentes lo inyectan y leen sus signals — Single source of truth en servicio = la pantalla siempre consistente.
**2.** ✅ Bloque de control nativo: @for (item of lista(); track item.id) { ... } — @for/@if en el template: sin imports extra, tracking explícito y más performance.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
