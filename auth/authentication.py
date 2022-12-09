from config.database import SessionLocal
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from SchemaModels import schemas, models
from auth import tokenz
from auth.hashing import Hash
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def authenticate_user(username: str, password: str):
    user = await schemas.BaseUserData.get(username=username)
    if not user:
        return False 
    if not user.verify_password(password):
        return False
    return user 

def login(request:schemas.Login, db:Session = Depends(get_db)):
    user = db.query(models.User_Real).filter(models.User_Real.username == request.username).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Password")
    access_token_expires = timedelta(minutes=tokenz.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = tokenz.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

'''
@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = tokenz.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
'''
