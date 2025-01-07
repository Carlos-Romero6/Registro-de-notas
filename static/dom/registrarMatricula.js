// Agregar Matricula
document.getElementById('agregarMatricula').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch(`/pensum-matricula/agregarmatricula/`, {
        method: 'POST',
        body: formData
        })
        .then(response => response.json())
        .then(data => {
        if (data.success) {
            alert("Se ha agregado correctamente.");
            const modal = new bootstrap.Modal(document.getElementById('modalAgregarMatricula'));
            modal.hide();
            window.location.reload();
        } else {
            alert("Error al cargar Matricula.");
        } 
        })
        .catch(error => {
        console.error('Error: ', error);
        alert("Ocurrió un error inesperado.");
        });
    });