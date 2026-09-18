# ⚡ Cheatsheet — 5. MVC en Laravel: flujo completo de una petición

> PHP y Laravel — El Backend Que Alimenta la Web · Lección 5 · 18/09/2026

## 💡 Idea central
DE URL A RESPUESTA: EL CAMINO LARAVEL

## 🧠 Autoexamen (tápate la respuesta)
- **¿Qué hace Route Model Binding en Laravel?** → Inyecta directo el modelo por ID (404 automático si no existe) sin hacer find manual _(function show(Tarea $tarea) — el framework busca el id y te da el modelo o 404.)_
- **¿Para qué sirve \$fillable en el modelo?** → Anti mass-assignment: lista blanca de campos rellenables vía create/update (evita inyectar campos no previstos) _(Tarea::create($request->all()) protegido: solo pasa lo autorizado.)_

## 🔁 Repaso espaciado sugerido
Hoy → mañana → dentro de 3 días → dentro de una semana. 5 minutos bastan.
