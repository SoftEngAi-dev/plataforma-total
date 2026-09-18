# ⚠️ Errores comunes — 2. listas, estilos y navegación móvil

> React Native — Móvil con Tu Stack Web · Lección 2 · Aprender de los errores (propios y ajenos)

- ❌ «Es más corto» → Frente a «¿Por qué FlatList y no un map dentro de ScrollView?» lo fácil es confundirse. **Verdad**: FlatList virtualiza: solo dibuja filas visibles; ScrollView+map renderiza TODO (mata listas largas). El rendimiento de listas = virtualización. Regla: lista > ~20 items → FlatList.
- ❌ «No hay FlatList» → Frente a «¿Por qué FlatList y no un map dentro de ScrollView?» lo fácil es confundirse. **Verdad**: FlatList virtualiza: solo dibuja filas visibles; ScrollView+map renderiza TODO (mata listas largas). El rendimiento de listas = virtualización. Regla: lista > ~20 items → FlatList.
- ❌ «Por URL» → Frente a «¿Cómo pasas datos al navegar entre pantallas?» lo fácil es confundirse. **Verdad**: navigation.navigate('Detalle', { id }) y los lees con route.params en la pantalla destino. El segundo argumento navega parámetros: detalle recibe el id y trae/renderiza el dato.
- ❌ «No se puede» → Frente a «¿Cómo pasas datos al navegar entre pantallas?» lo fácil es confundirse. **Verdad**: navigation.navigate('Detalle', { id }) y los lees con route.params en la pantalla destino. El segundo argumento navega parámetros: detalle recibe el id y trae/renderiza el dato.

## 🩹 Antídoto universal
1. Lee el mensaje de error COMPLETO antes de googlear.
2. Pon el error exacto a la IA local y pide explicación, no solución.
3. Documenta el error en tu bitácora: error → causa → fix.
