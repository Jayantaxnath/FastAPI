from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


address_dict = {"city": "Tezpur", "state": "Assam", "pin": "784001"}

address1 = Address(**address_dict)

patient_dict = {"name": "jayanta", "gender": "male", "age": 20, "address": address1}

patient01 = Patient(**patient_dict)

print(patient01)
print(patient01.name, patient01.age)
print(patient01.address.city, patient01.address.pin)


temp = patient01.model_dump(exclude=['name', 'address']) # {'address' : ['pin']}
print(temp, type(temp))