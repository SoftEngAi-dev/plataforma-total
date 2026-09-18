# 2. Componentes Astro: props, slots y estilos con scope

> 📚 Curso: **🚀 Astro — La Web de Contenido Moderna** · Lección 2 de 5
> 🗓 Exportado: 18/09/2026 desde Plataforma Total
> 🍅 Sugerencia: 1-2 pomodoros para leer + practicar

---

## 📖 Contenido

```text

Los componentes .astro (en src/components) son piezas reutilizables que se
renderizan SIEMPRE en build/servidor: no se hidratan, no envían JS.

    ---  // src/components/Tarjeta.astro
    const { titulo, categoria = "general" } = Astro.props;
    ---
    <article class="tarjeta">
      <h2>{titulo}</h2>
      <span>{categoria}</span>
      <slot />   <!-- aquí entra el contenido hijo -->
    </article>
    <style>
      .tarjeta { border: 1px solid #ddd; border-radius: 12px; }
    </style>

Uso:
    <Tarjeta titulo="Mi post">
      <p>Este contenido viaja por el slot.</p>
    </Tarjeta>

Claves: props tipadas (opcional con TypeScript e interfaces), <slot /> como
children, y <style> con SCOPE automático: solo aplica a ese componente,
adiós colisiones de CSS. Si necesitas reactividad (clicks, estado), usa un
componente de framework como isla; Astro los mezcla sin problema.
```

---

## 📝 Quiz de la lección

### 1. ¿Dónde se ejecuta el código del frontmatter (---) de un componente Astro?
- A) En el navegador del usuario
- B) En el servidor o en build time
- C) En un Web Worker
- D) En el CDN
### 2. ¿Cómo aplica por defecto Astro las reglas de un <style> dentro de un componente?
- A) Siempre globales
- B) Con scope automático solo a ese componente
- C) Las ignora
- D) Exige CSS-in-JS

---

## 🔑 Respuestas y explicaciones

**1.** ✅ En el servidor o en build time — El frontmatter corre fuera del cliente; al navegador solo llega el HTML resultante.
**2.** ✅ Con scope automático solo a ese componente — Astro hashea las clases para que el estilo no se escape del componente.

---
✅ Al terminar, marca la lección como completada en la app (📚 Aprender → ✅ Completada)
