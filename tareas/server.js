const http = require("http");
const fs = require("fs");
const path = require("path");

const carpeta = __dirname;
const archivoTareas = path.join(carpeta, "tareas.json");
const puerto = 3000;

const tipos = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8"
};

function responder(respuesta, codigo, contenido, tipo) {
    respuesta.writeHead(codigo, {
        "Content-Type": tipo,
        "Access-Control-Allow-Origin": "*"
    });
    respuesta.end(contenido);
}

const servidor = http.createServer(function (peticion, respuesta) {
    if (peticion.method === "GET" && peticion.url === "/api/tareas") {
        fs.readFile(archivoTareas, "utf8", function (error, contenido) {
            if (error) {
                responder(respuesta, 500, "No se pudo abrir tareas.json", "text/plain; charset=utf-8");
                return;
            }

            responder(respuesta, 200, contenido, "application/json; charset=utf-8");
        });
        return;
    }

    if (peticion.method === "PUT" && peticion.url === "/api/tareas") {
        let contenido = "";

        peticion.on("data", function (parte) {
            contenido += parte;
        });

        peticion.on("end", function () {
            try {
                const tareas = JSON.parse(contenido);

                if (!Array.isArray(tareas)) {
                    responder(respuesta, 400, "El contenido debe ser una lista de tareas", "text/plain; charset=utf-8");
                    return;
                }

                fs.writeFile(archivoTareas, JSON.stringify(tareas, null, 4) + "\n", "utf8", function (error) {
                    if (error) {
                        responder(respuesta, 500, "No se pudo guardar tareas.json", "text/plain; charset=utf-8");
                        return;
                    }

                    responder(respuesta, 200, "Tareas guardadas", "text/plain; charset=utf-8");
                });
            } catch (error) {
                responder(respuesta, 400, "El JSON enviado no es valido", "text/plain; charset=utf-8");
            }
        });
        return;
    }

    const rutaPedida = peticion.url === "/" ? "/index.html" : peticion.url;
    const nombreArchivo = path.basename(rutaPedida);
    const rutaArchivo = path.join(carpeta, nombreArchivo);

    fs.readFile(rutaArchivo, function (error, contenido) {
        if (error) {
            responder(respuesta, 404, "No se encontro el archivo", "text/plain; charset=utf-8");
            return;
        }

        const tipo = tipos[path.extname(nombreArchivo)] || "application/octet-stream";
        responder(respuesta, 200, contenido, tipo);
    });
});

servidor.listen(puerto, function () {
    console.log("Abre http://localhost:" + puerto + " en tu navegador");
    console.log("Las tareas se guardan en: " + archivoTareas);
});
