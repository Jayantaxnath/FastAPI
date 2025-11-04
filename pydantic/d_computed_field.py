from pydantic import BaseModel, EmailStr, Field, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):  # pydantic model inherit

    # type validation
    name: str
    email: EmailStr
    age: int
    weight: float = Field(..., ge=0) # kg
    height: float = Field(..., gt=0) #meters
    married: bool
    ex: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/self.height**2, 2)

def display(patient: Patient):
    print(f'name: {patient.name}, age: {patient.age}, weight: {patient.weight}, height: {patient.height}')
    print(f'bmi: {patient.bmi}')


patient_info = {
    "name": "jayanta",
    "email": "someone@hdfc.com",
    "age": 65,
    "weight": 64.5,
    "height": 1.6,
    "married": False,
    "ex": ["bob"],
    "contact_details": {"emergency": "8875694102"},
}

patient1 = Patient(**patient_info)  # validation -> corection (int this step)
display(patient1)