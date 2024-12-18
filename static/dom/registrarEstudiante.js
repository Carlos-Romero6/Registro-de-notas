// Agregar estudiante
document.getElementById('agregarEstudiante').addEventListener('submit', function(event) {
  event.preventDefault();
  const formData = new FormData(this);
  fetch(`/estudiantes/agregar/`, {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      alert("Se ha agregado correctamente.");
      $('#modalAgregarEstudiante').modal('hide');
      window.location.reload();
    } else {
      alert("Error al cargar estudiante.");
    }
  })
  .catch(error => {
    console.error('Error: ', error);
    alert("Ocurrió un error inesperado.");
  });
});