from fastapi import FastAPI, Depends, status, HTTPException,File, UploadFile, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from .config.database import get_db
from .auth.hashing import Hash
from sqlalchemy.orm import Session
from typing import List
from .SchemaModels import models, schemas
from .auth import authentication, oauth2

router_user = APIRouter(
    tags=["User"]
)

@router_user.post('/user') #(/ itu adalah path  )
def create_user(user : BaseUserData, db:Session = Depends(get_db)):
    new_user = User_Real(username=user.username, password=Hash.bcrypt(user.password), email=user.email, securityquestion=user.securityquestion, securityanswer=user.securityanswer) #manualnya (user.name = username, dst) **user.dict()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router_user.get('/user/getUser', response_model=List[ShowUser])
def get_allUser(db: Session = Depends(get_db)):
    return db.query(User_Real).all()
     #ini kyk contoh aja intinya bikin fungsi ada return