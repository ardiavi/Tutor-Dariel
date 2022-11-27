from sqlalchemy import Column, Integer, String

#import base dari database.py
# terus masukin si base sebagaai parent inget inheritance oop
# si usert child, base itu parent

from database import Base

#intinya ini buat tabell babes

class User(Base): 
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    secretCombination = Column(Integer)