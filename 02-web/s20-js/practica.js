// =====================================================================
//  SESIÓN 20 · PRÁCTICA
//
//  §5  Formas de declarar una función      [visto en clase]
//  §6  map y filter                        [visto en clase]
//  §7  localStorage                        [ESTÚDIALO TÚ]
//
//  Cómo correrlo: en index.html, comenta <script src="juego.js">
//  y descomenta <script src="practica.js">. Abre con Live Server
//  y mira la consola: F12 → Console.
// =====================================================================


// =====================================================================
//  §5 · DISTINTAS FORMAS DE DECLARAR UNA FUNCIÓN
// =====================================================================
// Las cuatro hacen EXACTAMENTE lo mismo. No es una función nueva:
// es la misma, escrita más corto.

// la de siempre
function sumarVieja(a, b) { return a + b; }

// flecha con llaves: el return SÍ se escribe
const sumarLarga = (a, b) => { return a + b; };

// flecha corta: una línea, el return es invisible
// A partir de ahora, y en todo React, va a ser así.
const sumar = (a, b) => a + b;

// un solo parámetro: los paréntesis sobran
const doble = n => n * 2;

console.log(sumarVieja(2, 3), sumarLarga(2, 3), sumar(2, 3), doble(5));

// EL ERROR MÁS COMÚN:
//     const malo = (a, b) => { a + b; };
// Pusiste llaves y olvidaste el return → devuelve undefined.


// =====================================================================
//  §6 · MAP y FILTER · bucles sin escribir el bucle
// =====================================================================

const historial = [
    { ganador: "X",      jugadas: 5 },
    { ganador: "empate", jugadas: 9 },
    { ganador: "X",      jugadas: 6 },
    { ganador: "O",      jugadas: 7 },
];
// OJO: las jugadas van SIN comillas. Son números, no texto.
// Con comillas, jugadas + 1 daría "51" en vez de 6.

// MAP · "dame una lista nueva con una cosa por cada una"
console.log(historial.map(p => p.ganador));
// ["X", "empate", "X", "O"]

// FILTER · "dame una lista nueva solo con los que cumplan"
console.log(historial.filter(p => p.ganador === "X").length);   // 2

// Lo mismo que el filter, con el for que ya sabíamos:
const deX = [];
for (const p of historial) {
    if (p.ganador === "X") {
        deX.push(p);
    }
}
console.log(deX.length);   // 2 · seis líneas contra una

// IMPORTANTE: las dos devuelven una lista NUEVA.
// La original no se toca.
console.log(historial.length);   // sigue siendo 4


// =====================================================================
//  §7 · localStorage   ·   NO LO VIMOS EN CLASE
// ---------------------------------------------------------------------
//  Esto es lo que le falta al gato para recordar.
//  Lee despacio y prueba CADA línea en la consola antes de seguir.
// =====================================================================


// ---------------------------------------------------------------------
//  7.1 · Qué es
// ---------------------------------------------------------------------
// Un cajón que el navegador le da a cada página.
// Lo importante: SOBREVIVE a recargar y a cerrar el navegador.
// Es por sitio, así que ninguna otra página puede verlo.

localStorage.setItem("nombre", "Ana");        // escribir
console.log(localStorage.getItem("nombre"));  // leer → "Ana"

// AHORA RECARGA LA PÁGINA y vuelve a pedirlo en la consola:
//     localStorage.getItem("nombre")
// Sigue ahí. Eso no pasaba con una variable normal: una variable
// se borra en cuanto la página se recarga.

// Cuando la llave no existe devuelve null. NO truena.
console.log(localStorage.getItem("no_existe"));   // null

// Para borrar una sola:     localStorage.removeItem("nombre")
// Para borrar todo:         localStorage.clear()
// Para VERLO en una tabla:  F12 → Application → Local Storage


// ---------------------------------------------------------------------
//  7.2 · LA TRAMPA · solo guarda TEXTO
// ---------------------------------------------------------------------
// Esto ya nos pasó en octubre, cuando guardábamos las tareas en un
// .txt separadas por punto y coma. Es el mismo problema.

localStorage.setItem("n", 42);
console.log(localStorage.getItem("n"));           // "42"
console.log(typeof localStorage.getItem("n"));    // "string" ← era número

// Y con un objeto es peor:
localStorage.setItem("malo", { ganador: "X" });
console.log(localStorage.getItem("malo"));        // "[object Object]"

// El objeto se DESTRUYÓ. No quedó ni el nombre de la llave.
// No hay forma de recuperarlo: hay que borrar y guardar bien.


// ---------------------------------------------------------------------
//  7.3 · La solución · la misma de Python
// ---------------------------------------------------------------------
//     json.dump   →   JSON.stringify    (de objeto a texto)
//     json.load   →   JSON.parse        (de texto a objeto)

const partidas = [{ ganador: "X", jugadas: 5 }];

// GUARDAR: primero convertir a texto
localStorage.setItem("prueba", JSON.stringify(partidas));

// mira cómo quedó guardado: es texto, pero texto con forma de JSON
console.log(localStorage.getItem("prueba"));
// '[{"ganador":"X","jugadas":5}]'

// LEER: primero traer el texto, luego convertirlo de vuelta
const devuelto = JSON.parse(localStorage.getItem("prueba"));

console.log(devuelto[0].ganador);          // "X"
console.log(typeof devuelto[0].jugadas);   // "number" ← volvió entero

// REGLA SIN EXCEPCIÓN:
//   todo lo que ENTRA a localStorage pasa por JSON.stringify
//   todo lo que SALE pasa por JSON.parse
// Aunque parezca que no hace falta.


// ---------------------------------------------------------------------
//  7.4 · El patrón completo · esto es lo que vas a usar en la tarea
// ---------------------------------------------------------------------
// Son las mismas cargar() y guardar() del gato de Python,
// con localStorage en lugar de open().

/**
 * Lee el historial guardado.
 * Si todavía no existe, devuelve una lista vacía en vez de null.
 */
const cargarHistorial = () => {
    const guardado = localStorage.getItem("historial");

    if (guardado === null) {
        return [];          // primera vez que se abre: no hay nada
    }

    return JSON.parse(guardado);
};

/** Escribe el historial completo. */
const guardarHistorial = (historial) => {
    localStorage.setItem("historial", JSON.stringify(historial));
};

// Pruébalas:
console.log(cargarHistorial());        // [] la primera vez

guardarHistorial([{ ganador: "X" }, { ganador: "O" }]);
console.log(cargarHistorial());        // dos partidas
console.log(cargarHistorial().length); // 2

// Y recarga la página: siguen ahí.


// ---------------------------------------------------------------------
//  7.5 · Por qué el if de "si es null"
// ---------------------------------------------------------------------
// Sin ese if, cargarHistorial devolvería null la primera vez.
// Y entonces esto truena:
//
//     const h = cargarHistorial();   // null
//     h.push({ ganador: "X" });      // TypeError: h.push is not a function
//
// Es el mismo caso del FileNotFoundError de la sesión 10:
// "todavía no existe" es una situación normal, no un error.
// Se atiende, no se ignora.