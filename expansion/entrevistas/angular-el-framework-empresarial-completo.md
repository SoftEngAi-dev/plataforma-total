# 🎤 Banco de entrevista — Angular — El Framework Empresarial Completo

> 8 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué distingue a Angular de React principalmente?**
   - Angular es framework COMPLETO con router/http/form/DI incluidos y TypeScript obligatorio; React es librería de vista + ecosistema a elección  _(Batteries-included vs composición libre: dos filosofías válidas según equipo y proyecto.)_

2. **¿Qué hacen {{ }} y (click) en un template Angular?**
   - {{ }} interpola valores al HTML; (evento)="fn()" enlaza eventos a métodos del componente  _(La sintaxis template de Angular: imprimir con {{}} y escuchar con () encadenado a la clase TS.)_

3. **¿Qué es @Injectable({ providedIn: 'root' })?**
   - Registra el servicio como singleton inyectable en toda la app (una sola instancia compartida)  _(El servicio vive una vez para toda la app: estado/lógica compartida y centralizada.)_

4. **¿En qué se diferencia un Observable de una Promesa?**
   - Emite N valores en el tiempo, es cancelable y componible con operadores; la promesa resuelve UNA vez  _(RxJS = promesas con esteroides: la columna vertebral de datos en Angular.)_

5. **¿Qué problema resuelven los signals respecto a Zone.js?**
   - Detección de cambios quirúrgica: solo se actualiza lo que usa el signal, sin escanear toda la app  _(Rendimiento por reacción fina: ganancia real en apps grandes y código más claro.)_

6. **Un computed() es...**
   - Un valor DERIVADO de signals que se recalcula automáticamente cuando cambian sus dependencias  _(Estado derivado sin lógica manual: defines la relación, Angular mantiene el valor fresco.)_

7. **¿Dónde debe vivir el estado compartido en Angular?**
   - En un servicio inyectable root: componentes lo inyectan y leen sus signals  _(Single source of truth en servicio = la pantalla siempre consistente.)_

8. **¿Cuál es el equivalente moderno a *ngFor en Angular 17+?**
   - Bloque de control nativo: @for (item of lista(); track item.id) { ... }  _(@for/@if en el template: sin imports extra, tracking explícito y más performance.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Angular y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Angular con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
