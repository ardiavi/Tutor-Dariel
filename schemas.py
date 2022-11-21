import datetime

from pydantic import BaseModel

#kayak ngatur bagaimana cara user melihat anuan kita

class BaseUser(BaseModel):
	username:str
	password:str
	email:str

# Used to get all attibutes from user
class GetUser(BaseUser):
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