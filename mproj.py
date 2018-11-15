#It has been proven that even aggregates are not safe. Hence, Dp for India census data
#champai female sc 1
#background information
#first, count of how many dist have female sc one
#the, by excluding districts and finding, eventually will be able to find champai
#if info of every female except one innchampai, the will be able to xdeduce about her

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read dataset
data_train = pd.read_csv('india-districts-census-2011.csv')

#plain count
c_data = (data_train[data_train['Male']>1000000].count()['Population'])
print(c_data) 
c_data = c_data + np.random.laplace(0,1.0/0.1)
print(c_data)

#Male population converted into histograms(buckets) and then compared for various amounts of epsilon
y,binEdges = np.histogram(data_train['Male'],20)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
plt.plot(bincenters,y,'-')
#plt.show()
print(y)
histlap = []
for element in y:
    newele = element + np.random.laplace(0,1.0/0.1)
    histlap.append(newele)
    print(element)
    print(newele)
print(histlap)
plt.plot(bincenters, histlap, '-')
plt.show()

5865078
n = int(640)
p1 = []
p2 = []
for i in data_train['Male']:
    avg = data_train.loc[:,"Male"].mean(axis=0)
    p1.append(avg)
    avg = avg + np.random.laplace(0,5865078.0/(n*0.1))
    p2.append(avg)

plt.plot(p1, p2)
#plt.show()

#Female average comparison
5195070
n = int(640)
avg = data_train.loc[:,"Female"].mean(axis=0)
print(avg)
avg = avg + np.random.laplace(0,1.0/(n*0.1))
print(avg)

                          
