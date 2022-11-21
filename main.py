from fastapi import FastAPI, Depends

from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
import schemas
import models

import uvicorn
#

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#migrate database
def migrate_table():
    return models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post('/user')
def create_user(user : schemas.BaseUser, db:Session = Depends(get_db)):
    new_user = models.User(**user.dict()) #manualnya (user.name = username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user', response_model=List[schemas.ShowUser])
def get_dummy(db: Session = Depends(get_db)):
    return db.query(models.User).all()
     #ini kyk contoh aja intinya bikin fungsi ada return

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload= True)
    '''
    uvicorn.run ini kalo misalkan kalian langsung run program
    main.py, program fastapi langsung jalan di terminal tinggal ketik python
    '''