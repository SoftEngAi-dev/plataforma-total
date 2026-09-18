# 📕 Resumen maestro — React Native — Móvil con Tu Stack Web

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. React Native: App = componentes que ya sabes
REACT NATIVE: REACT QUE COMPILA A NATIVO ━━━━━━━━━━━━━━━━━━━━━━━━━━━ Tus componentes React renderizan a vistas NATIVAS de iOS/Android (no es un WebView: es UI real). Si sabes React…

## 2. 2. listas, estilos y navegación móvil
FLATLIST + FLEXBOX + SCREENS ━━━━━━━━━━━━━━━━━━━━━━━━━━━ LISTAR RÁPIDO (nunca map en ScrollView largo)   import { FlatList } from "react-native";   <FlatList       data={notas}    …

## 3. 3. TextInput, estado y persistencia (AsyncStorage)
FORMS CONTROLADOS + GUARDAR EN EL DISPOSITIVO ━━━━━━━━━━━━━━━━━━━━━━━━━━━ INPUT CONTROLADO (el mismo patrón React)   const [texto, setTexto] = useState("");   <TextInput       styl…

## 4. 4. Proyecto: app móvil completa con Expo
CONSTRUYE: TU APP DE NOTAS MÓVIL EN TU CELULAR ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1. npx create-expo-app notasapp && cd notasapp 2. npm install @react-native-async-storage/async-storage 3…

---
✅ 4 lecciones · 📝 8 preguntas de repaso en quizzes_html/ · tests/