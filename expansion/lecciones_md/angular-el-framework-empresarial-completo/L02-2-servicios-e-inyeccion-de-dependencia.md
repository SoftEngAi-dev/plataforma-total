# 2. Servicios e inyección de dependencias: la joya oculta

> 📚 Curso: **Angular — El Framework Empresarial Completo** · Lección 2 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```typescript
SERVICIOS + DI: DÓNDE VIVE LA LÓGICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Regla Angular: los componentes pintan; los SERVICIOS trabajan (API, estado, lógica).

  // tareas.service.ts
  import { Injectable, inject } from "@angular/core";
  import { HttpClient } from "@angular/common/http";
  @Injectable({ providedIn: "root" })          // singleton en toda la app
  export class TareasService {
      private http = inject(HttpClient);        // DI moderna (sin constructor)
      private api = "https://jsonplaceholder.typicode.com/todos";
      todas() { return this.http.get<Tarea[]>(this.api); }   // devuelve Observable
  }

EN EL COMPONENTE
  export class ListaComponent {
      servicio = inject(TareasService);
      tareas: Tarea[] = [];
      ngOnInit() {
          this.servicio.todas().subscribe(datos => this.tareas = datos);
      }
  }

OBSERVABLES (RxJS): streams de datos que llegan en el tiempo — te SUSCRIBES para recibir.
Más potentes que promesas: se cancelan, componen (map/filter), llegan N veces (sockets, eventos).

DI = inyección de dependencias: pides lo que necesitas y Angular te lo entrega fabricado y singleton — tests con mocks triviales, arquitectura limpia de fábrica.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué es @Injectable({ providedIn: 'root' })?
- A) Decoración vacía
- B) Registra el servicio como singleton inyectable en toda la app (una sola instancia compartida)
- C) Una ruta
- D) Un test
### 2. ¿En qué se diferencia un Observable de una Promesa?
- A) Nada
- B) Emite N valores en el tiempo, es cancelable y componible con operadores; la promesa resuelve UNA vez
- C) Es solo Angular
- D) Es más lento siempre

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Registra el servicio como singleton inyectable en toda la app (una sola instancia compartida) — El servicio vive una vez para toda la app: estado/lógica compartida y centralizada.
**2.** ✅ Emite N valores en el tiempo, es cancelable y componible con operadores; la promesa resuelve UNA vez — RxJS = promesas con esteroides: la columna vertebral de datos en Angular.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
