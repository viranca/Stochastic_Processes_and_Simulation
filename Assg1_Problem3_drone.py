# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:22:54 2020

@author: theWissam
"""
import numpy as np
import matplotlib.pyplot as plt

#---------------simulation
# simulate a DTMC with state space and TPM
IT = 0
ITF = 1
means_T2F =[]
while IT<ITF:

    it  = 4
    it1 = 1
    T2F = [] #Time to find intruder
    while it1<it:
        #lambda values, index0 =0 is just a placeholder to make indexing easier such that L[i] is lambda_i.
        L = [0, 0.5, 0.612, 0.707, 0.791, 0.866, 0.935, 1, 1.061]
        
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
            #print('The simulated MC is', X)
            
            
            
            #From the file of the intruder, bring the function that returns the list of rooms and times 
            #of the intruder's visits.
            from Assg1_Problem3_d import Intruderpath
            y= Intruderpath()
            
            #print('intruder path:', y[0])
            # print('drone path: ', Z)
            # print('intruder time:', y[1])
            # print('drone time:', T)
            
            # plt.step(T,Z, 'r')
            # plt.step(y[1],y[0], 'g')
            # plt.ylabel('state')
            # plt.xlabel('time')
            # plt.show()
            
            
            
            # This function calculates the duration of the overlap.
            def getOverlap(a, b):
                    return max(0, min(a[1], b[1]) - max(a[0], b[0]))
            
            #The overlap function is used here to get the duration of time when the drone and intruder
            #are in the same room. It then returns the time when the drone and the intruder entered that room
            def meet():
                for i in range(len(Z)):
                    if Z[i] in y[0]:
                        m = getOverlap([T[i]-1,T[i]],[y[1][y[0].index(Z[i])-1],y[1][y[0].index(Z[i])]])
                        print('m', m, 'i',i, 'room', Z[i], 'drone', T[i]-1, T[i], 'int', y[1][y[0].index(Z[i])-1], y[1][y[0].index(Z[i])])
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
    print('time to find:', T2F, 'meanT2F', np.mean(T2F))
    plt.plot(T2F)
    plt.show()
    means_T2F.append(np.mean(T2F))
    print('means_T2F', means_T2F)
    plt.plot(means_T2F)
    plt.show
    IT +=1
