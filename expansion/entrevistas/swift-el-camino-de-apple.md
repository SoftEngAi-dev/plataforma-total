# 🎤 Banco de entrevista — Swift — El Camino de Apple

> 10 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿Qué distingue let de var en Swift?**
   - let = constante inmutable; var = reasignable — igual que val/var de Kotlin  _(Swift te empuja a let por defecto: mutación solo cuando la justificas.)_

2. **¿Cómo interpola strings Swift?**
   - \(x) dentro del string  _("Hola \(nombre)" — la interpolación nativa de Swift.)_

3. **¿Qué hace guard let x = y else { return }?**
   - Si y es nil, sale de la función ya; si no, x queda disponible desempaquetada para el resto  _(Guard clause: los casos raros se despachan arriba y el código queda plano y claro.)_

4. **¿Por qué se considera peligroso el force unwrap (!) ?**
   - Si el valor es nil, la app CRASHEA en runtime: evitas el mecanismo que te protege  _(El '!' es jurarle al compilador 'está ahí': cuando mientes, paga la app.)_

5. **¿Qué diferencia struct de class en Swift?**
   - struct = tipo VALOR (se copia); class = tipo REFERENCIA (se comparte) con herencia  _(Structs por defecto = menos bugs de aliasing; class solo para identidad compartida.)_

6. **¿Qué permite una extension?**
   - Agregar funcionalidad a tipos existentes sin subclases: incluso a Int, String nativos  _(Las extensiones hacen Swift extensible al infinito y súper idiomático.)_

7. **¿Qué hace @State en SwiftUI?**
   - Marca estado local que al cambiar provoca re-render automático del view que lo usa  _(@State = useState de React: mutás y la UI se actualiza sola.)_

8. **¿Qué es '.padding()' al final del VStack?**
   - Un modifier: transforma la vista y devuelve una nueva (estilo encadenado)  _(Los modifiers se apilan de afuera hacia dentro: declarativos y componibles.)_

9. **¿Qué significa text: $nueva en un TextField?**
   - Binding bidireccional: el campo edita el estado y el estado actualiza el campo  _($variable crea un Binding: ida y vuelta automática entre UI y estado.)_

10. **¿Para qué sirve Identifiable en el modelo de una lista?**
   - Cada item tiene id único para que SwiftUI rastree qué cambió en la lista (como key en React)  _(List/ForEach necesitan identidad estable: id = la key del mundo Apple.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve Swift y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta Swift con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
