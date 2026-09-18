# 🎤 Banco de entrevista — React Native — Móvil con Tu Stack Web

> 8 preguntas esenciales + guía de respuestas las que ya sabes del curso

## 🔥 Fundamentales (del contenido del curso)

1. **¿En qué difiere React Native de una WebView/web app empaquetada?**
   - RN compila tus componentes a widgets NATIVOS reales (rendimiento verdadero), no embebe una web  _(RN renderiza UIView/View nativas: por eso se siente app de verdad, no página.)_

2. **¿Qué hace Expo en el flujo RN?**
   - Toolchain que elimina el setup nativo: QR al teléfono, hot reload, build en la nube  _(Con Expo arrancas sin Xcode/Android Studio instalado: la puerta de entrada estándar.)_

3. **¿Por qué FlatList y no un map dentro de ScrollView?**
   - FlatList virtualiza: solo dibuja filas visibles; ScrollView+map renderiza TODO (mata listas largas)  _(El rendimiento de listas = virtualización. Regla: lista > ~20 items → FlatList.)_

4. **¿Cómo pasas datos al navegar entre pantallas?**
   - navigation.navigate('Detalle', { id }) y los lees con route.params en la pantalla destino  _(El segundo argumento navega parámetros: detalle recibe el id y trae/renderiza el dato.)_

5. **¿Cómo se envía texto controlado en RN vs web?**
   - onChangeText recibe el string directamente: setTexto(nuevoTexto)  _(Mismo patrón controlado, pero el callback te da el texto límpio.)_

6. **¿Qué es AsyncStorage?**
   - Almacenamiento clave-valor local (equivalente móvil de localStorage), strings+JSON  _(Guarda strings; con JSON.stringify/parse persistes objetos entre sesiones de app.)_

7. **¿Qué necesitas para probar tu app RN en tu celular hoy sin Mac ni cables?**
   - Expo: instalar Expo Go, correr expo start, escanear el QR en la misma red WiFi  _(El QR de Expo convierte tu teléfono en dispositivo de desarrollo instantáneo.)_

8. **¿Qué es onLongPress en un Pressable?**
   - Click mantenido: el patrón móvil para acciones secundarias como borrar/editar  _(Móvil no tiene botón derecho: long-press = menú contextual.)_

## 🧗 Profundización (prepáralas explicando en voz alta)
- ¿Qué problema real resuelve React Native y cuándo NO lo usarías?
- Explica el concepto más fuerte del curso sin usar jerga.
- Contrasta React Native con una alternativa: pros/contras.
- Cuenta un error típico de novato en este tema y cómo lo evitas.

## ⭐ Método para contestarlas
1. **Responde en 60 segundos** cada una de las fundamentales, de memoria. Las que tartamudean → repásalas (flashcards/).
2. Graba tu voz en 2 y escúchate: claridad y precisión importan tanto como el contenido técnico.
3. Una respuesta buena = definición (1 línea) + ejemplo (1) + por qué importa (1).
