// =====================================================================
//  EL GATO · juego.js
//  Escudería GEIIA · sesiones 19 y 20
//
//  19 · el tablero responde al clic
//  20 · detecta al ganador y recuerda el historial
//
//  ESTE ES EL ARCHIVO DE REFERENCIA. Si te atoras, compara el tuyo
//  con este, pero intenta escribirlo tú primero.
// =====================================================================


// ---------------------------------------------------------------------
//  1 · Agarrar los elementos de la página
// ---------------------------------------------------------------------
const casillas   = document.querySelectorAll(".casilla");
const turnoTexto = document.querySelector("#turno");
const boton      = document.querySelector(".reiniciar");
const marcador   = document.querySelector("#marcador");


// ---------------------------------------------------------------------
//  2 · El estado
// ---------------------------------------------------------------------
// Hay DOS tableros: este arreglo es LA VERDAD, la pantalla es
// UN REFLEJO. Siempre se cambia primero el arreglo.

let tablero   = [" ", " ", " ", " ", " ", " ", " ", " ", " "];
let turnoDeX  = true;
let terminada = false;   // sin esto se podría jugar después de ganar

// Las ocho formas de ganar. No cambia nunca: por eso va arriba y const.
const COMBINACIONES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],   // filas
    [0, 3, 6], [1, 4, 7], [2, 5, 8],   // columnas
    [0, 4, 8], [2, 4, 6],              // diagonales
];


// ---------------------------------------------------------------------
//  3 · Lógica pura · portada del gato de Python
// ---------------------------------------------------------------------

/** Devuelve "X", "O" o null si todavía no hay ganador. */
const hayGanador = (tablero) => {
    for (const combo of COMBINACIONES) {
        const [a, b, c] = combo;        // desestructurar la combinación

        if (tablero[a] !== " " &&       // sin esto, tres vacías "ganan"
            tablero[a] === tablero[b] &&
            tablero[b] === tablero[c]) {
            return tablero[a];
        }
    }
    return null;
};

/** Dice si ya no quedan casillas libres. */
const tableroLleno = (t) => !t.includes(" ");


// ---------------------------------------------------------------------
//  4 · El historial · localStorage + JSON
// ---------------------------------------------------------------------
// localStorage SOLO guarda texto, igual que un archivo. Por eso todo
// pasa por JSON.stringify al guardar y JSON.parse al leer.

const cargarHistorial = () => {
    const guardado = localStorage.getItem("historial");
    if (guardado === null) {
        return [];              // primera vez: todavía no hay nada
    }
    return JSON.parse(guardado);
};

const guardarHistorial = (historial) => {
    localStorage.setItem("historial", JSON.stringify(historial));
};

const registrarPartida = (ganador) => {
    const historial = cargarHistorial();   // 1 · cargar
    historial.push({ ganador: ganador });  // 2 · agregar
    guardarHistorial(historial);           // 3 · guardar
};

/** Cuenta las victorias con filter y las escribe en la página. */
const mostrarMarcador = () => {
    const historial = cargarHistorial();

    if (historial.length === 0) {
        marcador.textContent = "Sin partidas todavía";
        return;
    }

    const ganoX   = historial.filter(p => p.ganador === "X").length;
    const ganoO   = historial.filter(p => p.ganador === "O").length;
    const empates = historial.filter(p => p.ganador === "empate").length;

    marcador.textContent =
        `${historial.length} partidas · X: ${ganoX} · O: ${ganoO} · empates: ${empates}`;
};


// ---------------------------------------------------------------------
//  5 · Qué pasa al picar una casilla
// ---------------------------------------------------------------------
casillas.forEach((casilla, indice) => {
    casilla.addEventListener("click", () => {

        // dos razones para no hacer nada, en orden
        if (terminada)               return;   // la partida ya acabó
        if (tablero[indice] !== " ") return;   // casilla ocupada

        // 1 · se cambia el arreglo (la verdad)
        const marca = turnoDeX ? "X" : "O";
        tablero[indice] = marca;

        // 2 · se refleja en la pantalla
        casilla.textContent = marca;
        casilla.classList.add("ocupada");

        // 3 · ¿se acabó la partida?
        const ganador = hayGanador(tablero);

        if (ganador !== null) {
            turnoTexto.textContent = `¡Ganó ${ganador}!`;
            terminada = true;
            registrarPartida(ganador);
            mostrarMarcador();
            return;
        }

        if (tableroLleno(tablero)) {
            turnoTexto.textContent = "Empate";
            terminada = true;
            registrarPartida("empate");
            mostrarMarcador();
            return;
        }

        // 4 · si sigue el juego, cambia el turno
        turnoDeX = !turnoDeX;
        turnoTexto.textContent = turnoDeX ? "Turno de X" : "Turno de O";
    });
});


// ---------------------------------------------------------------------
//  6 · El botón de reiniciar
// ---------------------------------------------------------------------
// Vacía el arreglo Y la pantalla. Si solo vacías una de las dos,
// el juego miente. Ojo con terminada: sin regresarla a false,
// el tablero se limpia pero no deja volver a jugar.

boton.addEventListener("click", () => {
    tablero   = [" ", " ", " ", " ", " ", " ", " ", " ", " "];
    turnoDeX  = true;
    terminada = false;

    casillas.forEach((casilla) => {
        casilla.textContent = "";
        casilla.classList.remove("ocupada");
    });

    turnoTexto.textContent = "Turno de X";
});


// ---------------------------------------------------------------------
//  7 · Al abrir la página
// ---------------------------------------------------------------------
// Esta línea es la que demuestra que el historial se guardó:
// muestra el conteo antes de que juegues nada.
mostrarMarcador();