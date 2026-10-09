// =====================================================================
//  EL GATO · juego.js
//  Escudería GEIIA · sesión 19
//
//  El tablero responde al clic: alterna X y O, y no deja escribir
//  encima de una casilla ocupada.
//
//  Lo que todavía NO hace: detectar al ganador. Eso es la tarea.
// =====================================================================


// ---------------------------------------------------------------------
//  1 · Agarrar los elementos de la página
// ---------------------------------------------------------------------
const casillas   = document.querySelectorAll(".casilla");
const turnoTexto = document.querySelector("#turno");
const boton      = document.querySelector(".reiniciar");


// ---------------------------------------------------------------------
//  2 · El estado, en variables
// ---------------------------------------------------------------------
// IMPORTANTE: hay DOS tableros.
//
//   - este arreglo, que es LA VERDAD
//   - lo que se ve en la pantalla, que es UN REFLEJO
//
// Siempre se cambia primero el arreglo y luego se refleja.
// Si los dos se separan, el juego miente.

let tablero  = [" ", " ", " ", " ", " ", " ", " ", " ", " "];
let turnoDeX = true;


// ---------------------------------------------------------------------
//  3 · Qué pasa al picar una casilla
// ---------------------------------------------------------------------
casillas.forEach((casilla, indice) => {
    casilla.addEventListener("click", () => {

        // Si ya está ocupada, no hay nada que hacer.
        // Se revisa el ARREGLO, no la pantalla.
        if (tablero[indice] !== " ") {
            return;
        }

        // De quién es el turno. El ternario es el mismo de Python,
        // con otra forma: condición ? valor_si : valor_no
        const marca = turnoDeX ? "X" : "O";

        // 1 · se cambia el arreglo
        tablero[indice] = marca;

        // 2 · se refleja en la pantalla
        casilla.textContent = marca;

        // 3 · cambia el turno
        turnoDeX = !turnoDeX;
        turnoTexto.textContent = turnoDeX ? "Turno de X" : "Turno de O";
    });
});


// ---------------------------------------------------------------------
//  4 · El botón de reiniciar
// ---------------------------------------------------------------------
// Vacía el arreglo Y la pantalla. Si solo vacías una de las dos,
// se nota: el tablero se ve limpio pero no deja volver a jugar
// en las mismas casillas. Ese error demuestra que hay dos tableros.

boton.addEventListener("click", () => {
    tablero  = [" ", " ", " ", " ", " ", " ", " ", " ", " "];
    turnoDeX = true;

    casillas.forEach((casilla) => {
        casilla.textContent = "";
    });

    turnoTexto.textContent = "Turno de X";
});


// =====================================================================
//  TAREA · portar hayGanador del gato de Python
// =====================================================================
//  Las ocho formas de ganar, como posiciones del tablero:
//
//  const COMBINACIONES = [
//      [0, 1, 2], [3, 4, 5], [6, 7, 8],   // filas
//      [0, 3, 6], [1, 4, 7], [2, 5, 8],   // columnas
//      [0, 4, 8], [2, 4, 6],              // diagonales
//  ];
//
//  function hayGanador(tablero) {
//      // recorre las combinaciones y devuelve "X", "O" o null
//  }
//
//  Para comprobarlo, sin tocar la página:
//
//  console.log(hayGanador(["X","X","X"," "," "," "," "," "," "]));  // "X"
//  console.log(hayGanador(["O"," "," "," ","O"," "," "," ","O"]));  // "O"
//  console.log(hayGanador([" "," "," "," "," "," "," "," "," "]));  // null
//
//  Ojo: la condición tiene que revisar primero que la casilla
//  no esté vacía. Si no, tres casillas en blanco "ganan".
// =====================================================================

