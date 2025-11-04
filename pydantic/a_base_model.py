from pydantic import BaseModel


class Patient(BaseModel):  # pydantic model inherit

    # type validation
    name: str
    age: int
    weight: float


def insert_patient_Data(patient1: Patient):
    print(f"{patient1.name} {patient1.age} inserted")


def update_patient_Data(patient1: Patient):
    print(f"{patient1.name} {patient1.age} updated")


patient_info = {"name": "jayanta", "age": "45", "weight": 454}

patient1 = Patient(**patient_info)

insert_patient_Data(patient1)
update_patient_Data(patient1)
