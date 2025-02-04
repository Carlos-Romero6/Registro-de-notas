document.getElementById('cargarNota').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const url = document.getElementById("urlCargarNotas").value;
    fetch(`${url}`, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
        alert("Se ha cargado correctamente.");
        const modal = new bootstrap.Modal(document.getElementById('cargarNotaModal'));
        modal.hide();
        this.reset();
        window.location.reload();
        } 
        else {
        alert("Error al cargar nota.");
        }
    })
    .catch(error => {
        console.error('Error: ', error);
        alert("Ocurrió un error inesperado.");
    });

})
