// Selector de períodos dodne cargar revisiones

document.getElementById("cargarRevisionModal").addEventListener("shown.bs.modal", function(event) {
    const button = event.relatedTarget;
    const url = button.dataset.url;
    const selectorPeriodos = document.getElementById("periodoRevision");
    const estudiante = document.getElementById("estudiante").value;
    const selectorMateriasReprobadas = document.getElementById("materiaRevision");
    selectorMateriasReprobadas.disabled = true;

    selectorPeriodos.innerHTML = "<option value=''>Cargando...</option>";
    
    fetch(`${url}?estudiante=${estudiante}`)
        .then(response => response.json())
        .then(data => {
            selectorPeriodos.innerHTML = "<option value=''>Seleccione un período</option>";
            data.periodos_reprobados.forEach(periodo => {
                const periodo_inicio = periodo.inicio;
                const periodo_finalizacion = periodo.finalizacion;
                const option = document.createElement("option");
                option.value = periodo.id;
                option.textContent = `${periodo_inicio} - ${periodo_finalizacion}`;
                selectorPeriodos.appendChild(option);
            });
        })

    .catch(error => {
        console.error("Error al cargar los períodos: ", error);
        selectorPeriodos.innerHTML = "<option value=''>Error al cargar</option>";
    });
})

    document.getElementById("periodoRevision").addEventListener("change", function() {
        const periodo = this.value;
        const estudiante = document.getElementById("estudiante").value;
        const selectorMateriasReprobadas = document.getElementById("materiaRevision");
        selectorMateriasReprobadas.innerHTML = "<option value=''>Cargando...</option>";
        fetch(`/materias-reprobadas-revision/?estudiante=${estudiante}&periodo=${periodo}`)

            .then(response => response.json())
            .then(data => {
                selectorMateriasReprobadas.disabled = false;
                selectorMateriasReprobadas.innerHTML = "<option value=''>Seleccione una materia</option>";
                data.materias_reprobadas.forEach(materia => {
                    const nombre_materia = materia.nombre_materia;
                    const materia_id = materia.id;
                    const option = document.createElement("option");
                    option.value = materia_id;
                    option.textContent = nombre_materia;
                    selectorMateriasReprobadas.appendChild(option);
                });
            })

            .catch(error => {
                console.error("Error al cargar materias", error);
                selectorMateriasReprobadas.disabled = true;
                selectorMateriasReprobadas.innerHTML = "<option value=''>Por favor, seleccione un período</option>";
            })
    })
