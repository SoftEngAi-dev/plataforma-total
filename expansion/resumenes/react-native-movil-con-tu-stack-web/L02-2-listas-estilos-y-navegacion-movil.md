# ⚡ Cheatsheet — 2. listas, estilos y navegación móvil

> React Native — Móvil con Tu Stack Web · Lección 2 · 18/09/2026

## 💡 Idea central
FLATLIST + FLEXBOX + SCREENS

## 🧠 Autoexamen (tápate la respuesta)
- **¿Por qué FlatList y no un map dentro de ScrollView?** → FlatList virtualiza: solo dibuja filas visibles; ScrollView+map renderiza TODO (mata listas largas) _(El rendimiento de listas = virtualización. Regla: lista > ~20 items → FlatList.)_
- **¿Cómo pasas datos al navegar entre pantallas?** → navigation.navigate('Detalle', { id }) y los lees con route.params en la pantalla destino _(El segundo argumento navega parámetros: detalle recibe el id y trae/renderiza el dato.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
