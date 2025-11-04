from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[Optional[str], Field(default=None)]
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None)]
    gender: Annotated[Literal["male", "female", "others"], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None)]
    weight: Annotated[Optional[float], Field(default=None)]

    @computed_field
    @property
    def bmi(self) -> float:
        if self.weight and self.height:
            return round(self.weight / (self.height**2), 2)
        return None

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi:
            if self.bmi < 18.5:
                return "Underweight"
            elif self.bmi < 30:
                return "Normal"
            else:
                return "Obese"
        return None

class PatientUpdate(BaseModel):

    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None)]
    gender: Annotated[Literal["male", "female", "others"], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None)]
    weight: Annotated[Optional[float], Field(default=None)]


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data


def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=1)


@app.get("/")
def home():
    return {"message": "Patient Management System API is running..."}


@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, pat_update: PatientUpdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    existing_patient = data[patient_id]

    curr_patient_data = pat_update.model_dump(exclude_unset=True) # only give with value, exclude none fields

    for key, val in curr_patient_data.items():
        existing_patient[key] = val # updating new value

    existing_patient['id'] = patient_id
    recreating_Patient = Patient(**existing_patient)
    final_update_data = recreating_Patient.model_dump(exclude='id')
    data[patient_id] = final_update_data
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient Updated"})

