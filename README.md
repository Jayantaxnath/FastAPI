# FastAPI Practice Repository

This is a practice repository for learning FastAPI with patient data management.

Thanks to the **FastAPI CampusX YouTube channel** for the excellent tutorials!

## Overview

This project implements a simple Patient Management System API using FastAPI. It demonstrates:
- RESTful API endpoints (GET, POST, PUT)
- Pydantic models for data validation
- JSON file storage for patient records
- Computed fields (BMI calculation)
- Error handling and HTTP status codes

## Getting Started

1. Activate the virtual environment:
   ```powershell
   .\myenv\Scripts\Activate.ps1
   ```

2. Run the application:
   ```powershell
   uvicorn post:app --reload
   ```

3. Access the API documentation at `http://127.0.0.1:8000/docs`

## Acknowledgments

Special thanks to the **CampusX YouTube channel** for their comprehensive FastAPI tutorials!
