# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:22:54 2020

@author: theWissam
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#---------------simulation
# simulate a DTMC with state space and TPM
IT = 0
ITF = 1
means_T2F =[]
while IT<ITF:

    it  = 300
    it1 = 1
    T2F = [] #Time to find intruder
    while it1<it:
        
        T = [] #list of time stamps at every jump
        Z = [] #list of states(rooms) visited by drone
        S = [] #list of times spent in each state
        #initialize the chain X_0 = 1
        current_state = 8
        t = 0
    
        while t<20:
    
            #Draw omega
            omega = np.random.uniform(0,1)
    
            #check current
            if current_state == 1:
                Z.append(current_state)
                
                #Update to time when leaving this state
                t = t + 1
                
                #Store jump time in T list
                T.append(t)
                
                #give new state, and add it to X list
                current_state = 4
                
                
            elif current_state ==2:
                Z.append(current_state)
    
                
                #Update to time when leaving this state
                t = t + 1
        
                #Store jump time in T list
                T.append(t)
            
                #give new state, and add it to X list
                if omega<=0.5:
                    current_state = 3
                else:
                    current_state = 5
    
                
            elif current_state == 3:
                Z.append(current_state)
                
                #Update to time when leaving this state
                t = t + 1
                
                #Store jump time in T list
                T.append(t)
                
                #give new state, and add it to X list
                if omega<=0.5:
                    current_state = 2
                else:
                    current_state = 6
    
                    
            elif current_state == 4:
                Z.append(current_state)
    
                #Update to time when leaving this state
                t = t + 1
            
                #Store jump time in T list
                T.append(t)
            
                #give new state, and add it to X list
                if omega<=1/3:
                    current_state = 1
                elif omega<=2/3:
                    current_state = 5
                else:
                    current_state = 7
    
            
            elif current_state ==5:
                Z.append(current_state)
    
                #Update to time when leaving this state
                t = t + 1
                
                #Store jump time in T list
                T.append(t)
                
                #give new state, and add it to X list
                if omega<=1/3:
                    current_state = 2
    
                elif omega<=2/3:
                    current_state = 4
                else:
                    current_state = 8
    
                        
            elif current_state == 6:
                Z.append(current_state)
                
                #Update to time when leaving this state
                t = t + 1
                
                #Store jump time in T list
                T.append(t)
                
                #give new state, and add it to X list
                current_state = 3
    
                
            elif current_state == 7:
                Z.append(current_state)
                #Update to time when leaving this state
                t = t + 1
                
                #Store jump time in T list
                T.append(t)
                
                #give new state, and add it to X list
                if omega<=0.5:
                    current_state = 4
    
                else:
                    current_state = 8
    
                    
            elif current_state == 8:
                Z.append(current_state)
    
                #Update to time when leaving this state
                t = t + 1
                
                #Store jump time in T list
                T.append(t)
                
                #give new state, and add it to X list
                if omega<=0.5:
                    current_state = 5
    
                else:
                    current_state = 7
                    
            Z = list(Z)
            #-----------This is to overwrite Z and test Strategy 2
            """for i in range(len(Z)):
                if i ==0:
                    Z[i] = 8
                elif i == 1 or i ==6 or i ==7 or i==12 or i==13 or i ==18 or i==19:
                    Z[i] = 5
                elif i==2 or i==5 or i==8 or i==11 or i==14 or i==17:
                    Z[i]=4
                else:
                    Z[i]=7"""
                    
            #-----------Thisis to overwrite Z and test Strategy 3
            """for i in range(len(Z)):
                if i ==0:
                    Z[i] = 8
                elif i==2 or i==6:
                    Z[i]=2
                elif i==3 or i==5:
                    Z[i]=3
                elif i==4:
                    Z[i] = 6
                else:
                    Z[i] = 5"""
            
            
            #From the file of the intruder, bring the function that returns the list of rooms and times 
            #of the intruder's visits.
            from Assg1_Problem3_e import Intruderpath
            y= Intruderpath()
            
            
            #Plot step function showing the overlap of drone and intruder paths
            """ plt.step(T,Z, 'r',label='Drone path')
            # plt.step(y[1],y[0], 'g', label='Intruder path')
            # plt.ylabel('state')
            # plt.xlabel('time(s)')
            # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
            # plt.show()"""
            
            
            
            # This function calculates the duration of the overlap.
            def getOverlap(a, b):
                    return max(0, min(a[1], b[1]) - max(a[0], b[0]))
            

            #The overlap function is used here to get the duration of time when the drone and intruder
            #are in the same room. It then returns the time when the drone and the intruder entered that room
            def meet():
                for i in range(len(Z)):
                    if Z[i] in y[0]:
                        m = getOverlap([T[i]-1,T[i]],[y[1][y[0].index(Z[i])-1],y[1][y[0].index(Z[i])]])
                        #print('m', m, 'i',i, 'room', Z[i], 'drone', T[i]-1, T[i], 'int', y[1][y[0].index(Z[i])-1], y[1][y[0].index(Z[i])])
                        if m>0:
                            break    
                        
                return T[i]-1, y[1][y[0].index(Z[i])-1],m
            
            enter_time = meet()
            D_enter = enter_time[0]
            I_enter = enter_time[1]
            
            #Here, after determining the room and time range they meet within, the moment in time that 
            #they first meet is determined. If the drone enters first, the moment is the entrance of the intruder, 
            #if the intruder enters first, the moment is the entrance of the drone. This is all given
            #that they do meet in that room within those time intervals. 
            if D_enter < I_enter:
                  T2F.append(I_enter)
            else:
                T2F.append(D_enter) 
    
        it1 = it1 +1
        means_T2F.append(np.mean(T2F))
    IT +=1
    
    
print('time to find:', T2F, 'meanT2F', np.mean(T2F))
T2F_order = sorted(T2F)
plt.plot(T2F_order)
plt.ylabel('time until meeting')
plt.xlabel('number of simulation run')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()

print('means_T2F', means_T2F)
plt.plot(means_T2F)
plt.ylabel('Mean time until meeting')
plt.xlabel('number of simulations')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show

#------- Variance of sample mean
Variance = np.var(means_T2F)
print ('Variance: ',Variance)


#---------------Coefficient of variance--------
standard_dev = np.std(means_T2F)
print(standard_dev)
meanCV = np.mean(means_T2F)
print(meanCV)
CV = standard_dev/meanCV
print('CV', CV)
rooms_intruder = []
for i in range(1,9):
    rooms_intruder.append(y[0].count(i))
    