import datetime

from pydantic import BaseModel

#kayak ngatur bagaimana cara user melihat anuan kita

class BaseUserData(BaseModel):
	username:str
	password:str
	email:str
	secretCombination:int

# Used to get all attibutes from user
class GetUser(BaseUserData):
	id:int
	date_created:datetime.datetime

	class Config:
		orm_mode = True

# Used to show user without password
class ShowUser(BaseModel):
	username:str
	email:str

	class Config:
		orm_mode = True

class Login(BaseModel):
	username:str
	password:str

	class Config:
		orm_mode = True