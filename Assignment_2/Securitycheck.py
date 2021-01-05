# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 19:49:51 2021

@author: theWissam
"""
import numpy as np
import matplotlib.pyplot as plt


lamb = 0.3
Mu = 0.47 #Vary to find he optimum
allWT=[] #list of every waiting time of every pax through all iterations
allmeans =[] #list of the mean waiting time of every iteration
it = 1000
it0 = 0
CV=[]
within95=[]


while it0<it:
    WT = [0]
    arrivedat =[np.random.exponential(scale = 1/lamb)] #list of times pax arrive to the queue
    for i in range(50): #50 is an arbitrarily high number, since 18 is expected.
        if i!= 0: #the first value is already created
            x = np.random.exponential(scale = 1/lamb)
            y = x+arrivedat[i-1]
            if y <60:  
                arrivedat.append(y)
            else:
                break
            
    leftat=[] #list of times at which pax finished their security check
    check = [np.random.exponential(scale = 1/Mu)] #Security check duration 
    #1st passenger
    leftat.append(check[0]+arrivedat[0]+WT[0])
    #2nd passenger onwards:
    for i in range(len(arrivedat)-1):
        check.append(np.random.exponential(scale = 1/Mu))
        if leftat[i]>arrivedat[i+1]: #if I arrive before the one in front leaves
            WT.append(leftat[i]-arrivedat[i+1]) #add the waiting time until they leave
        else:
            WT.append(0) #my waiting time is 0 if the one in front left before I arrived
        leftat.append(check[i+1]+arrivedat[i+1]+WT[i+1]) #store my leaving time for the next pax calculation
    
    WTmean = np.mean(WT)
    allWT.append(WT)
    allmeans.append(WTmean)
    standard_dev = np.std(allmeans)
    #print(standard_dev)
    meanCV = np.mean(allmeans)
    #print(meanCV)
    CV.append(standard_dev/meanCV)
    within95.append(meanCV + 2*standard_dev)
    it0 = it0+1

#Plot the distribution of waiting times
plt.hist(allmeans, bins=100)

#------- Variance of sample mean
Variance = np.var(allmeans)
print ('Variance: ',Variance)


# #---------------Coefficient of variance--------

#print('CV', CV)
plt.plot(CV)
# plt.title('Security check waiting times with Mu = 0.47')

plt.ylabel('Waiting time [min]')
plt.xlabel('Number of simulations')
       
#Plot the convergence of waiting times 
plt.plot(within95) 
print(within95[-1], 'is within 95')


