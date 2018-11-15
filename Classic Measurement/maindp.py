import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.nan)

import matplotlib.pyplot as plt
from numpy import random
import bisect

#def weighted_choice(weights):
    #totals = []
    #running_total = 0

    #for w in weights:
        #running_total += w
        #totals.append(running_total)

    #rnd = random.random() * running_total
    #for i, total in enumerate(totals):
        #if rnd < total:
            #return i

def weighted_choice(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    return bisect.bisect_right(totals, rnd)

#def weighted_choice(weights):
    #rnd = random.random() * sum(weights)
    #for i, w in enumerate(weights):
        #rnd -= w
        #if rnd < 0:
            #return i

data_train = pd.read_csv('newcsv.csv') 
newd = data_train.groupby(['Destination']).count()
newnd = newd.add_suffix('_Count').reset_index()
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #print(newnd)
#newnd.to_csv('save_karlo', sep='\t')
#  Destination  No._Count  Time_Count  Source_Count  Protocol_Count  \  Length_Count  Info_Count  

here = []
now = []
for ele in newnd['No._Count']:
    now.append(int(ele) + np.random.laplace(0,1.0/0.9))
#print(now)

sum1 = float(0)
for ele in now:
    if ele>0:
        sum1 = sum1 + float(ele)
non = []
for ele in now:
    if ele<0:
        non.append(float(0))
    else:
        non.append(ele/sum1)

sampled = random.choice(newnd['Destination'], p = non, size = 10000)
print(sampled)

#fin = []
#for i in range(1, 10000):
    #this = weighted_choice(now)
    #fin.append(newnd['No._Count'][this])

#print(fin)
