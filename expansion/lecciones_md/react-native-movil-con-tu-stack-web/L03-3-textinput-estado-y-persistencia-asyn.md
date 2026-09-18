# 3. TextInput, estado y persistencia (AsyncStorage)

> 📚 Curso: **React Native — Móvil con Tu Stack Web** · Lección 3 de 4
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```jsx
FORMS CONTROLADOS + GUARDAR EN EL DISPOSITIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT CONTROLADO (el mismo patrón React)
  const [texto, setTexto] = useState("");
  <TextInput
      style={s.input}
      value={texto}
      onChangeText={setTexto}
      placeholder="Nueva nota..."
  />
  onChangeText da el string directo (no hay e.target.value en móvil).

PERSISTIR: AsyncStorage (el localStorage móvil)
  npm install @react-native-async-storage/async-storage
  import AsyncStorage from "@react-native-async-storage/async-storage";
  await AsyncStorage.setItem("notas", JSON.stringify(notas));
  const crudo = await AsyncStorage.getItem("notas");
  const notas = crudo ? JSON.parse(crudo) : [];

  Cargar al montar (useEffect + setState):  try/catch siempre.

DIFERENCIA CLAVE WEB: en móvil hay lifecycle de la app (va al background, la mata el SO...).
AppState de RN detecta "va al fondo" para guardar antes de que muera.

Para datos grandes: expo-sqlite (SQL nativa) o MMKV (clave-valor ultra rápida).
```

---

## 📝 Quiz de la lección

### 1. ¿Cómo se envía texto controlado en RN vs web?
- A) e.target.value
- B) onChangeText recibe el string directamente: setTexto(nuevoTexto)
- C) No se puede
- D) FormData
### 2. ¿Qué es AsyncStorage?
- A) Una BD SQL
- B) Almacenamiento clave-valor local (equivalente móvil de localStorage), strings+JSON
- C) Una nube
- D) Un caché HTTP

---

## 🔑 Respuestas y explicaciones

**1.** ✅ onChangeText recibe el string directamente: setTexto(nuevoTexto) — Mismo patrón controlado, pero el callback te da el texto límpio.
**2.** ✅ Almacenamiento clave-valor local (equivalente móvil de localStorage), strings+JSON — Guarda strings; con JSON.stringify/parse persistes objetos entre sesiones de app.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
