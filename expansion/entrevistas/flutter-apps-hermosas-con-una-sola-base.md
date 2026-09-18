# 🎤 Banco de entrevista — Flutter — Apps Hermosas con Una Sola Base

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué hace Flutter único entre cross-platform?**
   - Pinta cada píxel a mano (no usa widgets nativos): UI 100% idéntica y controlada en todas las plataformas  _(Render propio = diseño exacto en Android/iOS/web sin sorpresas de cada SO.)_

2. **¿Para qué sirve flutter doctor?**
   - Verificar tu entorno: qué falta/configurar para que Flutter funcione (emuladores, SDKs...)  _(El diagnóstico automático: si doctor dice OK, todo funciona.)_

3. **¿Qué es un StatelessWidget?**
   - Un widget sin estado propio: se dibuja igual salvo que su PADRE le pase datos nuevos  _(La mayoría de la UI: describe, no cambia. Lo con estado es StatefulWidget.)_

4. **¿Qué hace Column(children: [...])?**
   - Apila widgets verticalmente (Row es horizontal)  _(Layouts de una dimensión; con Expanded/flex dentro controlas el reparto.)_

5. **¿Por qué dentro de setState(() { cuenta++; })?**
   - setState marca el widget como sucio para que Flutter lo redibuje con el valor nuevo  _(Mutación sin setState = estado cambiado pero UI vieja: el bug de todo novato.)_

6. **¿Dónde inicias un fetch o timer en un StatefulWidget?**
   - En initState (corre una vez al crearse); y liberas sus recursos en dispose  _(build se ejecuta muchas veces: inicialización va en initState, limpieza en dispose.)_

7. **¿Qué paquete oficial se usa para HTTP en Flutter?**
   - http (pub.dev): http.get(Uri.parse(url)) devuelve Future<Response>  _(dart pub add http y Futures con async/await: el estándar de red en Dart.)_

8. **¿Qué renderiza ListView.builder con itemCount?**
   - Las filas BAJO DEMANDA mientras scrolleas (ideal para listas largas)  _(Lazy rendering nativo: miles de posts sin matar el rendimiento.)_

9. **¿Cómo se navega entre pantallas en Flutter nativo?**
   - Navigator.push con MaterialPageRoute; volver con pop (pila de rutas)  _(El Navigator maneja una pila: push apila pantalla, pop regresa con o sin valor.)_

10. **¿Qué comando compila la app para web?**
   - flutter build web → estáticos en build/web desplegables en Netlify/Pages  _(El mismo código Dart/Flutter corre como web estática: cross-platform real cumplida.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Flutter y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Flutter con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
