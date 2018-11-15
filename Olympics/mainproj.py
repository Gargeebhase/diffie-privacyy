import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read dataset
data_train = pd.read_csv('athlete_events.csv') 

def letsplot( ep):
    y,binEdges = np.histogram(data_train['Height'],20,range=(127.0,226.0))
    bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
    plt.plot(bincenters,y,'-')
    #plt.show()
    print(y)
    histlap = []
    for element in y:
        newele = element + np.random.laplace(0,1.0/ep)
        histlap.append(newele)
        print(element)
        print(newele)
    print(histlap)
    plt.plot(bincenters, histlap, '-')
    plt.show()

letsplot(0.1)
