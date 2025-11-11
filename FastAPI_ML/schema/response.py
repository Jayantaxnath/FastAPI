from pydantic import BaseModel, Field
from typing import Dict

class PredictonResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="The predicted insurance premium category",
        example="High"
        # example=["High"]
    )
    confidence: float  = Field(
        ...,
        description="Model's confidence score for the predicted class {range: 0 to 1}",
        example=0.95
        #examples=[0.95]
    )
    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probabilities distribution across all possible classes",
        # example={"Low": 0.01, "Medium": 0.12, "High": 0.95}
        examples=[{"Low": 0.01, "Medium": 0.12, "High": 0.95}]
    )