# importing libraires
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sklearn.compose import _column_transformer
_column_transformer._RemainderColsList = object

import pandas as pd
import joblib


app = FastAPI()

class Input(BaseModel):
    department: object
    region: object
    education: object
    gender: object
    recruitment_channel: object
    previous_year_rating: float
    no_of_trainings: int
    age: int
    length_of_service: int
    #KPIs_met: int
    #awards_won: int
    awards_won: int = Field(..., alias="awards_won?")
    KPIs_met: int = Field(..., alias="KPIs_met >80%")
    avg_training_score: int


class Output(BaseModel):
    is_promoted: int

@app.post("/predict")
async def predict(data: Input) -> Output:
    X_input = pd.DataFrame([[data.department,data.region,data.education,data.gender,
              data.recruitment_channel,data.no_of_trainings,data.age,data.previous_year_rating,
              data.length_of_service,data.KPIs_met,data.awards_won,data.avg_training_score]])

    X_input.columns = ['department','region','education','gender','recruitment_channel',
                       'no_of_trainings','age','previous_year_rating','length_of_service','KPIs_met >80%','awards_won?',
                       'avg_training_score']

    #load model
    model = joblib.load('APIDevelopment/model_pipeline.pkl')

    #predict
    prediction = model.predict(X_input)

    #output
    return Output(is_promoted = prediction)
