import datetime
from typing import Optional, List
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

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

#Schemas For Machine Learning
from .ml.model import n_features
class PredictRequest(BaseModel):
    data: List[List[float]]

    @validator("data")
    def check_dimensionality(cls, v):
        for point in v:
            if len(point) != n_features:
                raise ValueError(f"Each data point must contain {n_features} features")

        return v


class PredictResponse(BaseModel):
    data: List[float]