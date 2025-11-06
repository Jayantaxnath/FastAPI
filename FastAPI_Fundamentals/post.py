from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

app = FastAPI()


class Patient(BaseModel):

    id: Annotated[str, Field(..., description="Unique ID", examples=["p001"])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="Current city")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient")]
    gender: Annotated[
        Literal["male", "female", "others"],
        Field(..., description="Gender of the patient"),
    ]
    height: Annotated[float, Field(..., gt=0, description="Current Height in meters")]
    weight: Annotated[float, Field(..., gt=0, description="Current Weight in kgs")]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height**2), 2)

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Obese"

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data

def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=1)


@app.get('/')
def home():
    return {'message': "Patient Management System API is running..."}

@app.post('/create')
def create_patient(patient_: Patient):

    data = load_data()

    if patient_.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')
    
    data[patient_.id] = patient_.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(status_code=201, content={"message": "patient created successfully"})