# 2. listas, estilos y navegación móvil

> 📚 Curso: **React Native — Móvil con Tu Stack Web** · Lección 2 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
FLATLIST + FLEXBOX + SCREENS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
LISTAR RÁPIDO (nunca map en ScrollView largo)
  import { FlatList } from "react-native";
  <FlatList
      data={notas}
      keyExtractor={(item) => item.id}
      renderItem={({ item }) => <Text style={s.item}>{item.titulo}</Text>}
  />
FlatList renderiza solo lo visible (virtualizada): miles de filas suaves.

FLEXBOX CON SABOR MÓVIL: todo es flex por defecto, mainAxisAlignment = justifyContent:
  { flex: 1 } en la pantalla raíz SIEMPRE (que ocupe todo)
  { flexDirection: "row" } para horizontal; gap: 8; padding: 16
Las unidades son números sin "px" (density-independent pixels automáticos).

NAVEGACIÓN (react-navigation, el estándar):
  npm install @react-navigation/native @react-navigation/native-stack
  const Stack = createNativeStackNavigator();
  <NavigationContainer>
    <Stack.Navigator>
      <Stack.Screen name="Inicio" component={Home} />
      <Stack.Screen name="Detalle" component={Detail} />
    </Stack.Navigator>
  </NavigationContainer>
  // navegar: navigation.navigate("Detalle", { id: item.id })
```

---

## 📝 Quiz de la lección

### 1. ¿Por qué FlatList y no un map dentro de ScrollView?
- A) Es más corto
- B) FlatList virtualiza: solo dibuja filas visibles; ScrollView+map renderiza TODO (mata listas largas)
- C) No hay FlatList
- D) Es Apple
### 2. ¿Cómo pasas datos al navegar entre pantallas?
- A) Por URL
- B) navigation.navigate('Detalle', { id }) y los lees con route.params en la pantalla destino
- C) No se puede
- D) Con fetch

---

## 🔑 Respuestas y explicaciones

**1.** ✅ FlatList virtualiza: solo dibuja filas visibles; ScrollView+map renderiza TODO (mata listas largas) — El rendimiento de listas = virtualización. Regla: lista > ~20 items → FlatList.
**2.** ✅ navigation.navigate('Detalle', { id }) y los lees con route.params en la pantalla destino — El segundo argumento navega parámetros: detalle recibe el id y trae/renderiza el dato.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
