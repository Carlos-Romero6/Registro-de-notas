// Eliminar estudiante
function borrarEstudiante(estudiante_id) {
    if (confirm("¿Estás seguro de que quieres eliminar a este estudiante? No se podrán descartar los cambios")) {
        fetch(`eliminar/${estudiante_id}/`)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert(data.message)
            } else {
                alert("Error al eliminar estudiante.")
            }
        })
        .catch(error => console.error("Error:", error))
    }
}