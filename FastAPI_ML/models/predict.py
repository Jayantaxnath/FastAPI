import pickle
import pandas as pd
from pathlib import Path

# Get the directory where this file is located
MODEL_DIR = Path(__file__).parent
MODEL_PATH = MODEL_DIR / "model.pkl"

model = None
class_labels = []

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
        class_labels = model.classes_.tolist()
        print(f"Model loaded Successfully✅ from {MODEL_PATH}")
except Exception as e:
    print(f"Warning: Could not load model from {MODEL_PATH} - {e}")
    print("API will start but predictions will fail until model is loaded🔴")

MODEL_VERSION = '1.0.0'

def predict_output(user_input: dict):
    if model is None:
        raise RuntimeError("Model is not loaded. Please check if model.pkl exists in the models directory.")
    
    input_df = pd.DataFrame(user_input)

    class_output = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    # eg: create mapping {class_name: probabilities}
    class_prob = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": class_output,
        "confidence": round(confidence, 4),
        "class_probabilities": class_prob
    }