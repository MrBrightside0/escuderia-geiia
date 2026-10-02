# Escudería GEIIA · Temporada 2026

Aquí vive todo lo que construimos. **Si algo no está en este repo, no existe.**

## Cómo está organizado

Las carpetas van en orden y los archivos llevan el número de la sesión en la que
se vieron, para que siempre se pueda volver atrás.

    00-arranque/      sesiones 1 a 3 · git, la terminal y el primer programa
    01-python/        sesiones 4 a 13 · Python, de tipos de datos a validación
    02-web/           sesión 16 en adelante · HTML, CSS y lo que viene
    ejercicios/       los encargos de cada sesión
    pilotos/          una carpeta por piloto, para tus cosas

## Mapa de sesiones

| Sesión | Tema | Dónde está |
|---|---|---|
| 1–3 | Git, terminal y primer programa | `00-arranque/` |
| 4 | Tipos de datos, operaciones, input | `s04-*` |
| 5 | Comparadores y condicionales | `s05-*` |
| 6 | Listas y bucles `for` | `s06-listas-y-for.py` |
| 7 | Acumuladores y `while` | `s07-*` |
| 8 | Funciones | `s08-funciones.py` |
| 9 | Alcance y varios archivos | `s09-*` |
| 10 | Leer y escribir archivos | `s10-archivos.py` |
| 11 | Diccionarios | `s11-diccionarios.py` |
| 12 | `split`, `join` y JSON | `s12-*` |
| 13 | Errores y validación | `s13-errores-y-validacion.py` |
| 14–15 | Proyecto de cierre: el gato | entrega en tu rama |
| 16 | HTML | `02-web/s16-html/` |
| 17 | CSS | `02-web/s17-css/` |

## Ritmo de la semana

| Día | Qué pasa |
|---|---|
| Miércoles | Se enseña. Una idea nueva, tú al frente de tu máquina. |
| Jueves | Se practica. Ejercicio en parejas. |
| Viernes | Se muestra. Demo de 90 segundos, sin notas. |

## Reglas de la casa

1. **Nadie transcribe código.** La hora se gasta en decidir qué va en el hueco y por qué.
2. **La IA se usa para preguntar y entender, no para escribir lo que entregamos.**
   Si no lo puedes leer, todavía no es tuyo.
3. **El que acaba primero ayuda al de al lado.** La ronda se acaba cuando acaban los cinco.
4. **Si no entiendes un error, no lo borres: léelo en voz alta.** El error dice qué pasó.

## Cómo se trabaja en el repo

Cada quien en su rama, nunca directo en `main`:

    git switch main
    git pull
    git switch -c tu-rama
    # ... trabajas ...
    git add .
    git commit -m "lo que hiciste"
    git push -u origin tu-rama

Después se abre el pull request en GitHub.

## Qué NO se sube

Lo que genera el programa al correr: `tareas.json`, `historial.json`, `*.txt`
de prueba y las carpetas `__pycache__`. Ya está en el `.gitignore`.

## Cuando te atores

En este orden:

1. Léelo otra vez, despacio. La mitad de los errores se resuelven aquí.
2. Pregúntale al de al lado.
3. Pregúntale al grupo en el chat, pegando **el error completo**, no "no me funciona".
4. Pregúntale a una IA qué significa el error. No que te lo arregle.
