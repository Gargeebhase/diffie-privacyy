import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.nan)

import matplotlib.pyplot as plt
from numpy import random

data_train = pd.read_csv('newcsv.csv') 
#print(data_train.head())
newd = data_train.groupby(['Destination']).count()
newnd = newd.add_suffix('_Count').reset_index()
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #print(newnd)
#newnd.to_csv('save_karlo', sep='\t')
#  Destination  No._Count  Time_Count  Source_Count  Protocol_Count  \  Length_Count  Info_Count  
sum = int(0)
for ele in newnd['No._Count']:
    sum = sum + int(ele)

sampled = random.choice(newnd['Destination'], p = newnd['No._Count']/sum, size = 10000)
print(sampled)
