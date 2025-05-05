from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, List
from datetime import date
from datetime import datetime

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# For development: allow all origins (not safe for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class PatientBase(BaseModel):
    name: str
    last_name: str
    sex: str
    birth_date: str = Field(..., description="Birth date in format dd/mm/yyyy")
    weight_kg: float = Field(..., gt=0, description="Weight in kilograms")
    height_cm: float = Field(..., gt=0, description="Height in centimeters")
    goal: Optional[str] = Field(None, description="Patient's goal (e.g., lose weight, gain muscle, maintain)")

    @validator("birth_date")
    def parse_birth_date(cls, value):
        try:
            return datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Birth date format must be dd/mm/yyyy")

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    patient_id: int
    age: Optional[int] = None
    bmr: Optional[float] = None

    @validator("birth_date", pre=True)
    def format_birth_date(cls, value):
        if isinstance(value, date):
            return value.strftime("%d/%m/%Y")
        return value

class Macros(BaseModel):
    fat: Optional[str] = None
    protein: Optional[str] = None
    carbohydrates: Optional[str] = None

class Diet(BaseModel):
    diet: str
    macros: Macros

# Simulación de base de datos en memoria
patients_db = {}
next_patient_id = 1

diets_data: List[Dict] = [
    {
        "diet": "Keto (Ketogenic) Diet",
        "macros": {
            "fat": "70-75%",
            "protein": "20-25%",
            "carbohydrates": "5-10%"
        }
    },
    {
        "diet": "Paleo (Paleolithic) Diet",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        },
    },
    {
        "diet": "Vegan Diet",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "Vegetarian Diet",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "Mediterranean Diet",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "DASH (Dietary Approaches to Stop Hypertension) Diet",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "Flexitarian Diet",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "MIND (Mediterranean-DASH Intervention for Neurodegenerative Delay) Diet",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "Cyclical Ketogenic Diet (CKD)",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "Targeted Ketogenic Diet (TKD)",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "Atkins Diet",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "Zone Diet",
        "macros": {
            "fat": "30%",
            "protein": "30%",
            "carbohydrates": "40%"
        }
    },
    {
        "diet": "Intermittent Fasting",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "Dukan Diet",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "Alkaline Diet",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "Gluten-Free Diet",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    },
    {
        "diet": "Paleo Autoimmune Protocol (AIP)",
        "macros": {
            "fat": "N/A",
            "protein": "N/A",
            "carbohydrates": "N/A"
        }
    }
]

diets_db: Dict[str, Dict] = {item["diet"]: item for item in diets_data}


def calculate_age(birth_date: date) -> int:
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def calculate_bmr(weight_kg: float, height_cm: float, age: int, sex: str) -> float:
    """Calculates basal metabolic rate using the Mifflin-St Jeor formula."""
    if sex.lower() == "male":
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    elif sex.lower() == "female":
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
    else:
        raise ValueError("Sex must be 'male' or 'female'")
    return bmr

@app.post("/patients/", response_model=Patient, status_code=201)
async def create_patient(patient: PatientCreate):
    global next_patient_id
    age = calculate_age(patient.birth_date)
    bmr = calculate_bmr(patient.weight_kg, patient.height_cm, age, patient.sex)
    new_patient = Patient(patient_id=next_patient_id, age=age, bmr=bmr, **patient.dict())
    patients_db[next_patient_id] = new_patient
    next_patient_id += 1
    return new_patient

@app.get("/patients/{patient_id}", response_model=Patient)
async def read_patient(patient_id: int):
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail="Patient not found")
    patient = patients_db[patient_id]
    patient.age = calculate_age(patient.birth_date)
    patient.bmr = calculate_bmr(patient.weight_kg, patient.height_cm, patient.age, patient.sex)
    return patient

@app.put("/patients/{patient_id}", response_model=Patient)
async def update_patient(patient_id: int, updated_patient: PatientBase):
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail="Patient not found")
    existing_patient = patients_db[patient_id]
    age = calculate_age(updated_patient.birth_date)
    bmr = calculate_bmr(updated_patient.weight_kg, updated_patient.height_cm, age, updated_patient.sex)
    updated_patient_with_id = Patient(patient_id=patient_id, age=age, bmr=bmr, **updated_patient.dict())
    patients_db[patient_id] = updated_patient_with_id
    return updated_patient_with_id

@app.delete("/patients/{patient_id}", status_code=204)
async def delete_patient(patient_id: int):
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail="Patient not found")
    del patients_db[patient_id]
    return {"message": "Patient deleted"}

@app.get("/diets/{diet_name}", response_model=Macros)
async def get_diet_macros(diet_name: str):
    if diet_name in diets_db:
        return Macros(**diets_db[diet_name]["macros"])
    raise HTTPException(status_code=404, detail="Diet not found")

@app.get("/diets/", response_model=List[str])
async def get_all_diet_names():
    """Returns a list of all available diet names."""
    return list(diets_db.keys())

# To run this API: uvicorn patients_api:app --reload --port 8000