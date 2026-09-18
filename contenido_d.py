# -*- coding: utf-8 -*-
"""🧩 contenido_d — Stack moderno I (2026): Astro, Vue 3, Next.js.
Cursos orientados a proyectos web modernos y excelentes."""

CURSOS_MOD = {
    "🚀 Astro — La Web de Contenido Moderna": [
        ('''1. Islas: HTML primero, cero JS por defecto''', '''
Astro es el framework para sitios de contenido (blogs, docs, marketing,
portafolios) que envía CERO JavaScript por defecto: cada página .astro
compila a HTML estático puro. Resultado: carga instantánea, SEO perfecto.

¿Interactividad? Creas ISLAS: componentes (React, Vue, Svelte…) que se
hidratan de forma aislada sin lastrar el resto de la página. Es una MPA
(Multi-Page App) con navegación opcional tipo SPA via View Transitions.

Tu primer fichero src/pages/index.astro:
    ---
    // FRONTMATTER: corre en el SERVIDOR o en build. NUNCA llega al cliente.
    const titulo = "Hola Astro";
    const res = await fetch("https://api.example.com/datos");
    const datos = await res.json();
    ---
    <html>
      <body>
        <h1>{titulo}</h1>
        <p>{datos.mensaje}</p>
      </body>
    </html>

El frontmatter entre --- es TypeScript/JavaScript con acceso total al
backend (ficheros, bases de datos, secretos); abajo escribes HTML con
expresiones {…}. Proyecto nuevo: npm create astro@latest.''', [
            ("¿Qué envía Astro al navegador por defecto?",
             ["Un enorme bundle de JavaScript", "Solo HTML + CSS estático (cero JS)", "WebAssembly", "Un Service Worker obligatorio"],
             1, "Esa es su superpotencia: HTML estático sin JS salvo que añadas islas interactivas."),
            ("¿Qué son las <islas> de Astro?",
             ["Componentes interactivos que se hidratan de forma aislada", "Archivos del servidor", "Rutas dinámicas", "Plugins de Vite"],
             0, "Una isla (con client:load/visible…) se hidrata sola: el resto de la página sigue siendo HTML estático."),
        ]),
        ('''2. Componentes Astro: props, slots y estilos con scope''', '''
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
componente de framework como isla; Astro los mezcla sin problema.''', [
            ("¿Dónde se ejecuta el código del frontmatter (---) de un componente Astro?",
             ["En el navegador del usuario", "En el servidor o en build time", "En un Web Worker", "En el CDN"],
             1, "El frontmatter corre fuera del cliente; al navegador solo llega el HTML resultante."),
            ("¿Cómo aplica por defecto Astro las reglas de un <style> dentro de un componente?",
             ["Siempre globales", "Con scope automático solo a ese componente", "Las ignora", "Exige CSS-in-JS"],
             1, "Astro hashea las clases para que el estilo no se escape del componente."),
        ]),
        ('''3. Rutas por archivo, dinámicas y layouts''', '''
El sistema de rutas de Astro es el sistema de archivos de src/pages:
    src/pages/index.astro      →  /
    src/pages/sobre-mi.astro   →  /sobre-mi
    src/pages/blog/index.astro →  /blog
    src/pages/blog/[slug].astro → rutas dinámicas

Páginas dinámicas estáticas (SSG) con getStaticPaths:
    ---
    export function getStaticPaths() {
      return [
        { params: { slug: "primer-post" }, props: { autor: "Ana" } },
        { params: { slug: "segundo-post" } },
      ];
    }
    const { slug } = Astro.params;
    ---
    <h1>Post: {slug}</h1>

Los LAYOUTS comparten la envoltura (cabecera, pie, metas). En
src/layouts/Base.astro incluyes <slot /> y en cada página:
    <Base titulo="Inicio"><p>Contenido</p></Base>

Con SSR (output: "server" o prerender = false por página) las rutas se
generan en cada petición; si no, todo se pre-renderiza en build.''', [
            ("¿Qué combinación crea rutas estáticas tipo /blog/mi-post en Astro?",
             ["src/pages/blog/[slug].astro + getStaticPaths", "next.config.js", "un archivo routes.json", "server.js con Express"],
             0, "El [param].astro en src/pages + getStaticPaths enumera las rutas a generar en build."),
            ("¿Para qué sirve un layout con <slot /> en Astro?",
             ["Envolver páginas repitiendo cabecera y pie, metiendo el contenido dentro", "Optimizar imágenes", "Crear endpoints", "Minificar el HTML"],
             0, "El layout aporta la estructura común y cada página inyecta su contenido en el slot."),
        ]),
        ('''4. Content Collections: Markdown con tipos''', '''
La forma profesional de gestionar contenido en Astro: CONTENT COLLECTIONS.

1. Crea src/content/blog/mi-post.md con frontmatter:
    ---
    title: "Hola mundo"
    fecha: 2026-01-10
    tags: ["astro"]
    ---
    Contenido en **Markdown**…

2. Define el esquema en src/content.config.ts:
    import { defineCollection, z } from "astro:content";
    const blog = defineCollection({
      schema: z.object({ title: z.string(), fecha: z.date(),
                         tags: z.array(z.string()).optional() }),
    });
    export const collections = { blog };

3. Consulta tipada:
    import { getCollection } from "astro:content";
    const posts = await getCollection("blog");
    posts.sort((a, b) => b.data.fecha - a.data.fecha);

Ventajas: el frontmatter se valida en BUILD (si falta title, falla la
compilación), autocompletado total de entry.data, y con MDX puedes usar
componentes dentro del Markdown. Ideal para blogs y documentación.''', [
            ("¿Qué valida el esquema zod de una Content Collection?",
             ["El frontmatter de cada Markdown durante el build", "El CSS", "Las llamadas HTTP", "Nada, es decorativo"],
             0, "Si un post incumple el esquema, el build falla: contenido corrupto nunca llega a producción."),
            ("¿Cómo obtienes todas las entradas de la colección blog?",
             ["getCollection('blog')", "leyendo el directorio con fs", "fetch('/api/blog')", "una consulta SQL"],
             0, "getCollection devuelve las entradas tipadas; con entry.render() obtienes el HTML."),
        ]),
        ('''5. Hidratación con client:* y despliegue''', '''
Las directivas client controlan CUÁNDO se hidrata cada isla:
    <Contador client:load />      → al cargar la página
    <Contador client:visible />   → cuando entra en pantalla (la más eficiente)
    <Contador client:idle />      → cuando el navegador está libre
    <Contador client:only="react" /> → sin pre-render en servidor

Solo viaja el JavaScript de tus islas: una página típica pasa de ~300 KB
de JS (SPA clásica) a ~5-20 KB. Puedes mezclar frameworks: una isla React
para el carrito, otra Svelte para el buscador, todo en la misma página.

DESPLIEGUE:
  · npm run build → carpeta dist/ estática: Netlify, Vercel, Cloudflare
    Pages, GitHub Pages, cualquier hosting estático.
  · SSR: añade un adapter (node, vercel, cloudflare) y output:"server" en
    astro.config.mjs para rutas dinámicas por petición.
  · Extra moderno: <ViewTransitions /> da navegación fluida tipo SPA.''', [
            ("¿Qué directiva hidrata una isla SOLO cuando el usuario la ve en pantalla?",
             ["client:load", "client:visible", "client:only", "client:media"],
             1, "client:visible usa IntersectionObserver: cero coste hasta que la isla es visible."),
            ("¿Qué produce `astro build` por defecto?",
             ["Un ejecutable .exe", "La carpeta dist/ estática lista para cualquier hosting", "Un contenedor Docker", "Una app móvil"],
             1, "Salida 100% estática: la subes a cualquier CDN/hosting estático y vuela."),
        ]),
    ],

    "💚 Vue 3 — Composition API en Serio": [
        ('''1. El SFC y la reactividad con ref()''', '''
Vue 3 gira alrededor del SINGLE FILE COMPONENT (.vue):
    <script setup>
    // <script setup> = Composition API sin ceremonia
    import { ref } from "vue";
    const contador = ref(0);          // estado reactivo
    import Header from "./Header.vue"; // auto-usable en template
    </script>
    <template>
      <button @click="contador++">Clicks: {{ contador }}</button>
    </template>
    <style scoped>
      button { font-size: 1.2rem; }
    </style>

ref() crea una referencia reactiva: en el <script> se lee/escribe con
.value; en el template se desenvuelve sola. Para objetos grandes, reactive()
evita el .value (pero cuidado al desestructurar). {{ }} interpola texto,
@click escucha eventos (shorthand de v-on).

Proyecto real: npm create vue@latest (Vite incluido). Vue es progresivo:
puedes empezar con una etiqueta script en una página y crecer a SPA.''', [
            ("¿Cómo incrementas un ref dentro del <script setup>?",
             ["contador++", "contador.value++", "setContador(contador + 1)", "this.contador++"],
             1, "En el script los refs se manipulan con .value; en el template Vue lo desenvuelve automáticamente."),
            ("¿Qué tres bloques suele tener un Single File Component?",
             ["script, template y style", "html, css y js", "setup, render y mount", "props, state y emits"],
             0, "El SFC agrupa lógica (script), vista (template) y estilos (style) en un solo archivo .vue."),
        ]),
        ('''2. computed, watch y las directivas esenciales''', '''
VALORES DERIVADOS con computed (con caché: solo se recalcula si cambian
sus dependencias):
    import { computed } from "vue";
    const filtrados = computed(() =>
      tareas.value.filter(t => t.texto.includes(busqueda.value)));

EFECTOS con watch / watchEffect para reaccionar a cambios (fetch, logs…):
    watch(busqueda, (nuevo) => console.log("buscando", nuevo));

DIRECTIVAS del template:
  v-if / v-else-if / v-else   → render condicional real
  v-for="t in tareas" :key="t.id" → listas (¡key siempre!)
  v-model="texto"             → enlace bidireccional con inputs
  v-bind:src="url"  (o :src)  → atributos dinámicos
  v-on:click  (o @click)      → eventos; @submit.prevent, .stop

Patrón buscador: input con v-model + v-for sobre computed filtrado =
listas con filtro instantáneo sin librerías.''', [
            ("¿Qué hace computed() en Vue 3?",
             ["Calcula un valor derivado con caché, recalculando solo si cambian las dependencias", "Lanza peticiones HTTP", "Define rutas", "Compila CSS"],
             0, "El computed memoriza: si las dependencias no cambian, devuelve el valor cacheado."),
            ("¿Qué hace v-model en un input?",
             ["Enlace bidireccional: el input escribe el estado y el estado actualiza el input", "Importa módulos", "Crea bucles", "Registra eventos globales"],
             0, "v-model azucara value + @input: la vía rápida para formularios."),
        ]),
        ('''3. Componentes: props, emits y slots''', '''
JS baja por props, eventos suben por emits:
    <!-- Hijo.vue -->
    <script setup>
    const props = defineProps({ titulo: String, activa: Boolean });
    const emit = defineEmits(["guardar"]);
    </script>
    <template>
      <button @click="emit('guardar', { id: 1 })">💾 {{ titulo }}</button>
    </template>

    <!-- Padre.vue -->
    <Hijo titulo="Guardar borrador" @guardar="onGuardar" />

Las PROPS son de solo lectura en el hijo (flujo de datos predecible).
SLOTS para contenido flexible:
    <slot name="header" />  +  <template #header>…</template>

CICLO DE VIDA: onMounted(() => cargarDatos()) para iniciar fetch o
temporizadores (y onUnmounted para limpiar). Para datos que deben llegar
muy abajo sin prop drilling: provide("tema", tema) en el ancestro y
const tema = inject("tema") en cualquier descendiente.''', [
            ("¿Cómo comunica un componente hijo a su padre en Vue?",
             ["Emitiendo un evento personalizado con emit()", "Mutando la prop directamente", "Escribiendo en localStorage", "Con variables globales"],
             0, "Las props bajan, los eventos suben: el hijo emite, el padre decide qué hacer."),
            ("¿Para qué sirve provide/inject?",
             ["Pasar datos a descendientes lejanos sin retransmitir props intermedias", "Hacer peticiones HTTP", "Definir rutas", "Ejecutar tests"],
             0, "provide publica un valor en el árbol; inject lo consume a cualquier profundidad."),
        ]),
        ('''4. Pinia: el store oficial de Vue''', '''
Cuando el estado cruza muchos componentes → PINIA (sucesor de Vuex):
    // stores/tareas.js
    import { defineStore } from "pinia";
    export const useTareas = defineStore("tareas", () => {
      const lista = ref([]);                 // state
      const pendientes = computed(() =>      // getters
        lista.value.filter(t => !t.hecha));
      async function cargar() {              // actions
        lista.value = await (await fetch("/api/tareas")).json();
      }
      return { lista, pendientes, cargar };
    });

En cualquier componente:
    const tareas = useTareas();     // ¡ya está suscrito!
    tareas.cargar();

Estilo setup (como arriba) o estilo options (state/getters/actions).
Ventajas: estado central predecible, Devtools con time-travel, TypeScript
de primera y plugins (p. ej. persistencia en localStorage). Regla: el
estado LOCAL de un formulario no necesita store; el COMPARTIDO sí.''', [
            ("¿Cuál es la forma reactiva de compartir estado global en Vue 3 moderno?",
             ["Variables globales en window", "Un store de Pinia con defineStore", "Props encadenadas", "Cookies"],
             1, "Pinia es el store oficial: central, tipado y con Devtools; window es un hack frágil."),
            ("En un store de Pinia, ¿qué es un getter?",
             ["Un valor derivado del estado con caché (como computed)", "Una llamada HTTP", "Un middleware", "Un hook de montaje"],
             0, "Los getters son computed del store: se recalculan cuando cambia el estado base."),
        ]),
        ('''5. Nuxt 3: Vue full-stack''', '''
Nuxt convierte Vue en un framework full-stack de producción:

  pages/               → rutas automáticas (pages/index.vue → /)
  server/api/hola.ts   → endpoint Node: export default defineEventHandler(
                           () => ({ msg: "hola" }))  → /api/hola
  components/          → auto-import: no escribes ni un import
  composables/, utils/ → auto-import también

Datos universales (SSR + hidratación sin doble fetch):
    const { data, pending, error } =
      await useFetch("/api/tareas", { key: "tareas" });

Modos por proyecto o por ruta: SSR por defecto, SSG con nuxi generate,
SPA si quieres, e ISLAS de componentes (experimental). El servidor Nitro
despliega igual en Node, Vercel, Netlify, Cloudflare Workers o Deno.

Meta-framework moderno: app.vue como raíz, <NuxtPage /> como outlet,
useSeoMeta() para SEO, middleware de rutas (definePageMeta({ middleware:
"auth" })) para proteger páginas.''', [
            ("¿Qué carpeta de Nuxt genera las rutas automáticamente?",
             ["routes/", "pages/", "views/", "public/"],
             1, "Cada .vue dentro de pages/ se convierte en ruta sin configurar ningún router."),
            ("¿Dónde defines endpoints de backend en Nuxt 3?",
             ["en server/api/", "en la carpeta pages/", "en un Express aparte obligatorio", "en nuxt.config solo"],
             0, "server/api/*.ts son endpoints Node del mismo proyecto, con despliegue integrado vía Nitro."),
        ]),
    ],

    "▲ Next.js — El React Moderno": [
        ('''1. App Router: Server Components por defecto''', '''
Next.js 14/15 con APP ROUTER cambia las reglas: en la carpeta app/,
TODOS los componentes son REACT SERVER COMPONENTS salvo que digas lo
contrario. Eso significa:
  · Se ejecutan en el servidor; su JavaScript NO viaja al navegador.
  · Pueden ser async y leer bases de datos, ficheros o secretos directo.

    // app/panel/page.tsx   →  ruta /panel
    import db from "@/lib/db";
    export default async function Panel() {
      const pedidos = await db.query("SELECT * FROM pedidos");
      return <ul>{pedidos.map(p => <li key={p.id}>{p.total}</li>)}</ul>;
    }

Convenciones por carpeta:
  page.tsx     → la ruta en sí        layout.tsx → envoltura persistente
  loading.tsx  → fallback automático  error.tsx  → Error Boundary
  not-found.tsx→ 404 por segmento

Menos JS enviado, primera carga rapidísima, y acceso a datos sin APIs
intermedias. Proyecto: npx create-next-app@latest (App Router activo).''', [
            ("¿Qué es un React Server Component en Next.js App Router?",
             ["Un componente que se renderiza en el servidor y no envía su JS al cliente", "Un microservicio", "Un Web Worker", "Una librería de CSS"],
             0, "Corre en el servidor: puede usar async/await y recursos backend sin exponerlos al navegador."),
            ("¿Qué archivo crea la ruta /dashboard en el App Router?",
             ["app/dashboard/page.tsx", "pages/dashboard.tsx", "app/routes/dashboard.ts", "src/dashboard.jsx"],
             0, "En app/, cada carpeta con page.tsx es una ruta; layouts y loading se anidan por segmento."),
        ]),
        ('''2. 'use client': el borde servidor/navegador''', '''
Cuando necesitas interactividad (useState, useEffect, onClick, contexto,
librerías de terceros con eventos), marca el archivo:
    "use client";
    import { useState } from "react";
    export default function Buscador({ sugerencias }) {
      const [q, setQ] = useState("");
      return <input value={q} onChange={e => setQ(e.target.value)} />;
    }

Regla de oro: coloca el 'use client' LO MÁS ABAJO POSIBLE en el árbol
(hojas interactivas). La página sigue siendo Server Component, obtiene
datos y pasa props SERIALIZABLES (strings, números, JSON) a los clientes.

Ojo: un Client Component TAMBIÉN se pre-renderiza en el servidor en la
primera carga (html inicial rápido) y luego se hidrata. No es "solo
navegador"; es "servidor + interactividad posterior".

Patrón moderno: server para datos y estructura, client para botones,
formularios, animaciones y estado local.''', [
            ("¿Qué obliga escribir 'use client' al inicio de un componente?",
             ["Usar useState, useEffect o manejadores como onClick", "Hacer fetch de datos", "Devolver JSX", "Exportar metadata"],
             0, "Esas APIs son del navegador; sin la directiva el componente se trata como Server Component y falla."),
            ("¿Dónde conviene ubicar la directiva 'use client' para optimizar el bundle?",
             ["En la raíz de toda la app", "En los componentes hoja interactivos, lo más abajo posible", "En todos los archivos por igual", "En el layout.tsx"],
             1, "Cuanto más abajo, menos JS viaja: el resto del árbol permanece como Server Components."),
        ]),
        ('''3. Datos: fetch con caché, loading.tsx y error.tsx''', '''
En un Server Component pides datos donde los pintas, sin useEffect:
    export default async function Noticias() {
      const res = await fetch("https://api.site.com/noticias",
                              { next: { revalidate: 60 } });  // ISR: 60 s
      const noticias = await res.json();
      return noticias.map(n => <Article key={n.id} {...n} />);
    }

Estrategias de caché de fetch:
   force-cache (por defecto en build)  → estático
   next: { revalidate: N }             → regenera cada N segundos (ISR)
   cache: "no-store"                   → siempre fresco (tiempo real)

UX gratis por convención:
  loading.tsx → se muestra al instante como fallback (Suspense implícito)
  error.tsx   → captura errores del segmento con botón "reintentar"
  generateStaticParams() → pre-genera rutas dinámicas en build

Adiós al spinners-everywhere: el HTML llega con datos; el streaming
envía lo listo primero y el resto cuando termina.''', [
            ("¿Cómo se cargan datos en un Server Component de Next.js?",
             ["Con await fetch directamente en el cuerpo async del componente", "Solo con useEffect", "Únicamente desde una API externa", "Con jQuery"],
             0, "Al ejecutarse en el servidor, hacer await fetch en el componente es la vía natural y eficiente."),
            ("¿Para qué sirve loading.tsx en una ruta?",
             ["Muestra un fallback al instante mientras el segmento termina de cargar", "Bloquea la navegación", "Define la página 404", "Minifica el JS"],
             0, "Es un boundary de Suspense declarativo: el usuario ve esqueleto/UI de carga sin programarla."),
        ]),
        ('''4. Server Actions: mutaciones sin escribir APIs''', '''
Las SERVER ACTIONS son funciones del servidor llamables desde la UI:
    // app/actions.ts
    "use server";
    import { revalidatePath } from "next/cache";
    import { z } from "zod";
    export async function crearTarea(formData) {
      const t = z.object({ texto: z.string().min(1) })
                 .parse({ texto: formData.get("texto") }); // ¡validar!
      await db.tarea.create({ data: t });
      revalidatePath("/tareas");          // refresca la caché
    }

    // app/tareas/page.tsx (Server Component)
    <form action={crearTarea}>
      <input name="texto" />
      <button>Nueva tarea</button>
    </form>

El form funciona INCLUSO SIN JAVASCRIPT (enhancement progresivo), y con
JS da UX instantánea. Hooks de apoyo en client: useActionState (estado/
errores), useFormStatus (pending del botón). Para APIs públicas o
webhooks: app/api/hola/route.ts con export async function POST().

Seguridad: cada action es un endpoint público → valida entradas y
permisos SIEMPRE dentro; nunca confíes en hidden inputs.''', [
            ("¿Qué es una Server Action?",
             ["Una función que corre en el servidor invocable desde la UI sin escribir un endpoint", "Un Service Worker", "Un middleware de Express", "Un hook de React"],
             0, "Con 'use server' declaras funciones backend llamables: Next genera el canal seguro automáticamente."),
            ("¿Qué debes hacer SIEMPRE dentro de una Server Action?",
             ["Validar entradas y comprobar permisos", "Confiar en los datos del formulario", "Guardar en localStorage", "Llamar a alert()"],
             0, "El cliente puede enviar cualquier cosa: la action es tu última línea de defensa (zod + auth)."),
        ]),
        ('''5. SEO, next/image y despliegue''', '''
SEO declarativo por página:
    export const metadata = {
      title: "Mi tienda — Inicio",
      description: "Todo en 24 h",
      openGraph: { images: ["/og.png"] },
    };
( o export async function generateMetadata({ params }) para dinámico ).

next/image optimiza sola: tamaño responsive, formato moderno (webp/avif),
lazy loading y SIN saltos de layout:
    import Image from "next/image";
    <Image src="/hero.jpg" alt="" width={1200} height={600} priority />

next/font carga fuentes sin CLS: import { Inter } from "next/font/google".

DESPLIEGUE:
  · Vercel: git push y listo (creadores de Next).
  · Self-host: next build && next start, o imagen Docker con output:
    "standalone".
  · middleware.ts: auth, redirects e i18n en el edge, antes de la ruta.''', [
            ("¿Qué ventaja principal da next/image frente a una <img> normal?",
             ["Optimiza tamaño/formato y evita saltos de layout (CLS)", "Permite GIFs", "Sube la imagen a la nube", "Añade filtros Instagram"],
             0, "Reserva el espacio, sirve webp/avif responsive y carga diferida: métricas Core Web Vitals sanas."),
            ("¿Cómo defines el <title> y la descripción de una página en el App Router?",
             ["export const metadata en page.tsx", "Editando public/index.html", "Con useEffect", "En el package.json"],
             0, "metadata por segmento (objeto o generateMetadata async) alimenta <title>, meta y Open Graph."),
        ]),
    ],
}
