from fastapi import FastAPI, Depends, status, HTTPException,File, UploadFile
from fastapi.security import OAuth2PasswordRequestForm
from database import engine, SessionLocal
from hashing import Hash
from sqlalchemy.orm import Session
from typing import List
import schemas,authentication, oauth2
import models
import tokenz
from datetime import timedelta
import shutil
from ml import model
import joblib

import numpy as np
import pandas as pd
import uvicorn
#

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#migrate database
models.Base.metadata.create_all(bind=engine) #to create database

app = FastAPI()

@app.post('/user') #(/ itu adalah path  )
def create_user(user : schemas.BaseUserData, db:Session = Depends(get_db)):
    new_user = models.User(username=user.username, password=Hash.bcrypt(user.password), email=user.email, secretCombination=user.secretCombination) #manualnya (user.name = username, dst) **user.dict()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post('/exclusive') #(/ itu adalah path  )
def protected_function(current_user: schemas.BaseUserData = Depends(oauth2.get_current_user)):
    pass

@app.get('/user', response_model=List[schemas.ShowUser])
def get_allUser(db: Session = Depends(get_db)):
    return db.query(models.User).all()
     #ini kyk contoh aja intinya bikin fungsi ada return

@app.post('/login')

def login(db:Session=Depends(get_db), request:OAuth2PasswordRequestForm=Depends()):
	return authentication.login(request=request, db=db)

@app.post('/upload_file')

async def upload_file(file: UploadFile = File(...)):
    with open('sample.csv', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_name": file.filename}

@app.post("/predict_csv")
def predict_csv(csv_file: UploadFile = File(...)):
    with open('sample.csv', "wb") as buffer:
        shutil.copyfileobj(csv_file.file, buffer)
    try:
        df = pd.read_csv('sample.csv')
    except:
        raise HTTPException(
            status_code=422, detail="Unable to process file"
        )
    df_n_instances, df_n_features = df.shape
    if df_n_features != model.n_features:
        raise HTTPException(
            status_code=422,
            detail=f"Each data point must contain {n_features} features",
        )

    model.model_obj.predict()
    result = "done"

    return result

@app.post("/predict_loan")
def predict(input: schemas.LenderData):
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
#Machine Learning




if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload= True)
    '''
    uvicorn.run ini kalo misalkan kalian langsung run program
    main.py, program fastapi langsung jalan di terminal tinggal ketik python
    uvicorn used so programmer could run the program by python main.py command
    '''