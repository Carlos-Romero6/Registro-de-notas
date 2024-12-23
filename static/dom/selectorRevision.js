document.getElementById("momento").addEventListener("change", function() {
    const momento = document.getElementById("momento").value;
    const justificacion = document.getElementById("justificacion");

    if (momento === "revision") {
        justificacion.innerHTML = "<option value='Sin justificacion' disabled selected>Las revisiones no tienen justificaciones</option>";
    }
    else {
        options = [
            {value: "C", text: "C (cursado)"}, {value: "I", text: "I (inasistente)"}, {value: "NC", text: "NC (no cursado)"}, {value: "NP", text: "NP (no presentado)"}, {value: "EXO", text: "EXO (exonerado)"}, {value: "RT", text: "RT (retirado)"}, {value: "DES", text: "DES (desertor)"}
        ]
        optionsHTML = options.map(option => `<option value="${option.value}">${option.text}</option>`);
        justificacion.innerHTML = optionsHTML.join("");
    }

    })