# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:32:43 2021

@author: theWissam
"""
import numpy as np
import matplotlib.pyplot as plt


lamb = 0.3
Mu = 0.4
pax = list(range(19))
del(pax[0])



allWT=[] #list of every waiting time of every pax through all iterations
allmeans =[] #list of the mean waiting time of every iteration
allQ=[] #List of lengths of Q every time a passenger arrives
allmeansfrac =[]
    
it = 1000
it0 = 0

fractions = []
CV=[]
within95=[]
while it0<it:
    WT = [0]
    arrivedat =[np.random.exponential(scale = 1/lamb)] #list of times pax arrive to the queue
    for i in range(50):
        if i!= 0:
            x = np.random.exponential(scale = 1/lamb)
            y = x+arrivedat[i-1]
            if y <60:  
                arrivedat.append(y)
            else:
                break
            
    leftat=[] #list of times at which pax finished their security check
    check = [np.random.exponential(scale = 1/Mu)] #Security check duration 
    Q = [0]*len(arrivedat)
    #1st passenger
    leftat.append(check[0]+arrivedat[0]+WT[0])
    #2nd passenger:
    for i in range(len(arrivedat)-1):
        check.append(np.random.exponential(scale = 1/Mu))
        if leftat[i]>arrivedat[i+1]:
            WT.append(leftat[i]-arrivedat[i+1])
        else:
            WT.append(0)
        leftat.append(check[i+1]+arrivedat[i+1]+WT[i+1])
        
        
    for i in range(len(arrivedat)):
        for j in range(len(arrivedat)):
            if arrivedat[i]>arrivedat[j]:
                if leftat[j]>arrivedat[i]:
                    Q[i]+=1
    
    fractions.append(sum(k>7 for k in Q)/len(Q))
    fracmean = np.mean(fractions)
    allmeansfrac.append(fracmean)
    
    allQ.append(Q)
    WTmean = np.mean(WT)
    allWT.append(WT)
    allmeans.append(WTmean)
    standard_dev = np.std(allmeansfrac)
    #print(standard_dev)
    meanCV = np.mean(allmeansfrac)
    #print(meanCV)
    CV.append(standard_dev/meanCV)
    within95.append(meanCV + 2*standard_dev)
    it0 = it0+1

plt.hist(allQ)
plt.title('Distribution of number of passengers in the queue')
plt.xlabel('Number of passengers in the queue')
plt.ylabel('Number of occurences')
plt.show()
# plt.hist(allQ, 100, density=True, facecolor='b', alpha=0.8)
#------- Variance of sample mean
Variance = np.var(allmeansfrac)
#print ('Variance: ',Variance)


# #---------------Coefficient of variance--------

#print('CV', CV)
plt.plot(CV)
plt.title('Coefficient of variance for queue length simulations')

plt.xlabel('Number of simulations')
plt.ylabel('Coefficient of variance')
plt.show()
        
        
#print(within95[-1], 'is within 95')


