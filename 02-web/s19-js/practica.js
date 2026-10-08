document.querySelector("h1")
document.querySelector("h1").textContent

//podemos editar el html desde el javascript
document.querySelector("h1").textContent = "Hola";
 

// uno solo - el primero que encuentre
const turno = document.querySelector("#turno");

// TODOS - una lista
const casillas = document.querySelectorAll(".casilla");

console.log(casillas.length);


//ESCUCHAR
const boton = 
    document.querySelector(".reiniciar");

boton.addEventListener("click", function () {
    console.log("me picaron")
});

casillas.forEach(function (casilla, indice) {
    casilla.addEventListener("click", function () {
        console.log("picaron la: ", indice + 1);
    })
})

