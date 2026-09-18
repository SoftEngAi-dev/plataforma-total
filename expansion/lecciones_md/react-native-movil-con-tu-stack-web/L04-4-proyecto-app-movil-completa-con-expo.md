# 4. Proyecto: app móvil completa con Expo

> 📚 Curso: **React Native — Móvil con Tu Stack Web** · Lección 4 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
CONSTRUYE: TU APP DE NOTAS MÓVIL EN TU CELULAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. npx create-expo-app notasapp && cd notasapp
2. npm install @react-native-async-storage/async-storage
3. App.js: estado notas (useState) + cargar de AsyncStorage en useEffect + guardar en cada cambio
4. UI: SafeAreaView → TextInput + botón Agregar → FlatList de notas con keyExtractor
5. Borrar: Pressable onLongPress sobre cada item (long-press = click derecho móvil) o botón 🗑 por fila
6. Estilos nítidos: flex:1 raíz · tarjetas con padding 16, borderRadius 12, marginBottom 8, elevation:2 (sombra android) / boxShadow iOS
7. npx expo start → abre Expo Go en tu celu (App Store/Play) → escanea el QR → MISMA WIFI → tu app real en tu mano
8. Bonus nivel calle: pull-to-refresh con RefreshControl en FlatList · modo oscuro con useColorScheme()

BUILD PARA DISTRIBUIR: eas build -p android (APK en la nube, gratis en tier) → lo compartes.
EAS Submit → stores, cuando seas grande. No necesitas Mac para Android ahora.

EL MOMENTO MÁGICO: la app corriendo EN TU PROPIA MANO, construida por ti. Ese es el enganche del desarrollo móvil.
```

---

## 📝 Quiz de la lección

### 1. ¿Qué necesitas para probar tu app RN en tu celular hoy sin Mac ni cables?
- A) Un emulador
- B) Expo: instalar Expo Go, correr expo start, escanear el QR en la misma red WiFi
- C) Una Mac sí o sí
- D) Un AWS
### 2. ¿Qué es onLongPress en un Pressable?
- A) Error
- B) Click mantenido: el patrón móvil para acciones secundarias como borrar/editar
- C) Doble click
- D) Hover

---

## 🔑 Respuestas y explicaciones

**1.** ✅ Expo: instalar Expo Go, correr expo start, escanear el QR en la misma red WiFi — El QR de Expo convierte tu teléfono en dispositivo de desarrollo instantáneo.
**2.** ✅ Click mantenido: el patrón móvil para acciones secundarias como borrar/editar — Móvil no tiene botón derecho: long-press = menú contextual.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
