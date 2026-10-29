let task = [];
let tareas = [];
let hecho = [];
let chequeo = [];
let filtro = "todas";

const lista = document.getElementById("lista-tareas");
const formulario = document.getElementById("formulario-tarea");
const entrada = document.getElementById("nueva-tarea");
const mensaje = document.getElementById("mensaje");

// Separa los nombres de las tareas y su estado, como en funciones.py.
function separacion(tareas, hecho, task) {
    tareas.length = 0;
    hecho.length = 0;

    for (let i = 0; i < task.length; i++) {
        tareas.push(task[i].trabajo);
        hecho.push(Number(task[i].hecha));
    }

    return [tareas, hecho];
}

// Junta las tareas y su estado para guardarlos en el archivo JSON.
function juntar(task, tareas, hecho) {
    task = [];

    for (let i = 0; i < tareas.length; i++) {
        task.push({
            trabajo: tareas[i],
            hecha: hecho[i]
        });
    }

    return task;
}

// Crea el formato de diccionario que usa tareas.json.
function formato(chequeo, tareas, hecho) {
    chequeo = [];

    for (let i = 0; i < tareas.length; i++) {
        chequeo.push({
            trabajo: tareas[i],
            hecha: hecho[i]
        });
    }

    return chequeo;
}

// Imprime las tareas en la página.
function impresora(chequeo) {
    const tareasVisibles = [];

    for (let i = 0; i < chequeo.length; i++) {
        const estaHecha = Number(chequeo[i].hecha) === 1;

        if (filtro === "hechas" && !estaHecha) {
            continue;
        }
        if (filtro === "pendientes" && estaHecha) {
            continue;
        }

        const elemento = document.createElement("li");
        const casilla = document.createElement("input");
        const nombre = document.createElement("span");
        const botonQuitar = document.createElement("button");

        elemento.className = estaHecha ? "hecha" : "";
        casilla.type = "checkbox";
        casilla.checked = estaHecha;
        casilla.setAttribute("aria-label", "Marcar tarea como terminada");
        casilla.addEventListener("change", function () {
            marcar_tarea(i);
        });

        nombre.className = "nombre-tarea";
        nombre.textContent = chequeo[i].trabajo;

        botonQuitar.type = "button";
        botonQuitar.className = "boton-quitar";
        botonQuitar.textContent = "Quitar";
        botonQuitar.addEventListener("click", function () {
            quitar_tarea(i);
        });

        elemento.append(casilla, nombre, botonQuitar);
        tareasVisibles.push(elemento);
    }

    lista.replaceChildren(...tareasVisibles);
    document.getElementById("sin-tareas").hidden = tareasVisibles.length > 0;
}

// Cuenta las tareas hechas y las que faltan.
function contador(hecho) {
    let listo = 0;
    let nolisto = 0;

    for (let i = 0; i < hecho.length; i++) {
        if (Number(hecho[i]) === 1) {
            listo++;
        } else if (Number(hecho[i]) === 0) {
            nolisto++;
        }
    }

    document.getElementById("contador-hechas").textContent =
        "Tienes hechas: " + listo + " tareas";
    document.getElementById("contador-pendientes").textContent =
        "Te faltan: " + nolisto + " tareas";
    document.getElementById("cantidad-tareas").textContent =
        "Tu tienes: " + tareas.length + " tarea/s en la lista";
}

// Muestra el mensaje final del programa.
function creditos(tareas) {
    if (tareas.length !== 0) {
        document.getElementById("creditos").textContent =
            "Termina tus tareas no seas flojo";
    } else {
        document.getElementById("creditos").textContent =
            "Bien hecho, puedes ver anime todo lo q quieras :3";
    }
}

// Actualiza la lista y los contadores.
function actualizar_pagina() {
    chequeo = formato(chequeo, tareas, hecho);
    impresora(chequeo);
    contador(hecho);
    creditos(tareas);
}

// Abre tareas.json desde el servidor local.
async function abrir() {
    const respuesta = await fetch("/api/tareas");

    if (!respuesta.ok) {
        throw new Error("No se pudo abrir tareas.json");
    }

    task = await respuesta.json();
    separacion(tareas, hecho, task);
    actualizar_pagina();
}

// Guarda los cambios directamente en tareas.json.
async function guardar() {
    task = juntar(task, tareas, hecho);

    const respuesta = await fetch("/api/tareas", {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(task, null, 4)
    });

    if (!respuesta.ok) {
        throw new Error("No se pudieron guardar las tareas");
    }
}

// Agrega una tarea nueva, evitando repetir una que ya existe.
function failsafet1(_, tareas) {
    const nueva = _.trim();

    if (nueva.length === 0) {
        return "Escribe una tarea";
    }
    if (tareas.includes(nueva)) {
        return "Esta tarea ya existe, pon una que no exista";
    }

    return "";
}

// Comprueba que la tarea exista y que todavía no esté terminada.
function failsafe4(_, hecho, tareas) {
    const indice = tareas.indexOf(_);

    if (indice === -1) {
        return "La tarea no existe";
    }
    if (Number(hecho[indice]) === 1) {
        return "La tarea ya esta marcada como terminada, selecciona otra";
    }

    return "";
}

// Comprueba que la tarea que se quiere quitar exista.
function failsafet5(_, tareas) {
    if (!tareas.includes(_)) {
        return "La tarea no existe";
    }

    return "";
}

// Mantiene el nombre de la función del menú original.
function falesafemenu(_, opciones) {
    if (!opciones.includes(_)) {
        return "Selecciona un numero que este en las opciones";
    }

    return "";
}

// Mantiene la función del menú original para volver a la lista.
function volver_al_menu() {
    entrada.focus();
}

async function agregar_tarea(nombre) {
    const error = failsafet1(nombre, tareas);
    mensaje.textContent = error;

    if (error) {
        return;
    }

    tareas.push(nombre.trim());
    hecho.push(0);
    await guardar_y_actualizar();
    volver_al_menu();
}

async function marcar_tarea(indice) {
    const error = failsafe4(tareas[indice], hecho, tareas);

    if (error) {
        mensaje.textContent = error;
        actualizar_pagina();
        return;
    }

    hecho[indice] = 1;
    await guardar_y_actualizar();
}

async function quitar_tarea(indice) {
    const nombre = tareas[indice];
    const error = failsafet5(nombre, tareas);

    if (error) {
        mensaje.textContent = error;
        return;
    }

    tareas.splice(indice, 1);
    hecho.splice(indice, 1);
    await guardar_y_actualizar();
}

async function guardar_y_actualizar() {
    try {
        await guardar();
        mensaje.textContent = "";
        actualizar_pagina();
    } catch (error) {
        mensaje.textContent = "No se pudieron guardar las tareas en tareas.json";
    }
}

formulario.addEventListener("submit", async function (evento) {
    evento.preventDefault();
    const error = failsafet1(entrada.value, tareas);
    await agregar_tarea(entrada.value);

    if (!error) {
        entrada.value = "";
    }
});

document.getElementById("filtro-todas").addEventListener("click", function () {
    filtro = "todas";
    actualizar_pagina();
});

document.getElementById("filtro-pendientes").addEventListener("click", function () {
    filtro = "pendientes";
    actualizar_pagina();
});

document.getElementById("filtro-hechas").addEventListener("click", function () {
    filtro = "hechas";
    actualizar_pagina();
});

// Inicia el programa leyendo el archivo JSON.
abrir().catch(function () {
    mensaje.textContent = "No se pudo abrir tareas.json. Revisa que exista en esta carpeta.";
});
