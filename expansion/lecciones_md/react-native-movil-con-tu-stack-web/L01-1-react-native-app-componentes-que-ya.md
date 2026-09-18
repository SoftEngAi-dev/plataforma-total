# 1. React Native: App = componentes que ya sabes

> 📚 Curso: **React Native — Móvil con Tu Stack Web** · Lección 1 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
REACT NATIVE: REACT QUE COMPILA A NATIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tus componentes React renderizan a vistas NATIVAS de iOS/Android (no es un WebView: es UI real). Si sabes React, estás al 80%.

EQUIVALENCIAS (traducción directa de tu HTML)
  <div>        → <View>
  <p>/<span>   → <Text>     (¡todo texto va dentro de Text!)
  <img>        → <Image source={...}>
  <button>     → <Pressable onPress={fn}> o <Button title=... onPress={fn}>
  CSS inline   → style con StyleSheet.create (flexbox Y CSS-like, unidades sin "px")

  import { View, Text, Pressable, StyleSheet } from "react-native";
  export default function Hola() {
      return (
          <View style={estilos.pantalla}>
              <Text style={estilos.titulo}>¡Hola móvil!</Text>
              <Pressable style={estilos.boton} onPress={() => alert("¡clic!")}>
                  <Text>Soy un botón</Text>
              </Pressable>
          </View>
      );
  }
  const estilos = StyleSheet.create({
      pantalla: { flex: 1, justifyContent: "center", alignItems: "center" },
      titulo: { fontSize: 28, fontWeight: "bold" },
      boton: { backgroundColor: "#6f42c1", padding: 12, borderRadius: 8 },
  });

EXPO: la herramienta que hace el setup trivial:
  npx create-expo-app miapp && cd miapp && npx expo start
Escanneas un QR con tu celu (app Expo Go) y ves la app EN TU TELÉFONO en segundos. Magia.
```

---

## 📝 Quiz de la lección

### 1. ¿En qué difiere React Native de una WebView/web app empaquetada?
- A) Son iguales
- B) RN compila tus componentes a widgets NATIVOS reales (rendimiento verdadero), no embebe una web
- C) Es HTML nativo
- D) Usa Flutter
### 2. ¿Qué hace Expo en el flujo RN?
- A) Otro lenguaje
- B) Toolchain que elimina el setup nativo: QR al teléfono, hot reload, build en la nube
- C) Una BD
- D) Un navegador

---

## 🔑 Respuestas y explicaciones

**1.** ✅ RN compila tus componentes a widgets NATIVOS reales (rendimiento verdadero), no embebe una web — RN renderiza UIView/View nativas: por eso se siente app de verdad, no página.
**2.** ✅ Toolchain que elimina el setup nativo: QR al teléfono, hot reload, build en la nube — Con Expo arrancas sin Xcode/Android Studio instalado: la puerta de entrada estándar.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
