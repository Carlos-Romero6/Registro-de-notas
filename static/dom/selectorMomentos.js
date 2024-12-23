document.getElementById("materia").addEventListener("change", function()  {
    const estudiante = document.getElementById("estudiante").value;
    const materiaSeleccionada = this.value;
    const momentoSelector = document.getElementById("momento");
    momentoSelector.innerHTML = "<option value=''>Cargando...</option>";
    fetch(`/consultar-momentos/?materia=${materiaSeleccionada}&estudiante=${estudiante}`)
        .then(response => response.json())
        .then(data => {

            momentoSelector.innerHTML = "<option value=''>Seleccione un momento</option>";
            if (!data.momentos && data.momentos.length === 0){
                momentoSelector.innerHTML = "<option value=''>No hay momentos para cargar...</option>";
                return;    
            }
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
