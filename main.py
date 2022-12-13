from fastapi import FastAPI, Depends, status, HTTPException,File, UploadFile
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from .config.database import engine, SessionLocal
from datetime import timedelta
import shutil
import joblib

import numpy as np
import pandas as pd
import uvicorn
from .routers.ML_predict import *
from .routers.user import *
from SchemaModels import models
#

#migrate database
models.Base.metadata.create_all(bind=engine) #to create database

app = FastAPI()

app.include_router(router_ml)
app.include_router(router_user)




if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload= True)
    '''
    uvicorn.run ini kalo misalkan kalian langsung run program
    main.py, program fastapi langsung jalan di terminal tinggal ketik python
    uvicorn used so programmer could run the program by python main.py command
    '''