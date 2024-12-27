// Agregar estudiante

function modalAgregarEstudiante() {
  document.getElementById('nombres').value = "";
  document.getElementById('apellidos').value = "";
  document.getElementById('cedula').value = "";
  document.getElementById('genero').value = "";
  let ventana = new bootstrap.Modal(document.getElementById('modalAgregarEstudiante'));
  ventana.show();
}

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
      let modal = new bootstrap.Modal(document.getElementById('modalAgregarEstudiante'));
      modal.hide();
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