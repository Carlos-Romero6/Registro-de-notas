// Dinamizar selector de secciones
document.getElementById('cursomateria').addEventListener('change', function () { // Ubica un elemento por su ID y le implementa un evento
    const cursoSeleccionado = this.value; //Declara una constante para el curso que se eligió en el selector
    const materiaSelector = document.getElementById('nombremateria'); // Toma al selector de seccion por su ID
    const pensumSeleccionado = document.getElementById('pensummateria'); // Toma al selector de pensum por su ID
    materiaSelector.innerHTML = '<option value="">Cargando...</option>'; //Cambia el contenido de la opcion por "Cargando..."
    
    // Llama a la url que ejecuta la funcion en el backend que devolveria un json
    fetch(`/consultar-materias/?curso=${cursoSeleccionado}&pensum=${pensumSeleccionado}`) 
      .then(response => response.json()) // El json tiene los datos de las secciones del curso que se seleccionó
    .then(data => {
        materiaSelector.innerHTML = '<option value="">Seleccione una sección</option>'; // Limpia el selector

        data.secciones.forEach(materias => { // Itera sobre las secciones obtenidas en el Json
          const option = document.createElement('option'); // Crea una opcion para cada seccion en el selector
          option.value = materias; // Asigna el valor de la opcion que se crea
          option.textContent = materias; // Cotenido de la etiqueta <option></option>
          materiaSelector.appendChild(option); // Añade la opcion al selector
        });
    })
      .catch(error => { // En caso de que haya un error
        console.error('Error al cargar las materias: ', error); // Imprime un error en la consola del servidor
        materiaSelector.innerHTML = '<option value="">Error al cargar</option>'; // Escribe un error en la opcion del selector
    });
});