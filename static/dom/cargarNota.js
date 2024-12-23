// Cargar notas

document.getElementById('cargarNota').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch(`/notas/cargar-nota/`, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
        alert("Se ha cargado correctamente.");
        $('#modalCargarNota').modal('hide');
        window.location.reload();
        } else {
        alert("Error al cargar nota.");
        }
    })
    .catch(error => {
        console.error('Error: ', error);
        alert("Ocurrió un error inesperado.");
    });

})
