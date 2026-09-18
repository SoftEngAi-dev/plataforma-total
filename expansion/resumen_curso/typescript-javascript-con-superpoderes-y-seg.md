# 📕 Resumen maestro — TypeScript — JavaScript con Superpoderes y Seguridad

> Todo el curso en una hoja: una idea núcleo por lección. Releer semanal.

## 1. 1. TypeScript en 10 minutos: por qué existe
TS: JS + CHEQUEO DE TIPOS ANTES DE EJECUTAR ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ TypeScript es JavaScript con anotaciones que el compilador verifica ANTES de que corras nada. Detecta 40…

## 2. 2. Tipos básicos y anotaciones
EL VOCABULARIO DE TIPOS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   const nombre: string = "Ada";   const edad: number = 36;   const activa: boolean = true;   const temas: string[] = ["js", …

## 3. 3. Interfaces vs Types: modelar el mundo
MODELAR DATOS CON ESTILO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ INTERFACE — el contrato de forma de un objeto:   interface Usuario {     id: number;     nombre: string;     email?: string…

## 4. 4. Genéricos: reusabilidad con seguridad
GENÉRICOS: <T> = TIPO PARÁMETRO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Sin genérico pierdes tipos o repites código:   function identidad<T>(valor: T): T { return valor; }   identidad("hol…

## 5. 5. Clases en TS: private, readonly e implements
POO SERIA CON VISIBILIDAD ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   class Cuenta {     private saldo: number;          // solo accesible dentro     readonly titular: string;       // no re…

## 6. 6. Narrowing y utilidades: escribir lógica segura
NARROWING: DESECHAR CASOS Y GANAR CERTEZA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ TS VIGILA tu código y afina el tipo dentro de condicionales:    function procesar(x: string | number) {   …

## 7. 7. TS en proyectos reales: configuración y flujo
DE LOS TIPOS A LA PRODUCCIÓN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ SETUP   npm init -y   npm install --save-dev typescript   npx tsc --init      → tsconfig.json  TSCONFIG (los 5 que impo…

---
✅ 7 lecciones · 📝 14 preguntas de repaso en quizzes_html/ · tests/