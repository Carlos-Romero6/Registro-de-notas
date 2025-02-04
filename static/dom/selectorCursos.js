// Dinamizar selector de secciones
document.getElementById('curso').addEventListener('change', function () { // Ubica un elemento por su ID y le implementa un evento
  const cursoSeleccionado = this.value; //Declara una constante para el curso que se eligió en el selector
  const seccionSelector = document.getElementById('seccion'); // Toma al selector de seccion por su ID
  seccionSelector.innerHTML = '<option value="">Cargando...</option>'; //Cambia el contenido de la opcion por "Cargando..."

  // Llama a la url que ejecuta la funcion en el backend que devolveria un json
  fetch(`/consultar-secciones/?curso=${cursoSeleccionado}`)
    .then(response => response.json()) // El json tiene los datos de las secciones del curso que se seleccionó
    .then(data => {
      seccionSelector.innerHTML = '<option value="">Seleccione una sección</option>'; // Limpia el selector

      data.secciones.forEach(seccion => { // Itera sobre las secciones obtenidas en el Json
        const option = document.createElement('option'); // Crea una opcion para cada seccion en el selector
        option.value = seccion; // Asigna el valor de la opcion que se crea
        option.textContent = seccion; // Cotenido de la etiqueta <option></option>
        seccionSelector.appendChild(option); // Añade la opcion al selector
      });
    })
    .catch(error => { // En caso de que haya un error
      console.error('Error al cargar las secciones: ', error); // Imprime un error en la consola del servidor
      seccionSelector.innerHTML = '<option value="">Error al cargar</option>'; // Escribe un error en la opcion del selector
    });
});

