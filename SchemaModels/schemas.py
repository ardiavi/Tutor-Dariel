import datetime
from typing import Optional, List
from pydantic import BaseModel



class BaseUserData(BaseModel):
	username:str
	password:str
	email:str
	securityquestion:str
	securityanswer:str

# Used to get all attibutes from user
class GetUser(BaseUserData):
	id:int
	date_created:datetime.datetime

	class Config:
		orm_mode = True

# Used to show user without password
class ShowUser(BaseModel):
	id:int
	username:str
	email:str
	securityquestion:str

	class Config:
		orm_mode = True

class Login(BaseModel):
	username:str
	password:str

	class Config:
		orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None


class LenderData(BaseModel):
	Name : str
	Dependents : int
	Education : int
	ApplicantIncome : int
	CoapplicantIncome : float
	LoanAmount : int
	Credit_History : float
	Property_Area : int
	Male : int
	Self_Employed_Yes : int
	married_Yes : int