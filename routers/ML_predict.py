from fastapi import APIRouter, Depends
from .auth.authentication import *
from.auth.oauth2 import *
from .SchemaModels import schemas
import joblib
import numpy as np
import pandas as pd

router_ml = APIRouter(tags=["Machine Learning Model"])
@router_ml.post("/predict_loan")
def predict(input: LenderData, current_user: BaseUserData = Depends(get_current_user)):
    file = open("ml/train_model.joblib", "rb")
    trained_model = joblib.load(file)
    types = {
        "Dependents" : np.int32,
        "Education" : np.int32,
        "ApplicantIncome" : np.int64,
        "CoapplicantIncome" : np.float64,
        "LoanAmount" : np.int32,
        "Credit_History" : np.float64,
        "Property_Area" : np.int32,
        "Male" : np.uint8,
        "Self_Employed_Yes" : np.uint8,
        "married_Yes" : np.uint8,
    }

    input_arr = [input.Dependents,input.Education,input.ApplicantIncome,input.CoapplicantIncome,input.LoanAmount, input.Credit_History, input.Property_Area, input.Male, input.Self_Employed_Yes, input.married_Yes]
    df = pd.DataFrame(input_arr).transpose()
    df.columns = list(types.keys())
    df = df.astype(types)
    df.to_numpy()
    
    amount = int(df["LoanAmount"])
    results = (trained_model.predict(df))
    if results == 1:
        results = "Accepted"
    else :
        results = "Declined"
    
    return {"Loan Status:": results,
                "Loan Amount" : amount}