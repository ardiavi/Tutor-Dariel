from fastapi import FastAPI, Depends, status, HTTPException,File, UploadFile, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from config.database import get_db
from auth.hashing import Hash
from sqlalchemy.orm import Session
from typing import List
from SchemaModels import models, schemas
from auth import authentication, oauth2

router = APIRouter(
    tags=["User"]
)

@router.post('/user') #(/ itu adalah path  )
def create_user(user : schemas.BaseUserData, db:Session = Depends(get_db)):
    new_user = models.User(username=user.username, password=Hash.bcrypt(user.password), email=user.email, secretCombination=user.secretCombination) #manualnya (user.name = username, dst) **user.dict()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/exclusive') #(/ itu adalah path  )
def protected_function(current_user: schemas.BaseUserData = Depends(oauth2.get_current_user)):
    pass

@router.get('/user', response_model=List[schemas.ShowUser])
def get_allUser(db: Session = Depends(get_db)):
    return db.query(models.User).all()
     #ini kyk contoh aja intinya bikin fungsi ada return

@router.post('/login')

def login(db:Session=Depends(get_db), request:OAuth2PasswordRequestForm=Depends()):
	return authentication.login(request=request, db=db)