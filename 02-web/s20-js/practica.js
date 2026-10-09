// =====================================================================
//  SESIÓN 19 · PRÁCTICA
//  El cuaderno de experimentos del DOM.
//  Esto NO es el juego: son pruebas para entender cómo funciona.
//
//  Se corre abriendo index.html con Live Server y mirando
//  la consola del navegador (F12 → Console).
// =====================================================================


// ---------------------------------------------------------------------
//  1 · El navegador convierte el HTML en un objeto
// ---------------------------------------------------------------------
// Ese objeto se llama document y JavaScript lo puede leer Y modificar.
// A eso se le llama el DOM.

//console.log(document.querySelector("h1"));              // el elemento
//console.log(document.querySelector("h1").textContent);  // su texto
//
//// y se puede cambiar desde aquí:
//document.querySelector("h1").textContent = "El gato";

// OJO: esto NO modifica el archivo index.html.
// Solo cambia la copia que el navegador tiene en memoria.
// Al recargar, vuelve a como estaba.


// ---------------------------------------------------------------------
//  2 · Agarrar elementos · los selectores son los mismos de CSS
// ---------------------------------------------------------------------
//   .clase   con punto
//   #id      con gato
//   etiqueta sola
// No hay nada nuevo que aprender: es lo que ya sabían de CSS.

// querySelector devuelve UNO · el primero que encuentre
//const turno = document.querySelector("#turno");
//
//// querySelectorAll devuelve una LISTA
//const casillas = document.querySelectorAll(".casilla");
//
//console.log(casillas.length);   // 9
//console.log(casillas[0]);       // la primera

// Error típico: usar querySelector cuando querías todas.
// Entonces solo funciona la primera casilla.


// ---------------------------------------------------------------------
//  3 · Escuchar · addEventListener
// ---------------------------------------------------------------------
// Se lee: "botón, cuando te hagan clic, corre esto".
//
// Lo nuevo de verdad: esa función NUNCA la llamas tú.
// La escribes, la dejas ahí, y el navegador la ejecuta cuando
// pase el evento. Es el primer código del semestre que no corre
// de arriba abajo: el programa se queda esperando.

//const boton = document.querySelector(".reiniciar");
//
//boton.addEventListener("click", function () {
//    console.log("me picaron");
//});


// ---------------------------------------------------------------------
//  4 · Las nueve casillas, en un solo bloque
// ---------------------------------------------------------------------
// forEach recorre la lista y regala el índice de cada casilla.
// Ese índice es la posición en el arreglo del tablero:
// la casilla 4 de la página es tablero[4]. Ahí se juntan
// la página y la lógica que escribimos en Python.

//casillas.forEach(function (casilla, indice) {
//    casilla.addEventListener("click", function () {
//        console.log("picaron la:", indice);
//    });
//});

// Prueba esto antes de seguir: pica casillas al azar y
// comprueba que sale el número correcto. Si eso no funciona,
// nada de lo que viene va a funcionar.

//Distintas formas de declarar funciones

function sumarVieja(a, b) { return a + b;  }

const sumarLarga = (a,b) => {return a + b;};


//a partir de ahora cuando veamos react sera de esta manera
//flechita simplificada
const sumar = (a,b) => a + b;

const doble = n => n * 2;

//historial
const historial = [
    {ganador:"X", jugadas: "5"},
    {ganador:"empate", jugadas: "9"},
    {ganador:"X", jugadas: "6"},
    {ganador:"O", jugadas: "7"}
]

//lista nueva con una cosa por cada una
historial.map(p => p.ganador)

//filtrar datos 
historial.filter(p => p.ganador === "X")

//desppaye sin filter :(
const deX = []
for (const p of historial) {
    if (p.ganador === "X") {
        deX.push(p);
    }
}