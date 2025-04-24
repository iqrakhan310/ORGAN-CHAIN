async function makePrediction() {
    const formData = {
        age: parseInt(document.getElementById('age').value),
        blood_pressure: (document.getElementById('bp').value),
        specific_gravity: (document.getElementById('sg').value),
        albumin: (document.getElementById('al').value),
        sugar: (document.getElementById('su').value),
        red_blood_cells: document.getElementById('rbc').value === "normal" ? 0 : 1,
        pus_cell: document.getElementById('pc').value === "normal" ? 0 : 1,
        pus_cell_clumps: document.getElementById('pcc').value === "notpresent" ? 0 : 1,
        bacteria: document.getElementById('ba').value === "notpresent" ? 0 : 1,
        blood_glucose_random: parseFloat(document.getElementById('bgr').value),
        blood_urea: parseFloat(document.getElementById('bu').value),
        serum_creatinine: parseFloat(document.getElementById('sc').value),
        sodium: parseFloat(document.getElementById('sod').value),
        potassium: parseFloat(document.getElementById('pot').value),
        haemoglobin: parseFloat(document.getElementById('hemo').value),
        packed_cell_volume: parseFloat(document.getElementById('pcv').value),
        white_blood_cell_count: parseFloat(document.getElementById('wbcc').value),
        red_blood_cell_count: parseFloat(document.getElementById('rbcc').value),
        hypertension: document.getElementById('htn').value === "1" ? 1 : 0,
        diabetes_mellitus: document.getElementById('dm').value === "1" ? 1 : 0,
        coronary_artery_disease: document.getElementById('cad').value === "1" ? 1 : 0,
        appetite: document.getElementById('appet').value === "1" ? 1 : 0,
        peda_edema: document.getElementById('pe').value === "1" ? 1 : 0,
        anemia: document.getElementById('ane').value === "1" ? 1 : 0
    };

    const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
    });

    const result = await response.json();
    document.getElementById("result").textContent = `Prediction: ${result.prediction ? 'CKD' : 'No CKD'}`;
}
