# Hoja de comandos · Semana 1

Imprímela o tenla abierta. No hay que memorizarla.

## Terminal · moverse

| Comando | Qué hace |
|---|---|
| `pwd` | ¿En qué carpeta estoy? |
| `ls` | ¿Qué hay aquí dentro? |
| `cd escuderia-geiia` | Entrar a una carpeta |
| `cd ..` | Salir una carpeta hacia atrás |
| `mkdir pruebas` | Crear una carpeta |
| `python arranque/hola.py` | Correr un archivo de Python |

## Git · trabajar sin pisarse

| Comando | Qué hace |
|---|---|
| `git clone <url>` | Traerte el repo a tu máquina, la primera vez |
| `git switch -c piloto/tu-nombre` | Crear tu rama y moverte a ella |
| `git add parrilla.md` | Marcar qué archivo quieres guardar |
| `git commit -m "alta de piloto"` | Guardar con un mensaje que diga qué hiciste |
| `git push -u origin piloto/tu-nombre` | Subir tu rama a GitHub |
| `git switch main` | Regresar a la rama principal |
| `git pull` | Bajar lo que otros ya subieron |

## Git · mirar y deshacer

| Comando | Qué hace |
|---|---|
| `git log --oneline` | La lista de todo lo que ha pasado, lo más nuevo arriba |
| `git show <id>` | Qué cambió exactamente en ese commit |
| `git revert <id>` | Deshacer ese commit **sin borrar historia** |
| `git status` | ¿En qué rama estoy y qué tengo sin guardar? |

> Si te pierdes: `git status`. Contesta las dos preguntas que importan.
