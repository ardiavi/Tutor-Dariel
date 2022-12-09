from sqlalchemy import Column, Integer, String

#import base dari database.py

from config.database import Base

#intinya ini buat tabell babes

class User_Real(Base): 
    __tablename__ = 'users_real'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    securityquestion = Column(String)
    securityanswer = Column(String)
