# FastAPI Project Repository

This repository contains comprehensive FastAPI implementations demonstrating both fundamental API development and machine learning integration.

## 📁 Project Structure

### 1. FastAPI Fundamentals
Located in `FastAPI_Fundamentals/`, this module demonstrates core FastAPI concepts:
- **Patient Management System**: CRUD operations for managing patient records
- **RESTful API endpoints**: GET, POST, PUT, and DELETE operations
- **Data validation**: Request/response validation using Pydantic models
- **Path parameters & Query parameters**: Dynamic routing and filtering

**Key Files:**
- `main.py`: Core API with patient data operations
- `post.py`: POST endpoint implementations
- `put_delete.py`: Update and delete operations
- `patients.json`: Sample patient data storage

### 2. FastAPI ML Integration
Located in `FastAPI_ML/`, this module showcases machine learning model deployment:
- **Insurance Premium Prediction API**: ML model serving through FastAPI
- **Streamlit Frontend**: Interactive web interface for predictions
- **Model Training Pipeline**: Jupyter notebook for model development

**Key Components:**
- `api/app.py`: FastAPI application serving the ML model
- `frontend/streamlit.py`: User-friendly prediction interface
- `model_building.ipynb`: Model training and evaluation
- `dataset/insurance.csv`: Training dataset

### 3. Pydantic Examples
The `pydantic/` directory contains practical examples of Pydantic features including base models, field validation, computed fields, and nested models.

## 🚀 Getting Started

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Jayantaxnath/FastAPI.git
cd FastAPI
```

2. **Create virtual environment:**
```bash
python -m venv myenv
myenv\Scripts\activate  # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Running the Applications

**FastAPI Fundamentals:**
```bash
cd FastAPI_Fundamentals
uvicorn main:app --reload
```

**ML API:**
```bash
cd FastAPI_ML/api
uvicorn app:app --reload
```

**Streamlit Frontend:**
```bash
cd FastAPI_ML/frontend
streamlit run streamlit.py
```

## 🛠️ Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Scikit-learn**: Machine learning model development
- **Pandas & NumPy**: Data manipulation and analysis
- **Streamlit**: Frontend interface for ML predictions
- **Uvicorn**: ASGI server for running FastAPI applications

## 📚 Learning Outcomes

This repository demonstrates:
- Building RESTful APIs with FastAPI
- Data validation and serialization
- ML model deployment and serving
- Integration of frontend and backend services
- Best practices for API development

## 🔗 API Documentation

Once running, access interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📄 License

Open source project for learning and demonstration purposes.
