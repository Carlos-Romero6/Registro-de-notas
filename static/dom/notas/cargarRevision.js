document.getElementById("cargarRevision").addEventListener("submit", function(event) {
    event.preventDefault();
    alert("¿Esta seguro que quiere cargar la revisión? No se podrá modificar lo cargado.");
    const formData = new FormData(this);
    const estudiante = document.getElementById("estudiante").value;
    const url = document.getElementById("urlCargarRevision").value
    fetch(`${url}?estudiante=${estudiante}`, {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if(data.success) {
                alert(data.message);
                const modal = new bootstrap.Modal(document.getElementById("cargarRevisionModal"));
                modal.hide();
                this.reset();
                window.location.reload();
            }
            else {
                alert(data.message);
            }
        })

        .catch(error => {
            console.error('Error:', error);

        })
})
