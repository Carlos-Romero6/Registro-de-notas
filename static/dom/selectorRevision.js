// Objetivo: Cambiar las opciones de justificación si el momento seleccionado es "revision"


document.getElementById("momento").addEventListener("change", function() {

    // Obtener el valor del momento seleccionado
    const momento = document.getElementById("momento").value;
    const justificacion = document.getElementById("justificacion");

    if (momento === "revision") {
        justificacion.innerHTML = "<option value='revision' selected disable>Las revisiones no tienen justificaciones</option>";
    }
    else {
        options = [
            {value: "C", text: "C (cursado)"}, {value: "I", text: "I (inasistente)"}, {value: "NC", text: "NC (no cursado)"}, {value: "NP", text: "NP (no presentado)"}, {value: "EXO", text: "EXO (exonerado)"}, {value: "RT", text: "RT (retirado)"}, {value: "DES", text: "DES (desertor)"}
        ]
        // Crear las opciones de justificación si se selecciona un momento válido
        optionsHTML = options.map(option => `<option value="${option.value}">${option.text}</option>`);
        justificacion.innerHTML = optionsHTML.join("");
    }

    })