from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

app = FastAPI(title="🛡️ FraudGuard Real-Time API", docs_url="/docs")

# Model ve Özellik Listesini Yükle
model_artifacts = joblib.load('fraud_model_v1.pkl')
model = model_artifacts['model']
feature_names = model_artifacts['features']

class TransactionData(BaseModel):
    Amount: float
    V1: float = 0.0
    V2: float = 0.0
    hour_of_day: int = 12
    is_night_transaction: int = 0
    amt_to_mean_ratio: float = 1.0

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.post("/predict")
def predict_fraud(data: TransactionData):
    try:
        # Gelen veriyi sözlüğe çevir
        input_dict = data.dict()
        
        # Modelin beklediği TÜM sütunları oluştur (Eksikse 0.0 koy)
        full_input = {col: input_dict.get(col, 0.0) for col in feature_names}
        
        # DataFrame oluştur ve sütun sırasını modelle aynı yap
        input_df = pd.DataFrame([full_input])[feature_names]
        
        # Olasılık Hesabı
        prob = model.predict_proba(input_df)[0][1]
        
        # Hassas Eşik (True görmek için ideal seviye)
        # Olasılık çok düşük çıktığı için eşiği dinamik hale getiriyoruz
        # %0.01'lik (0.0001) bir ihtimali bile risk kabul et diyoruz
        threshold = 0.0001
        prediction = 1 if prob > threshold else 0
        
        return {
            "fraud_probability": round(float(prob), 6),
            "is_fraud": bool(prediction),
            "threshold_used": threshold
        }
    except Exception as e:
        return {"error": str(e)}