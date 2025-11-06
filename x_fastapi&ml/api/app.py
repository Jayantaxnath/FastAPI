from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated

import pickle
import pandas as pd

# importing the ml model
# C:\Users\HP\Desktop\FastAPI\x_fastapi&ml\models\model.pkl

with open("../models/model.pkl", "rb") as f:
    model = pickle.load(f)
    if model:
        print("Model loaded Successfully✅")
    else:
        print("Model not found🔴")

tier_1_cities = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Chennai",
    "Kolkata",
    "Hyderabad",
    "Pune",
]
tier_2_cities = [
    "Jaipur",
    "Chandigarh",
    "Indore",
    "Lucknow",
    "Patna",
    "Ranchi",
    "Visakhapatnam",
    "Coimbatore",
    "Bhopal",
    "Nagpur",
    "Vadodara",
    "Surat",
    "Rajkot",
    "Jodhpur",
    "Raipur",
    "Amritsar",
    "Varanasi",
    "Agra",
    "Dehradun",
    "Mysore",
    "Jabalpur",
    "Guwahati",
    "Thiruvananthapuram",
    "Ludhiana",
    "Nashik",
    "Allahabad",
    "Udaipur",
    "Aurangabad",
    "Hubli",
    "Belgaum",
    "Salem",
    "Vijayawada",
    "Tiruchirappalli",
    "Bhavnagar",
    "Gwalior",
    "Dhanbad",
    "Bareilly",
    "Aligarh",
    "Gaya",
    "Kozhikode",
    "Warangal",
    "Kolhapur",
    "Bilaspur",
    "Jalandhar",
    "Noida",
    "Guntur",
    "Asansol",
    "Siliguri",
]

# FastAPI Boject
app = FastAPI()


# Pydantic model for data validation
class User(BaseModel):

    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the user")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user in kg")]
    height: Annotated[float, Field(..., gt=0, lt=250, description="Height of the user in cm")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Salary of the user")]
    smoker: Annotated[bool, Field(..., description="User Smoke?")]
    city: Annotated[str, Field(..., description="Current city of the user")]
    occupation: Annotated[
        Literal[
            "private_job",
            "freelancer",
            "student",
            "retired",
            "business_owner",
            "government_job",
            "unemployed",
        ],
        Field(..., description="User occupation"),
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        # Convert height from cm to meters for BMI calculation
        height_in_meters = self.height / 100
        return self.weight / (height_in_meters**2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        # Map both tier 2 and tier 3 cities to tier 2 
        # because the model was only trained with tier 1 and tier 2
        else:
            return 2


@app.get("/")
def home():
    return {"message": "API is running..."}


@app.post("/predict")
def predict_premium(data: User):  # input the of User type

    input_df = pd.DataFrame(
        [
            {
                "bmi": data.bmi,
                "age_group": data.age_group,
                "lifestyle_risk": data.lifestyle_risk,
                "city_tier": data.city_tier,
                "income_lpa": data.income_lpa,
                "occupation": data.occupation,
            }
        ]
    )

    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={"predicted_category": prediction})
