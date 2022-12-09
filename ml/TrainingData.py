import joblib
import numpy as np
import  pandas as pd
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score 
        
train = pd.read_csv('../database/train_u6lujuX_CVtuZ9i.csv')
test = pd.read_csv('../database/train_u6lujuX_CVtuZ9i.csv') #ganti sesuai dengan upload file gimana
#Upload and Open File Sample
#Open FIle Sample yang udah ada
        #bersih data
#Filling up NAN values of Gender and Converting categorial variables(Male,Female) to numerical variables(0,1)
train.Gender = train.Gender.fillna(train.Gender.mode())
test.Gender = test.Gender.fillna(test.Gender.mode())

sex = pd.get_dummies(train['Gender'] , drop_first = True )
train.drop(['Gender'], axis = 1 , inplace =True)
train = pd.concat([train , sex ] , axis = 1)

sex = pd.get_dummies(test['Gender'] , drop_first = True )
test.drop(['Gender'], axis = 1 , inplace =True)
test = pd.concat([test , sex ] , axis = 1)

#Filling up NAN values of Dependents and Converting categorial variables(1,2,3+) to numerical variables(1,2,3)
train.Dependents = train.Dependents.fillna("0")
test.Dependents = test.Dependents.fillna("0")

rpl = {'0':'0', '1':'1', '2':'2', '3+':'3'}

train.Dependents = train.Dependents.replace(rpl).astype(int)
test.Dependents = test.Dependents.replace(rpl).astype(int)

#Filling up NAN values of Credit history by taking the mode
train.Credit_History = train.Credit_History.fillna(train.Credit_History.mode()[0])
test.Credit_History  = test.Credit_History.fillna(test.Credit_History.mode()[0])

#Filling Self Employed NAN values and Converting categorial variables(Yes,No) to numerical variables(1,0)
train.Self_Employed = train.Self_Employed.fillna(train.Self_Employed.mode())
test.Self_Employed = test.Self_Employed.fillna(test.Self_Employed.mode())

Self_Employed = pd.get_dummies(train['Self_Employed'] , prefix = 'Self_Employed',drop_first = True )
train.drop(['Self_Employed'], axis = 1 , inplace =True)
train = pd.concat([train , Self_Employed ] , axis = 1)

Self_Employed = pd.get_dummies(test['Self_Employed'] , prefix = 'Self_Employed', drop_first = True )
test.drop(['Self_Employed'], axis = 1 , inplace =True)
test = pd.concat([test , Self_Employed ] , axis = 1)

#Filling Married NAN values and Converting categorial variables(Yes,No) to numerical variables(1,0)
train.Married = train.Married.fillna(train.Married.mode())
test.Married = test.Married.fillna(test.Married.mode())

married = pd.get_dummies(train['Married'] , prefix = 'married',drop_first = True )
train.drop(['Married'], axis = 1 , inplace =True)
train = pd.concat([train , married ] , axis = 1)

married = pd.get_dummies(test['Married'] , prefix = 'married', drop_first = True )
test.drop(['Married'], axis = 1 , inplace =True)
test = pd.concat([test , married ] , axis = 1) 

#Filling up NAN values of Loan Amount Term

train.drop(['Loan_Amount_Term'], axis = 1 , inplace =True)
test.drop(['Loan_Amount_Term'], axis = 1 , inplace =True)

train.LoanAmount = train.LoanAmount.fillna(train.LoanAmount.mean()).astype(int)
test.LoanAmount = test.LoanAmount.fillna(test.LoanAmount.mean()).astype(int)

#Converting categorial variables to numerical variables¶
train['Education'] = train['Education'].map( {'Graduate': 0, 'Not Graduate': 1} ).astype(int)
test['Education'] = test['Education'].map( {'Graduate': 0, 'Not Graduate': 1} ).astype(int)

#Converting categorial variables to numerical variables
train['Property_Area'] = train['Property_Area'].map( {'Urban': 0, 'Semiurban': 1 ,'Rural': 2  } ).astype(int)

test.Property_Area = test.Property_Area.fillna(test.Property_Area.mode())
test['Property_Area'] = test['Property_Area'].map( {'Urban': 0, 'Semiurban': 1 ,'Rural': 2  } ).astype(int)

#Target Variable : Loan Status (Converting categorial variables to numerical variables)
train['Loan_Status'] = train['Loan_Status'].map( {'N': 0, 'Y': 1 } ).astype(int)

#Dropping the ID column
train.drop(['Loan_ID'], axis = 1 , inplace =True)
#training nich babes
X = train.drop('Loan_Status' , axis = 1 )
y = train['Loan_Status']
X_train ,X_test , y_train , y_test = train_test_split(X , y , test_size = 0.3 , random_state =102)
logmodel = LogisticRegression()
logmodel.fit(X_train , y_train)

print(train.dtypes)
joblib.dump(logmodel, "train_model.joblib")