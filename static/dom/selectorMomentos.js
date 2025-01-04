// Objetivo: Cargar los momentos válidos (no nulos) de una materia seleccionada en un selector

document.getElementById("materia").addEventListener("change", function()  {

    // Obtener el valor del estudiante y de la materia seleccionada
    const estudiante = document.getElementById("estudiante").value;
    const materiaSeleccionada = this.value;
    const momentoSelector = document.getElementById("momento");
    const periodo = document.getElementById("periodo").value;
    momentoSelector.innerHTML = "<option value=''>Cargando...</option>";

    // Llamada a la función momentosDisponibles
    fetch(`/consultar-momentos/?materia=${materiaSeleccionada}&estudiante=${estudiante}&periodo=${periodo}`)
        .then(response => response.json())
        .then(data => {

            momentoSelector.innerHTML = "<option value=''>Seleccione un momento</option>";

            // Si no hay momentos, mostrar mensaje
            if (!data.momentos && data.momentos.length === 0){
                momentoSelector.innerHTML = "<option value=''>No hay momentos para cargar...</option>";
                return;    
            }

            // Si hay momentos, cargarlos en el selector
            else {
            data.momentos.forEach(momento => {
                const momentoTextContent = momento
                .replace(/_/g, " ")
                .replace(/\s+/g, ' ')
                .trim()
                .split(' ')
                .map(palabra => palabra ? palabra.charAt(0).toUpperCase() + palabra.slice(1) : "")
                .join(' ');
                const option = document.createElement("option");
                option.value = momento;
                option.textContent = momentoTextContent;
                momentoSelector.appendChild(option);
            });
        }
    })
        .catch(error => {
            console.error("Error al cargar los momentos: ", error);
            momentoSelector.innerHTML = "<option value=''>Error al cargar</option>";
        });
});
