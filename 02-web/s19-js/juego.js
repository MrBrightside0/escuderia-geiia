//const COMBINACIONES = [
//    [0,1,2],[3,4,5],[6,7,8],
//    [0,3,6],[1,4,7],[2,5,8],
//    [0,4,8],[2,4,6]
//]
//
////investigar sintaxis de javascript
////tarea portar dos funciones mas de su gato: tableLleno 
////Crear tablero
//
//
//function hayGanador(tablero) { 
//    //esto les toca ustedes
//}
//
//console.log(hayGanador(["X","X","X","","","","","",""]))

// 1 agarrar los elementos de la pagina
const casillas =
    document.querySelectorAll(".casilla");
const turnoTexto = 
    document.querySelector("#turno");

// 2 el estado en variables 
let tablero = [" "," "," "," "," "," "," "," "," "];
let turnoDex = true;

// 3 que pasa al picar
casillas.forEach(function (casilla,indice ) {
    casilla.addEventListener("click", function () {
        
        if (tablero[indice] != " ")
        {
            return; //ya esta ocupado
        }

    const marca = turnoDex ? "X" : "O";
    tablero[indice] = marca;
    casilla.textContent = marca;

    turnoDex = !turnoDex;
    turnoTexto.textContent = 
        turnoDex ? "Turno de X" : "Turno de O";
    });
});

//boton de reiniciar

const boton = 
    document.querySelector(".reiniciar");

boton.addEventListener("click", function () {
    tablero = [" "," "," "," "," "," "," "," "," "];
    turnoDex = true;

    casillas.forEach(function (casilla) { 
        casilla.textContent = "";
     });

    turnoTexto.textContent = "Turno De X";
});