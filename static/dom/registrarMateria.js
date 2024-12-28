// Agregar materia
document.getElementById('agregarMateria').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch(`/pensum-matricula/agregar2/`, {
        method: 'POST',
        body: formData
        })
        .then(response => response.json())
        .then(data => {
        if (data.success) {
            alert("Se ha agregado correctamente.");
            const modal = new bootstrap.Modal(document.getElementById('modalAgregarMateria'));
            modal.hide();
            window.location.reload();
        } else {
            alert("Error al cargar Materia.");
        } 
        })
        .catch(error => {
        console.error('Error: ', error);
        alert("Ocurrió un error inesperado.");
        });
    });