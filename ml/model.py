import joblib
import numpy as np
import  pandas as pd
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score 

class Model:
    def __init__(self, model_path: str = None):
        self._model = None
        self._model_path = model_path
        self.train_data = pd.read_csv('database/train_u6lujuX_CVtuZ9i.csv')
        self.test_data = pd.read_csv('sample.csv') #ganti sesuai dengan upload file gimana
        
        self.load()
    """
    def train(self):
        self.test_data = pd.read_csv('../database/ini_input.csv')
        #bersih data
        #Filling up NAN values of Gender and Converting categorial variables(Male,Female) to numerical variables(0,1)
        self.train_data.Gender = self.train_data.Gender.fillna(self.train_data.Gender.mode())
        self.test_data.Gender = self.test_data.Gender.fillna(self.test_data.Gender.mode())

        sex = pd.get_dummies(self.train_data['Gender'] , drop_first = True )
        self.train_data.drop(['Gender'], axis = 1 , inplace =True)
        self.train_data = pd.concat([self.train_data , sex ] , axis = 1)

        sex = pd.get_dummies(self.test_data['Gender'] , drop_first = True )
        self.test_data.drop(['Gender'], axis = 1 , inplace =True)
        self.test_data = pd.concat([self.test_data , sex ] , axis = 1)

        #Filling up NAN values of Dependents and Converting categorial variables(1,2,3+) to numerical variables(1,2,3)
        self.train_data.Dependents = self.train_data.Dependents.fillna("0")
        self.test_data.Dependents = self.test_data.Dependents.fillna("0")

        rpl = {'0':'0', '1':'1', '2':'2', '3+':'3'}

        self.train_data.Dependents = self.train_data.Dependents.replace(rpl).astype(int)
        self.test_data.Dependents = self.test_data.Dependents.replace(rpl).astype(int)

        #Filling up NAN values of Credit history by taking the mode
        self.train_data.Credit_History = self.train_data.Credit_History.fillna(self.train_data.Credit_History.mode()[0])
        self.train_data.Credit_History  = self.train_data.Credit_History.fillna(self.train_data.Credit_History.mode()[0])

        #Filling Self Employed NAN values and Converting categorial variables(Yes,No) to numerical variables(1,0)
        self.train_data.Self_Employed = self.train_data.Self_Employed.fillna(self.train_data.Self_Employed.mode())
        self.test_data.Self_Employed = self.test_data.Self_Employed.fillna(self.test_data.Self_Employed.mode())

        Self_Employed = pd.get_dummies(self.train_data['Self_Employed'] , prefix = 'Self_Employed',drop_first = True )
        self.train_data.drop(['Self_Employed'], axis = 1 , inplace =True)
        self.train_data = pd.concat([self.train_data , Self_Employed ] , axis = 1)

        Self_Employed = pd.get_dummies(self.test_data['Self_Employed'] , prefix = 'Self_Employed', drop_first = True )
        self.test_data.drop(['Self_Employed'], axis = 1 , inplace =True)
        self.test_data = pd.concat([self.test_data , Self_Employed ] , axis = 1)

        #Filling Married NAN values and Converting categorial variables(Yes,No) to numerical variables(1,0)
        self.train_data.Married = self.train_data.Married.fillna(self.train_data.Married.mode())
        self.test_data.Married = self.test_data.Married.fillna(self.test_data.Married.mode())

        married = pd.get_dummies(self.train_data['Married'] , prefix = 'married',drop_first = True )
        self.train_data.drop(['Married'], axis = 1 , inplace =True)
        self.train_data = pd.concat([self.train_data , married ] , axis = 1)

        married = pd.get_dummies(self.test_data['Married'] , prefix = 'married', drop_first = True )
        self.test_data.drop(['Married'], axis = 1 , inplace =True)
        self.test_data = pd.concat([self.test_data , married ] , axis = 1) 
        
        #Filling up NAN values of Loan Amount Term
        
        self.train_data.drop(['Loan_Amount_Term'], axis = 1 , inplace =True)
        self.test_data.drop(['Loan_Amount_Term'], axis = 1 , inplace =True)

        self.train_data.LoanAmount = self.train_data.LoanAmount.fillna(self.train_data.LoanAmount.mean()).astype(int)
        self.test_data.LoanAmount = self.test_data.LoanAmount.fillna(self.test_data.LoanAmount.mean()).astype(int)

        #Converting categorial variables to numerical variables¶
        self.train_data['Education'] = self.train_data['Education'].map( {'Graduate': 0, 'Not Graduate': 1} ).astype(int)
        self.test_data['Education'] = self.test_data['Education'].map( {'Graduate': 0, 'Not Graduate': 1} ).astype(int)

        #Converting categorial variables to numerical variables
        self.train_data['Property_Area'] = self.train_data['Property_Area'].map( {'Urban': 0, 'Semiurban': 1 ,'Rural': 2  } ).astype(int)

        self.test_data.Property_Area = self.test_data.Property_Area.fillna(self.test_data.Property_Area.mode())
        self.test_data['Property_Area'] = self.test_data['Property_Area'].map( {'Urban': 0, 'Semiurban': 1 ,'Rural': 2  } ).astype(int)

        #Target Variable : Loan Status (Converting categorial variables to numerical variables)
        self.train_data['Loan_Status'] = self.train_data['Loan_Status'].map( {'N': 0, 'Y': 1 } ).astype(int)

        #Dropping the ID column
        self.train_data.drop(['Loan_ID'], axis = 1 , inplace =True)
        #training nich babes
        X = self.train_data.drop('Loan_Status' , axis = 1 )
        y = self.train_data['Loan_Status']
        X_train ,X_test , y_train , y_test = train_test_split(X , y , test_size = 0.3 , random_state =102)
        logmodel = LogisticRegression()
        logmodel.fit(X_train , y_train)
        pred_l = logmodel.predict(X_test)
        return accuracy_score(y_test , pred_l)*100
    """
    

    def predict(self):
        self.train_data = pd.read_csv('database/train_u6lujuX_CVtuZ9i.csv')
        self.test_data = pd.read_csv('sample.csv') #ganti sesuai dengan upload file gimana
        #Upload and Open File Sample
        #Open FIle Sample yang udah ada
                #bersih data
        #Filling up NAN values of Gender and Converting categorial variables(Male,Female) to numerical variables(0,1)
        self.train_data.Gender = self.train_data.Gender.fillna(self.train_data.Gender.mode())
        self.test_data.Gender = self.test_data.Gender.fillna(self.test_data.Gender.mode())

        sex = pd.get_dummies(self.train_data['Gender'] , drop_first = True )
        self.train_data.drop(['Gender'], axis = 1 , inplace =True)
        self.train_data = pd.concat([self.train_data , sex ] , axis = 1)

        sex = pd.get_dummies(self.test_data['Gender'] , drop_first = True )
        self.test_data.drop(['Gender'], axis = 1 , inplace =True)
        self.test_data = pd.concat([self.test_data , sex ] , axis = 1)

        #Filling up NAN values of Dependents and Converting categorial variables(1,2,3+) to numerical variables(1,2,3)
        self.train_data.Dependents = self.train_data.Dependents.fillna("0")
        self.test_data.Dependents = self.test_data.Dependents.fillna("0")

        rpl = {'0':'0', '1':'1', '2':'2', '3+':'3'}

        self.train_data.Dependents = self.train_data.Dependents.replace(rpl).astype(int)
        self.test_data.Dependents = self.test_data.Dependents.replace(rpl).astype(int)

        #Filling up NAN values of Credit history by taking the mode
        self.train_data.Credit_History = self.train_data.Credit_History.fillna(self.train_data.Credit_History.mode()[0])
        self.test_data.Credit_History  = self.test_data.Credit_History.fillna(self.test_data.Credit_History.mode()[0])

        #Filling Self Employed NAN values and Converting categorial variables(Yes,No) to numerical variables(1,0)
        self.train_data.Self_Employed = self.train_data.Self_Employed.fillna(self.train_data.Self_Employed.mode())
        self.test_data.Self_Employed = self.test_data.Self_Employed.fillna(self.test_data.Self_Employed.mode())

        Self_Employed = pd.get_dummies(self.train_data['Self_Employed'] , prefix = 'Self_Employed',drop_first = True )
        self.train_data.drop(['Self_Employed'], axis = 1 , inplace =True)
        self.train_data = pd.concat([self.train_data , Self_Employed ] , axis = 1)

        Self_Employed = pd.get_dummies(self.test_data['Self_Employed'] , prefix = 'Self_Employed', drop_first = True )
        self.test_data.drop(['Self_Employed'], axis = 1 , inplace =True)
        self.test_data = pd.concat([self.test_data , Self_Employed ] , axis = 1)

        #Filling Married NAN values and Converting categorial variables(Yes,No) to numerical variables(1,0)
        self.train_data.Married = self.train_data.Married.fillna(self.train_data.Married.mode())
        self.test_data.Married = self.test_data.Married.fillna(self.test_data.Married.mode())

        married = pd.get_dummies(self.train_data['Married'] , prefix = 'married',drop_first = True )
        self.train_data.drop(['Married'], axis = 1 , inplace =True)
        self.train_data = pd.concat([self.train_data , married ] , axis = 1)

        married = pd.get_dummies(self.test_data['Married'] , prefix = 'married', drop_first = True )
        self.test_data.drop(['Married'], axis = 1 , inplace =True)
        self.test_data = pd.concat([self.test_data , married ] , axis = 1) 
        
        #Filling up NAN values of Loan Amount Term
        
        self.train_data.drop(['Loan_Amount_Term'], axis = 1 , inplace =True)
        self.test_data.drop(['Loan_Amount_Term'], axis = 1 , inplace =True)

        self.train_data.LoanAmount = self.train_data.LoanAmount.fillna(self.train_data.LoanAmount.mean()).astype(int)
        self.test_data.LoanAmount = self.test_data.LoanAmount.fillna(self.test_data.LoanAmount.mean()).astype(int)

        #Converting categorial variables to numerical variables¶
        self.train_data['Education'] = self.train_data['Education'].map( {'Graduate': 0, 'Not Graduate': 1} ).astype(int)
        self.test_data['Education'] = self.test_data['Education'].map( {'Graduate': 0, 'Not Graduate': 1} ).astype(int)

        #Converting categorial variables to numerical variables
        self.train_data['Property_Area'] = self.train_data['Property_Area'].map( {'Urban': 0, 'Semiurban': 1 ,'Rural': 2  } ).astype(int)

        self.test_data.Property_Area = self.test_data.Property_Area.fillna(self.test_data.Property_Area.mode())
        self.test_data['Property_Area'] = self.test_data['Property_Area'].map( {'Urban': 0, 'Semiurban': 1 ,'Rural': 2  } ).astype(int)

        #Target Variable : Loan Status (Converting categorial variables to numerical variables)
        self.train_data['Loan_Status'] = self.train_data['Loan_Status'].map( {'N': 0, 'Y': 1 } ).astype(int)

        #Dropping the ID column
        self.train_data.drop(['Loan_ID'], axis = 1 , inplace =True)
        #training nich babes
        X = self.train_data.drop('Loan_Status' , axis = 1 )
        y = self.train_data['Loan_Status']
        X_train ,X_test , y_train , y_test = train_test_split(X , y , test_size = 0.3 , random_state =102)
        logmodel = LogisticRegression()
        logmodel.fit(X_train , y_train)
        joblib.dump(logmodel, "train_model.joblib")
        logmodel.predict(X_test)

        

        df_test = self.test_data.drop(['Loan_ID'], axis = 1)

        p_log = logmodel.predict(df_test)
        submission = pd.DataFrame({
                "Loan_ID": self.test_data["Loan_ID"],
                "Loan_Status": p_log
            })

        submission.to_csv("results.csv", encoding='utf-8', index=False)
        a = "done"
        return a
    def save(self):
        if self._model is not None:
            joblib.dump(self._model, self._model_path)
        else:
            raise TypeError("The model is not trained yet, use .train() before saving")

    def load(self):
        try:
            self._model = joblib.load(self._model_path)
        except:
            self._model = None
        return self



model_path = Path(__file__).parent / "model.joblib"
model_obj = Model(model_path)
n_features = 12
#print(model.predict())
def get_model():
    return model



#if __name__ == "__main__":
    #X, y = load_boston(return_X_y=True)
    #model.train(X, y)
    #model.save()