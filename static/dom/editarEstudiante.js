// Editar un estudiante
let ESTUDIANTE_ID

// Mostrar secciones
function disponerSecciones() { 
    const cursoSeleccionado = document.getElementById('curso-edit').value;
    const seccionSelector = document.getElementById('edit-seccion');
    seccionSelector.innerHTML = '<option value="">Cargando...</option>';
  

    fetch(`/consultar-secciones/?curso=${cursoSeleccionado}`)
    .then(response => response.json())
    .then(data => {
        seccionSelector.innerHTML = '<option value="">Seleccione una sección</option>';
  
        data.secciones.forEach(seccion => { 
            const option = document.createElement('option'); 
            option.value = seccion;
            option.textContent = seccion;
            seccionSelector.appendChild(option);
        });
    })
    .catch(error => {
        console.error('Error al cargar las secciones: ', error);
        seccionSelector.innerHTML = '<option value="">Error al cargar</option>';
    });
}

// Llenar formulario con datos del estudiante
function editarEstudiante(estudiante_id) {
    if (confirm("¿Estás seguro de que quieres editar datos de este estudiante?")) {
        let formulario = new bootstrap.Modal(document.getElementById('modalEditarEstudiante'));
        formulario.show();
        ESTUDIANTE_ID = estudiante_id;

        fetch(`../obtener-datos/?estudiante=${estudiante_id}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('edit-nombres').value = data.nombres;
            document.getElementById('edit-apellidos').value = data.apellidos;
            document.getElementById('edit-cedula').value = data.ci;
            document.getElementById('edit-genero').value = data.genero;
            disponerSecciones();
        })
        .catch(error => {
            console.error("Error:", error);
        })
    }
}

// Confirmar la edición de datos
document.getElementById('editarEstudiante').addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(this)
    if (confirm("¿Estás seguro de que quieres actualizar los datos de este estudiante?"))
    fetch(`../actualizar/${ESTUDIANTE_ID}/`, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Se ha actualizado el estudiante exitosamente.");
            let modal = new bootstrap.Modal(document.getElementById('modalEditarEstudiante'));
            modal.hide();
            window.location.reload();
        } else {
            alert(`${data.message}`);
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Ocurrió un error inesperado.");
    });
});