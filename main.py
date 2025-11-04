from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()  # creating object


# func to return stored patients data
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"message": "API to manage patients records."}


@app.get("/view")
def view():
    data = load_data()
    return data


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id=Path(..., description="ID of the patient in DB", example="p001")
):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(
        status_code=404, detail="Not found"
    )  # {"error":"Patient not found."}


@app.get("/sort")
def sort_patients(
    sort_by: str = Query("bmi", description="sort: height, weight or bmi"),
    order: str = Query("asc", description="sorting: asc/desc"),
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400, detail="Invalid field select from {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order, select asc/desc")

    data = load_data()
    s_order = True if order == "desc" else False
    sorted_data = sorted(
        data.values(), key=lambda x: x.get(sort_by, 0), reverse=s_order
    )
    return sorted_data
