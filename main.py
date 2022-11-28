from fastapi import FastAPI, Depends, status, HTTPException

from database import engine, SessionLocal
from hashing import Hash
from sqlalchemy.orm import Session
from typing import List
import schemas
import models
import tokenz
from datetime import timedelta

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

@app.get('/user', response_model=List[schemas.ShowUser])
def get_allUser(db: Session = Depends(get_db)):
    return db.query(models.User).all()
     #ini kyk contoh aja intinya bikin fungsi ada return

@app.post('/login')
def login(request:schemas.Login, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Password")
    access_token_expires = timedelta(minutes=tokenz.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = tokenz.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload= True)
    '''
    uvicorn.run ini kalo misalkan kalian langsung run program
    main.py, program fastapi langsung jalan di terminal tinggal ketik python
    uvicorn used so programmer could run the program by python main.py command
    '''