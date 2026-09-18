# -*- coding: utf-8 -*-
"""🧩 contenido_e — Stack moderno II (2026): Tailwind, SvelteKit, Bun/Deno.
Herramientas que definen cómo se construyen hoy los proyectos punteros."""

CURSOS_MOD = {
    "🎨 Tailwind CSS — Diseño a Velocidad": [
        ('''1. Utility-first: pensar en clases pequeñas''', '''
Tailwind rompe con el CSS tradicional: en vez de inventar clases
(.boton-primario con 8 propiedades), COMPONES con utilidades de un solo
propósito directamente en el HTML:
    <button class="px-4 py-2 rounded-lg bg-indigo-600 text-white
                   font-semibold hover:bg-indigo-500 transition">
      Guardar
    </button>

Ventajas reales: no hay nombres que inventar ni CSS muerto que nadie
borra, la escala de espaciados/colores fuerza consistencia de diseño, y
prototipas pantallas completas sin salir del HTML.

Instalación moderna (v4) con Vite: importas "tailwindcss" y en tu CSS:
@import "tailwindcss"; — el motor genera SOLO las clases que usas.
Para jugar sin instalar nada: <script src="https://cdn.tailwindcss.com">.

Vocabulario esencial: p-4 m-2 (padding/margin), w-full max-w-md,
text-lg font-bold text-slate-600, bg-white, rounded-xl shadow-lg,
border border-slate-200, flex (¡la siguiente lección profundiza!).''', [
            ("¿Qué es el enfoque utility-first de Tailwind?",
             ["Componer el diseño con muchas clases de un solo propósito en el HTML", "Escribir todo el CSS a mano con !important", "Usar solo CSS-in-JS", "Poner estilos inline en cada etiqueta"],
             0, "Muchas utilidades pequeñas y predecibles que se combinan: el diseño vive junto al marcado."),
            ("¿Por qué el CSS final en producción con Tailwind es pequeño?",
             ["Porque solo se generan las clases que realmente usas", "Porque se borra todo el CSS", "Porque se usa el CDN", "Porque Tailwind no genera CSS"],
             0, "El compilador detecta las clases presentes en tus archivos y emite únicamente esas reglas."),
        ]),
        ('''2. Layout: flexbox, grid y responsive móvil primero''', '''
Maquetar con Tailwind es aplicar flexbox/grid por utilidades:
    <nav class="flex items-center justify-between gap-4 px-6 py-3">
    <section class="grid grid-cols-3 gap-6">
    <main class="container mx-auto px-4">

flex items-center justify-between  → barra con logo a un lado y menú al otro
grid grid-cols-3 gap-6             → tarjetas en 3 columnas
container mx-auto px-4             → contenido centrado y acolchado

RESPONSIVE móvil primero (los prefijos significan "desde esta medida
HACIA ARRIBA"):
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
  · sin prefijo → estilo base para móvil
  · md: → a partir de 768px   · lg: → a partir de 1024px

Visibilidad: hidden md:block (oculto en móvil, visible en escritorio)
para menús hamburguesa. Diseña primero la pantalla pequeña y escala.''', [
            ("¿Qué significa la clase md:grid-cols-3?",
             ["3 columnas a partir del breakpoint md (768px) hacia arriba", "3 columnas solo en móvil", "3 filas", "Un margen de 3 píxeles"],
             0, "Tailwind es mobile-first: el base es móvil y los prefijos md:/lg: aplican hacia arriba."),
            ("¿Cómo centras horizontalmente un contenedor con ancho máximo?",
             ["con la clase mx-auto (más max-w-* o container)", "con text-center", "con float:center", "con grid"],
             0, "mx-auto reparte el margen lateral; text-center solo alinea texto en línea."),
        ]),
        ('''3. Estados y variantes: hover, dark: y group''', '''
Los pseudo-estados CSS son prefijos:
    <button class="bg-indigo-600 hover:bg-indigo-500 active:scale-95
                   focus:ring-2 ring-indigo-300 transition">
    <input class="border focus:border-indigo-500 focus:outline-none" />

Soporte oscuro con dark: (modo clase, recomendado):
    <html class="dark">  →  <body class="bg-white dark:bg-slate-900
                                         text-slate-900 dark:text-slate-100">

GRUPOS: el hijo reacciona al estado del padre:
    <a class="group p-4 hover:bg-slate-100">
      <span class="group-hover:text-indigo-600">Ver más →</span>
    </a>

Listas y posiciones: odd:bg-slate-50 even:bg-white (tablas cebra),
first:rounded-t-xl last:rounded-b-xl.

Y anima cambios con transition, duration-300, ease-out: dale vida sin
escribir keyframes (aunque también existen: animate-pulse, animate-spin).''', [
            ("¿Cómo haces que un hijo cambie cuando el padre recibe hover?",
             ["Con group en el padre y group-hover: en el hijo", "Con JavaScript obligatorio", "Con media queries", "No se puede con CSS"],
             0, "group marca el contenedor; group-hover:aplica-estilo solo cuando el grupo está en hover."),
            ("¿Qué hace la clase transition en un botón?",
             ["Anima suavemente los cambios de propiedades (color, escala…) entre estados", "Oculta el botón", "Cambia el tipo de letra", "Añade un borde"],
             0, "transition + duration-* suaviza hover/active/focus sin escribir @keyframes."),
        ]),
        ('''4. Personalizar el tema, @apply y valores arbitrarios''', '''
Tu marca, tu tema. En Tailwind v4 personalizas en el propio CSS:
    @import "tailwindcss";
    @theme {
      --color-marca: #7c3aed;
      --font-display: "Space Grotesk", sans-serif;
    }
    → ya existen las clases bg-marca, text-marca, font-display…

(En v3 se hacía en tailwind.config.js con theme.extend.)

Cuando repites MUCHO un combo, extráelo con @apply (con moderación):
    .btn { @apply px-4 py-2 rounded-lg font-semibold transition; }
    .btn-primario { @apply btn bg-indigo-600 text-white hover:bg-indigo-500; }

Valores arbitrarios puntuales con corchetes:
    w-[347px]  grid-cols-[1fr_280px]  text-[15px]  top-[-6px]

Plugins oficiales: @tailwindcss/typography (prose para Markdown),
forms. Regla de buen gusto: primero utilidades; si el HTML se vuelve
ilegible, crea un COMPONENTE (React/Vue/Astro) antes que 30 @apply.''', [
            ("En Tailwind v4, ¿dónde defines colores de marca personalizados?",
             ["En el bloque @theme de tu archivo CSS", "En un XML", "En el HTML", "En package.json"],
             0, "@theme genera tokens (p. ej. --color-marca) que se convierten en clases como bg-marca automáticamente."),
            ("¿Para qué sirve @apply?",
             ["Reutilizar un conjunto de utilidades dentro de una clase propia", "Importar fuentes", "Hacer responsive", "Generar el build"],
             0, "@apply incrusta utilidades en .mi-clase (útil para patrones repetidos), aunque los componentes suelen abstraer mejor."),
        ]),
        ('''5. Producción: shadcn/ui, accesibilidad y buenas prácticas''', '''
En producción el JIT genera solo lo usado: no hay "purgado" manual que
configurar; evita componer nombres de clase en strings dinámicos
(`bg-${color}-500` NO se detectará → usa objetos/mapas de clases completas).

El ecosistema moderno:
  · shadcn/ui: componentes ACCESIBLES (Radix) + Tailwind que COPIAS a tu
    repo (son tuyos, no una dependencia) → diálogos, menús, tablas…
  · Headless UI: comportamiento sin estilos para Vue/React.

Accesibilidad (no negociable en proyectos excelentes):
  · Contraste suficiente (text-slate-600 sobre blanco ≈ AA).
  · focus-visible:ring-2 para navegación con teclado.
  · sr-only para textos solo para lectores de pantalla.

Orden y legibilidad: agrupa clases por bloques (layout → box → texto →
visual → estados), usa el plugin oficial de Prettier para ordenarlas
automáticamente, y extrae componentes cuando la cadena supera lo cómodo.''', [
            ("¿Qué es shadcn/ui?",
             ["Componentes accesibles (Radix + Tailwind) que copias a tu proyecto y son tuyos", "Un framework de CSS rival", "Un plugin de jQuery", "Una librería de iconos"],
             0, "No es una dependencia: copia el código del componente a tu repo, con accesibilidad Radix y estilos Tailwind incluidos."),
            ("¿Qué clase de Tailwind muestra un texto solo a lectores de pantalla?",
             ["sr-only", "hidden", "invisible", "opacity-0"],
             0, "sr-only lo oculta visualmente pero mantiene accesibilidad para tecnologías asistivas."),
        ]),
    ],

    "🔥 SvelteKit & Svelte 5 — Apps Completas": [
        ('''1. Svelte 5 con runas: reactividad sin Virtual DOM''', '''
Svelte COMPILA sus componentes a JavaScript quirúrgico: no hay Virtual
DOM en runtime, por eso es tan rápido y liviano. En Svelte 5 la
reactividad se declara con RUNAS:
    <script>
      let n = $state(0);                 // estado reactivo
      let usuario = $state({ nombre: "Ana" });
      const doble = $derived(n * 2);     // valor derivado
      $effect(() => console.log("n vale", n));  // efectos
      let { titulo = "Sin título" } = $props(); // props
    </script>
    <button onclick={() => n++}>Clicks: {n} (doble: {doble})</button>

    <style> button { color: teal; } </style>

Bloques de plantilla potentes: {#if cond}…{/if}, {#each lista as item
(item.id)}…{/each}, {#await promesa}…{/await}. El CSS es scoped por
defecto. Arrancar: npx sv create. Menos magia, menos código, más render
directo: una de las experiencias de desarrollo mejor valoradas.''', [
            ("¿Cómo se declara estado reactivo en Svelte 5?",
             ["Con la runa $state()", "Con setState()", "Con data()", "Con new Reactive()"],
             0, "$state(0) crea una variable reactiva; $derived deriva valores y $effect ejecuta efectos."),
            ("¿Qué NO utiliza Svelte en tiempo de ejecución?",
             ["El Virtual DOM", "JavaScript", "CSS", "HTML"],
             0, "Svelte compila a actualizaciones quirúrgicas del DOM real: sin VDOM, menos memoria y más velocidad."),
        ]),
        ('''2. SvelteKit: rutas +page y datos con load''', '''
SvelteKit es el framework full-stack de Svelte. Rutas por archivos en
src/routes:
    src/routes/+page.svelte          → /
    src/routes/sobre/+page.svelte    → /sobre
    src/routes/blog/[slug]/+page.svelte → /blog/cualquiera
    +layout.svelte → envoltura compartida (con <slot /> o {@render children()})

DATOS con load (antes de renderizar):
    // src/routes/blog/[slug]/+page.js
    export async function load({ params, fetch }) {
      const res = await fetch(`/api/posts/${params.slug}`);
      return { post: await res.json() };
    }
    <!-- +page.svelte -->
    <script> let { data } = $props(); </script>
    <h1>{data.post.titulo}</h1>

load universal (+page.js) corre en servidor la 1ª vez y en el cliente al
navegar; +page.server.js SOLO en servidor (para secretos/DB). Streaming
con promises, forms con actions (siguiente lección) y endpoints API con
+server.js. SSR + hidratación + navegación cliente, todo de serie.''', [
            ("¿Qué archivo dentro de src/routes/blog crea la ruta /blog?",
             ["+page.svelte", "index.html", "routes.js", "blog.svelte"],
             0, "La convención de SvelteKit: +page.svelte marca la página; los directorios definen el path."),
            ("¿Cuándo se ejecuta la función load universal de +page.js?",
             ["En la primera carga en el servidor y después en el cliente al navegar", "Solo en build", "Nunca en el servidor", "Solo en tests"],
             0, "Es universal: SSR primero, y hidratación cliente en las navegaciones siguientes (con fetch especial)."),
        ]),
        ('''3. Form actions: el regreso glorioso del <form>''', '''
SvelteKit abraza la plataforma web: los formularios clásicos funcionan
SIN JavaScript y con JS se comportan como SPA (enhancement progresivo).

    <!-- +page.svelte -->
    <form method="POST" action="?/crear">
      <input name="texto" required />
      <button>Añadir</button>
    </form>

    // +page.server.js
    import { fail } from "@sveltejs/kit";
    export const actions = {
      crear: async ({ request }) => {
        const data = await request.formData();
        const texto = data.get("texto")?.toString().trim();
        if (!texto) return fail(422, { error: "Texto obligatorio" });
        await db.insertar({ texto });
        return { ok: true };
      },
    };

En la página, export let form (o $props()) recibe lo devuelto: errores de
validación sin estado manual. Con use:enhance obtienes comportamiento SPA
y mejor UX. acciones nombradas: ?/crear, ?/borrar por formulario.
Valida SIEMPRE en el servidor (zod/valibot encajan perfecto).''', [
            ("¿Funciona un <form> de SvelteKit sin JavaScript?",
             ["Sí: enhancement progresivo, funciona como formulario clásico", "No, siempre requiere JS", "Solo en Chrome", "Solo con use:enhance"],
             0, "Ese es su punto fuerte: con JS es SPA; sin JS sigue funcionando vía POST estándar."),
            ("¿Cómo devuelves un error de validación al formulario desde una action?",
             ["Con fail(422, { error })", "Con alert()", "Con console.log", "Con redirect(404)"],
             0, "fail devuelve al navegador el estado y un objeto que la página lee en la prop form."),
        ]),
        ('''4. Endpoints +server.js, adapters y despliegue''', '''
APIs con endpoints de archivo:
    // src/routes/api/tareas/+server.js
    import { json } from "@sveltejs/kit";
    export async function GET() {
      return json([{ id: 1, texto: "Aprender SvelteKit" }]);
    }
    export async function POST({ request }) {
      const body = await request.json();
      // guardar…
      return json(body, { status: 201 });
    }

ADAPTERS: el mismo proyecto compila para donde despliegues:
  · adapter-auto    → detecta Vercel/Netlify/Cloudflare
  · adapter-node    → tu VPS o contenedor Docker
  · adapter-static  → SSG puro (sitios sin servidor)
Pre-render por página: export const prerender = true.

Variables de entorno seguras: $env/static/private jamás llega al cliente;
$env/dynamic/public para valores públicos.

Svelte 5 + SvelteKit destaca en Core Web Vitals: menos JS enviado,
rendimiento de compilador. Ideal para apps completas modernas con
presupuesto de bytes ajustado.''', [
            ("¿Cómo creas un endpoint JSON en SvelteKit?",
             ["Con un archivo +server.js que exporta funciones GET/POST", "Con una carpeta /api de Next", "Con localStorage", "Con ngrok"],
             0, "+server.js en una ruta define handlers HTTP que devuelven json() personalizados."),
            ("¿Qué adapter eliges para desplegar SvelteKit en tu propio contenedor Docker?",
             ["adapter-node", "adapter-static", "adapter-auto", "ninguno"],
             0, "adapter-node genera un servidor Node independiente, perfecto para VPS o Docker."),
        ]),
    ],

    "🍞 Bun & Deno — Los Nuevos Runtimes": [
        ('''1. Por qué existen: más allá de Node''', '''
Node.js (2009) no se diseñó para TypeScript, ESM primero ni seguridad
moderna. Dos runtimes modernos lo repiensan:

BUN (escrito en Zig): arranque en milisegundos, y es 4 herramientas en 1
— runtime, BUNDLER, TEST RUNNER y GESTOR DE PAQUETES (bun install es
muchísimo más rápido que npm). Compatible con APIs de Node y con tu
package.json: puedes probarlo en proyectos actuales casi sin cambios.

DENO (escrito en Rust, del creador original de Node): TypeScript NATIVO
sin paso de build, SEGURO por defecto (el código no toca red ni disco sin
permisos explícitos), estándar moderna (@std) y registro propio JSR.

¿Cuándo usar cada uno?
  · Bun: velocidad extrema y tooling en ecosistemas Node actuales.
  · Deno: proyectos TypeScript estrictos, scripts seguros y edge
    (Deno Deploy reparte tu app por el mundo sin servidores).''', [
            ("¿Qué incluye Bun además del runtime?",
             ["Bundler, test runner y gestor de paquetes", "Una base de datos", "Un editor de código", "Un navegador"],
             0, "Bun unifica herramientas: bun install, bun test y el bundler vienen de serie, todo muy rápido."),
            ("¿Cuál es el principio de seguridad por defecto de Deno?",
             ["Permisos explícitos (--allow-net, --allow-read…)", "Ejecuta todo como root", "Bloquea la red para siempre", "Solo permite HTTPS"],
             0, "Sin --allow-* el código no puede salir de su caja de arena: ideal para scripts de terceros."),
        ]),
        ('''2. Bun en la práctica''', '''
Flujo diario con Bun:
    bun init                 → proyecto nuevo (index.ts listo)
    bun run index.ts         → ejecuta TS directamente
    bun add express          → instala rapidísimo (bun.lock)
    bun run dev              → corre scripts del package.json
    bun test                 → tests integrados API tipo Jest
                              (import { test, expect } from "bun:test")

Ejecuta TypeScript y JSX SIN configurar transpiladores: escribes .ts y
corre. También trae watch mode (--watch) y hot reload.

Servidor HTTP nativo sin frameworks, rapidísimo:
    Bun.serve({
      port: 3000,
      fetch(req) {
        return new Response("Hola desde Bun");
      },
    });
    console.log("http://localhost:3000");

APIs modernas de Web (fetch, Response, Request) son ciudadanos de
primera clase; muchas APIs de Node (fs, path, process) también funcionan.''', [
            ("¿Qué comando ejecuta los tests integrados de Bun?",
             ["bun test", "npm test", "bun check", "deno test"],
             0, "bun test incluye runner con API estilo Jest (describe/test/expect), sin instalar nada."),
            ("¿Cómo levanta Bun un servidor HTTP sin Express?",
             ["Con Bun.serve({ fetch })", "Con http.createServer solamente", "Con nginx", "No puede"],
             0, "Bun.serve es el servidor nativo de alto rendimiento con handlers fetch estándar Web."),
        ]),
        ('''3. Deno en la práctica''', '''
Seguridad primero: un script no tiene permisos hasta que los pides:
    deno run --allow-net --allow-read server.ts
Si el código intenta usar red sin --allow-net → PermissionDenied, y tú
decides. --allow-read=./datos limita incluso el directorio.

TypeScript nativo:
    // hola.ts — se ejecuta tal cual, sin tsc ni build
    const saludar = (n: string): string => `Hola ${n}`;
    console.log(saludar("Deno"));

Imports modernos: URLs, npm:, jsr: (registro de Deno) y deno.json para
mapear imports y tareas ("tasks": { "dev": "deno run --watch main.ts" }).

HTTP estándar:
    Deno.serve({ port: 8000 }, (_req) => new Response("Hola Deno"));

Herramientas de serie (cero configuración): deno fmt (formatea),
deno lint (analiza), deno test (tests), deno compile (un binario
ejecutable de tu app). Menos node_modules, más estándares Web.''', [
            ("¿Qué pasa si un script de Deno usa la red sin --allow-net?",
             ["Deno lanza PermissionDenied y bloquea la operación", "Funciona igual", "Lo reporta por email", "Se reinicia el PC"],
             0, "El sandbox de Deno exige permisos explícitos por recurso: seguridad real por defecto."),
            ("¿Qué herramientas trae Deno integradas sin configuración?",
             ["fmt, lint y test (además de compile)", "Solo el runtime", "Photoshop", "Docker"],
             0, "deno fmt, deno lint, deno test y deno compile vienen de serie: toolchain todo-en-uno."),
        ]),
        ('''4. Frameworks modernos y despliegue edge''', '''
El ecosistema moderno sobre estos runtimes:
  · FRESH (Deno): framework web de ISLAS como Astro, sin paso de build;
    escribes .tsx y despliegas al instante.
  · ELYSIA (Bun): estilo Express pero con tipos end-to-end y una
    velocidad asombrosa aprovechando Bun.
  · HONO: ultraligero y MULTI-RUNTIME: el mismo código corre en Deno,
    Bun, Node y workers del edge (Cloudflare, Vercel) — escribe una vez.

Despliegue moderno:
  · Deno Deploy: git push → tu app en el edge global en segundos, con
    KV/queues/cron integrados y TLS gratis.
  · Bun: Fly.io, Railway o tu VPS (arranque en frío casi instantáneo).

En serverless/edge el ARRANQUE EN FRÍO manda: Bun y Deno inician en
milisegundos frente a cientos de ms de un Node cargado de dependencias.
Por eso dominan en APIs pequeñas, webhooks y middlewares del edge.''', [
            ("¿Qué framework corre el MISMO código en Deno, Bun, Node y workers del edge?",
             ["Hono", "Rails", "Django", "Laravel"],
             0, "Hono es ultraligero y multi-runtime: una API escrita una vez despliega en todos los runtimes."),
            ("¿Qué es Fresh?",
             ["El framework de islas para Deno, sin paso de build", "Un gestor de paquetes", "Un bundler", "Una base de datos"],
             0, "Fresh aplica arquitectura de islas (como Astro) sobre Deno con Preact: cero build, súper rápido."),
        ]),
    ],
}
