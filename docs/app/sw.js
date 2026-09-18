/* PWA offline: precache de la shell + cursos GRATIS; el resto cache-first dinámico */
const CACHE = 'pt-web-v1';
const PRE = ["./", "./index.html", "./app.js", "./data/indice.json", "./icon-192.png", "./icon-512.png", "./data/cursos/01-ruta-maestra-como-usar-esta-plataforma.json", "./data/cursos/02-herramientas-del-desarrollador.json", "./data/cursos/03-html-y-css-diseno-web-total.json", "./data/cursos/04-javascript-de-cero-a-experto.json", "./data/cursos/05-typescript-javascript-con-superpoderes-y.json", "./data/cursos/06-react-interfaces-modernas-y-reutilizable.json", "./data/cursos/07-node-js-javascript-en-el-servidor.json", "./data/cursos/08-python-de-cero-a-profesional.json", "./data/cursos/09-sql-y-bases-de-datos-datos-que-persisten.json", "./data/cursos/10-git-y-github-tu-historia-nunca-se-pierde.json", "./data/cursos/11-docker-en-mi-maquina-si-funciona-resuelt.json", "./data/cursos/12-linux-y-terminal-el-superpoder-del-dev.json", "./data/cursos/13-devops-y-ci-cd-de-tu-pc-a-produccion-sin.json", "./data/cursos/14-despliegue-y-servidores-tu-app-al-mundo.json", "./data/cursos/15-php-y-laravel-el-backend-que-alimenta-la.json"];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRE)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(r => {
    if (r.ok && new URL(e.request.url).origin === location.origin) {
      const cl = r.clone(); caches.open(CACHE).then(c => c.put(e.request, cl));
    }
    return r;
  }).catch(() => hit)));
});
