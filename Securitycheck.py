# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 19:49:51 2021

@author: theWissam
"""
import numpy as np
import matplotlib.pyplot as plt


lamb = 0.3
Mu = 0.1
pax = list(range(19))
del(pax[0])


leftat=[] #list of times at which pax finished their security check
allWT=[] #list of every waiting time of every pax through all iterations
allmeans =[] #list of the mean waiting time of every iteration

arrivedat =[] #list of times pax arrive to the queue
for i in range(len(pax)):
    arrivedat.append(pax[i]/lamb)
    
it = 2
it0 = 0



while it0<it:
    WT = [0]
    check = [np.random.exponential(scale = 1/Mu)] #Security check duration 
    #1st passenger
    leftat.append(check[0]+arrivedat[0]+WT[0])
    #2nd passenger:
    for i in range(len(pax)-1):
        check.append(np.random.exponential(scale = 1/Mu))
        if leftat[i]>arrivedat[i+1]:
            WT.append(leftat[i]-arrivedat[i+1])
        else:
            WT.append(0)
        leftat.append(check[i+1]+arrivedat[i+1]+WT[i+1])
    
    WTmean = np.mean(WT)
    allWT.append(WT)
    allmeans.append(WTmean)
    print(allWT)
    it0 = it0+1


"""Steps to solve 1f:
    1 - Times to arrive at the queue are pre-determined
    2 - For every passenger, exponentially distributed duration of security check
    3 - For every passenger, the waiting time starts at their arrival, and takes
        into account the previous passenger's security check duration"""

