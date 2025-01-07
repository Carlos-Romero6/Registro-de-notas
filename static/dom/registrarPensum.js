// Agregar Pensum
document.getElementById('agregarPensum').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch(`/pensum-matricula/agregar/`, {
        method: 'POST',
        body: formData
        })
        .then(response => response.json())
        .then(data => {
        if (data.success) {
            alert("Se ha agregado correctamente.");
            const modal = new bootstrap.Modal(document.getElementById('modalAgregarPensum'));
            modal.hide();
            window.location.reload();
        } else {
            alert("Error al cargar Pensum.");
        } 
        })
        .catch(error => {
        console.error('Error: ', error);
        alert("Ocurrió un error inesperado.");
        });
    });