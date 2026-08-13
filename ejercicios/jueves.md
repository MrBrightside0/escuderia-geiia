# Jueves · Deshacer

**Meta de hoy:** perderle el miedo a equivocarse. Nada de lo que hagas en git es
irreversible, y hoy lo vas a comprobar tú.

---

## 1 · La terminal sin miedo · 15 min

Cuatro comandos y ya te puedes mover en cualquier máquina:

    pwd            ¿dónde estoy?
    ls             ¿qué hay aquí?
    cd carpeta     entrar
    cd ..          salir

Luego abre `arranque/hola.py`, pon tu nombre, y córrelo:

    python arranque/hola.py

Esa línea que apareció la escribió tu computadora porque tú se lo pediste.
Ya estás programando.

---

## 2 · El sabotaje · 25 min

Alguien mandó un commit a `main` que **borró un nombre de la parrilla**.
El mensaje del commit dice "ajustes". Muy sospechoso.

### Su misión

1. Averiguar **qué commit** lo borró.
2. Averiguar **qué decía** exactamente antes.
3. Deshacerlo **sin borrar historia**.

### Herramientas

    git log --oneline        la lista, lo más nuevo arriba
    git show <id>            qué cambió en ese commit
    git revert <id>          deshacerlo, dejando el rastro

### Pista, si a los 8 minutos siguen atorados

El historial se lee de arriba hacia abajo: arriba lo más reciente.
Lo que buscan pasó **después** de los cinco pull requests de ayer.

### Lo que se aprende hoy

En git nada se pierde. Es una red de seguridad, no un trámite.

---

## 3 · Carrera de deshacer · 10 min

Por parejas, con reloj:

1. El piloto A rompe algo del repo a propósito y hace commit.
2. El piloto B lo encuentra y lo revierte.
3. Cambian de papel.

Gana la pareja que lo haga más rápido **y** pueda decir qué commit revirtió.

---

## Antes de irte

- [ ] El sabotaje está revertido y el historial intacto.
- [ ] Corriste tu `hola.py`.
- [ ] Rompiste y arreglaste algo con tus manos.
- [ ] Traes tu pregunta para mañana: algo que se responda con un número.
