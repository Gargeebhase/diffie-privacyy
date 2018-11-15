import pandas as pd
import numpy as np
#Attributes = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket,Fare,Cabin,Embarked]
#A_type = [Numerical,Numerical,Numerical,Categorical,Categorical,Numerical,Numerical,Numerical,Categorical,Numerical,Categorical,Categorical]
#target = Survived   

#trainf = train.csv
#testf = test.csv

data_train = pd.read_csv('train.csv')
#abg = int(0)
#ind = 0
 
#for row in data_train:
    #new = data_train['Survived'].astype(float)
    #abg = abg + new
    #ind = ind+1
     
#print(ind)
#print(abg)
#abg = abg/ind 
#print(abg)
n = int(890)
avg = data_train.loc[:,"Survived"].mean(axis=0)
print(avg)
avg = avg + np.random.laplace(0,1.0/(n*0.1))
print(avg)
