from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Load the pre-trained model
model = joblib.load("random_forest_model.pkl")

# Define the FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or "*" to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def home():
    return {"message": "Welcome to the CKD Prediction API!"}
# Define the input schema using Pydantic
class PatientData(BaseModel):
    age: int
    blood_pressure: float
    specific_gravity: float
    albumin: int
    sugar: int
    red_blood_cells: str
    pus_cell: str
    pus_cell_clumps: str
    bacteria: str
    blood_glucose_random: float
    blood_urea: float
    serum_creatinine: float
    sodium: float
    potassium: float
    haemoglobin: float
    packed_cell_volume: int
    white_blood_cell_count: int
    red_blood_cell_count: float
    hypertension: str
    diabetes_mellitus: str
    coronary_artery_disease: str
    appetite: str
    pedal_edema: str
    anemia: str

# Endpoint to receive patient data and return CKD prediction
@app.post("/predict")
async def predict_ckd(age: float,
    blood_pressure: float,
    specific_gravity: float,
    albumin: int,
    sugar: int,
    red_blood_cells: str,
    pus_cell: str,
    pus_cell_clumps: str,
    bacteria: str,
    blood_glucose_random: float,
    blood_urea: float,
    serum_creatinine: float,
    sodium: float,
    potassium: float,
    haemoglobin: float,
    packed_cell_volume: int,
    white_blood_cell_count: int,
    red_blood_cell_count: float,
    hypertension: str,
    diabetes_mellitus: str,
    coronary_artery_disease: str,
    appetite: str,
    pedal_edema: str,
    anemia: str
                      ):
    # Convert input data into a numpy array for the model
    input_data = np.array([[
        age,
        blood_pressure,
        specific_gravity,
        albumin,
        sugar,
        1 if red_blood_cells == 'normal' else 0,
        1 if pus_cell == 'normal' else 0,
        1 if pus_cell_clumps == 'present' else 0,
        1 if bacteria == 'present' else 0,
        blood_glucose_random,
        blood_urea,
        serum_creatinine,
        sodium,
        potassium,
        haemoglobin,
        packed_cell_volume,
        white_blood_cell_count,
        red_blood_cell_count,
        1 if hypertension == 'yes' else 0,
        1 if diabetes_mellitus == 'yes' else 0,
        1 if coronary_artery_disease == 'yes' else 0,
        1 if appetite == 'good' else 0,
        1 if pedal_edema == 'yes' else 0,
        1 if anemia == 'yes' else 0
    ]]).reshape(1, -1)

    # Make a prediction using the model
    prediction = model.predict(input_data)
    result = "Affected" if prediction[0] == 1 else "Not Affected"

    return result
