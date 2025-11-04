from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):  # pydantic model inherit

    # type validation
    name: Annotated[
        str, Field(max_length=40, title="patient name", description="here description ")
    ]
    age: int = Field(gt=0, lt=120)
    weight: Annotated[
        float, Field(gt=0, strict=False)
    ]  # will not allow '64.4' (for True)
    height: float
    email: EmailStr = Field(default=None)
    married: bool
    ex: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def insert_patient_Data(patient1: Patient):
    print(f"{patient1.name} {patient1.age} inserted")


def update_patient_Data(patient1: Patient):
    print(f"{patient1.name} {patient1.age} updated")


patient_info = {
    "name": "jayanta",
    "age": "45",
    "weight": "64.4",
    "height": 1.6,
    "married": False,
    "contact_details": {"mom": "9707885094", "dad": "8875694102"},
}

patient1 = Patient(**patient_info)

insert_patient_Data(patient1)
update_patient_Data(patient1)
