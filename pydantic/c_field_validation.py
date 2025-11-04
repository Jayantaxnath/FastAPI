from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):  # pydantic model inherit

    # type validation
    name: str
    email: EmailStr
    age: int
    weight: float = Field(..., gt=0)
    married: bool
    ex: List[str]
    contact_details: Dict[str, str]

    @field_validator("email", mode="after")  # after is defaul
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")

        return value

    @field_validator("name")
    @classmethod
    def name_transform(cls, value):
        return value.upper()

    @field_validator("age", mode="after")
    @classmethod
    def age_validate(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")

    @model_validator(mode="after")
    def emergency_validate(self):
        if self.age > 60 and "emergency" not in self.contact_details:
            raise ValueError("Patient older than 60 must have emegency contact")
        return self


def insert_patient_Data(patient1: Patient):
    print(patient1.name)


def update_patient_Data(patient1: Patient):
    print(f"updated")


patient_info = {
    "name": "jayanta",
    "email": "someone@hdfc.com",
    "age": 65,
    "weight": "64.4",
    "married": False,
    "ex": ["bob"],
    "contact_details": {"emergency": "8875694102"},
}

patient1 = Patient(**patient_info)  # validation -> corection (int this step)
