// mainCRUD.js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('form');

    form.addEventListener('submit', function (event) {
        const nombrePokemonInput = document.getElementById('nombre_pokemon');
        const regionInput = document.getElementById('region');
        const tipoInput = document.getElementById('tipo');

        const errors = [];

        if (!nombrePokemonInput.value) {
            errors.push('Por favor, ingrese el nombre del Pokemon.');
        }

        if (!regionInput.value) {
            errors.push('Por favor, ingrese la región del Pokemon.');
        }

        if (tipoInput.value === '0') {
            errors.push('Por favor, seleccione el tipo del Pokemon.');
        }

        if (errors.length > 0) {
            alert(errors.join('\n'));
            event.preventDefault();
            return;
        }

        const confirmacion = confirm('¿Estás seguro de enviar el formulario?');
        if (!confirmacion) {
            event.preventDefault();
        }
    });

    // Validación en tiempo real
    form.addEventListener('input', function (event) {
        const input = event.target;

        if (input.required && !input.value) {
            input.classList.add('is-invalid');
        } else {
            input.classList.remove('is-invalid');
        }
    });

    // Efecto visual en la lista de Pokemones
    const tableRows = document.querySelectorAll('.table tbody tr');

    tableRows.forEach(row => {
        row.addEventListener('mouseover', function () {
            row.classList.add('table-hover');
        });

        row.addEventListener('mouseout', function () {
            row.classList.remove('table-hover');
        });
    });
});
