// main.js
document.addEventListener("DOMContentLoaded", function () {
    // Obtén una referencia al título "Pokemones"
    const tituloPokemones = document.querySelector('.titulo h1');

    // Agrega un evento de clic al título
    tituloPokemones.addEventListener('click', function () {
        alert('¡Has hecho clic en el título "Pokemones"!');
    });

    // Obtén una referencia al botón "Ir a CRUD Pokemones"
    const btnIrCrud = document.querySelector('.btn-ir-crud a');

    // Agrega eventos para cambiar el color de fondo cuando se pasa el ratón sobre el botón
    btnIrCrud.addEventListener('mouseover', function () {
        btnIrCrud.style.backgroundColor = 'blue';
    });

    btnIrCrud.addEventListener('mouseout', function () {
        btnIrCrud.style.backgroundColor = ''; // Restaura el color de fondo predeterminado
    });
});
