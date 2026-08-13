# Miércoles · El garaje

**Meta de hoy:** que los cinco entornos corran y que rompamos el repo una vez,
a propósito, para ver que no pasa nada.

---

## 1 · Semáforo de entorno · 8 min

Corre estos tres comandos y escribe tu nombre en el pizarrón:

    python --version
    git --version
    git clone <url-del-repo>

- **Verde** si los tres contestaron.
- **Amarillo** si alguno falló pero ya lo estás resolviendo.
- **Rojo** si nada.

Los verdes se sientan con los rojos. Nadie resuelve esto solo.

---

## 2 · El conflicto de la parrilla · 32 min

### Reglas

1. Abre `parrilla.md`. Tiene cinco renglones numerados.
2. Escribe tu nombre y la capa que te late **en el renglón P1**. Todos en el mismo.
3. Crea tu rama, guarda y súbela:

       git switch -c piloto/tu-nombre
       git add parrilla.md
       git commit -m "alta de piloto"
       git push -u origin piloto/tu-nombre

4. Abre tu pull request en GitHub.
5. Cuando el segundo pull request no se pueda mergear, **todos sueltan el teclado.**
   Eso se llama conflicto y lo vamos a resolver juntos en la pantalla grande.

### La regla de oro al resolver

**No se borra el nombre de nadie.** El conflicto se arregla conservando los dos.

---

## 3 · Lectura de telemetría · 10 min

Con `git log --oneline` en pantalla, contesta:

- ¿Quién subió el primer commit?
- ¿En qué orden entraron los cinco?
- ¿Cuál fue el commit donde se resolvió el conflicto?
- ¿En qué se ve distinto un merge de un commit normal?

---

## Antes de irte

- [ ] Los cinco nombres están en `parrilla.md`, en la rama `main`.
- [ ] Abriste tu pull request con tus propias manos.
- [ ] Sabes en qué rama estás (`git status`).
