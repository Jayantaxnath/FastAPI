from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import sys
from pathlib import Path
import pandas as pd

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))
from schema.user_input import User # pydantic model
from config.city_tier import tier_1_cities, tier_2_cities
from models.predict import predict_output, MODEL_VERSION
from schema.response import PredictonResponse


# FastAPI Boject
app = FastAPI()

# human readable
@app.get("/")
def home():
    return {"message": "API is running..."}

# machine readable
@app.get("/health")
def health_check():
    return {
        'status' : 'OK',
        'version' : MODEL_VERSION
    }

@app.post("/predict", response_model=PredictonResponse)
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

    try:
        prediction = predict_output(input_df)
        return JSONResponse(status_code=200, content={"response": prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
