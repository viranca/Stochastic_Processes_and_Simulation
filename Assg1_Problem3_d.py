# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:13:42 2020

@author: theWissam
"""
import numpy as np
import matplotlib.pyplot as plt
#---------------simulation
# simulate a DTMC with state space and TPM
def Intruderpath():
    
    it  = 9
    it1 = 1
    
    #lambda values, index0 =0 is just a placeholder to make indexing easier such that L[i] is lambda_i.
    L = [0, 0.5, 0.612, 0.707, 0.791, 0.866, 0.935, 1, 1.061]
        
    T = [] #list of time stamps at every jump
    X = [] #list of states(rooms) visited by intruder
    S = [] #list of times spent in each state
    #initialize the chain X_0 = 1
    current_state = 1
    t = 0
    while it1<it:
        while t<100:
            
            #Draw omega
            omega = np.random.uniform(0,1)
    
            #check current
            if current_state == 1:
                X.append(current_state)
                #Draw exponential random variable
                S1 = np.random.exponential(scale = 1/L[1])
                
                #Store this sojourn time in S list
                S.append(S1)
                
                #Update to time when leaving this state
                t = t + S1
                
                #Store jump time in T list
                T.append(t)
                
                #give new state, and add it to X list
                current_state = 4
                
                
            elif current_state ==2:
                X.append(current_state)
                #Draw exponential random variable
                S2 = np.random.exponential(scale = 1/L[2])
                
                #Store this sojourn time in S list
                S.append(S2)
                
                #Update to time when leaving this state
                t = t + S2
        
                #Store jump time in T list
                T.append(t)
            
                #give new state, and add it to X list
                if omega<=0.5:
                    current_state = 3
                else:
                    current_state = 5
    
                
            elif current_state == 3:
                X.append(current_state)
                #Draw exponential random variable
                S3 = np.random.exponential(scale = 1/L[3])
                
                #Store this sojourn time in S list
                S.append(S3)
                
                #Update to time when leaving this state
                t = t + S3
                
                #Store jump time in T list
                T.append(t)
                
                #give new state, and add it to X list
                if omega<=0.5:
                    current_state = 2
                else:
                    current_state = 6
    
                    
            elif current_state == 4:
                X.append(current_state)
                
                #Draw exponential random variable
                S4 = np.random.exponential(scale = 1/L[4])
                
                #Store this sojourn time in S list
                S.append(S4)
        
                #Update to time when leaving this state
                t = t + S4
            
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
                X.append(current_state)
                #Draw exponential random variable
                S5 = np.random.exponential(scale = 1/L[5])
                
                #Store this sojourn time in S list
                S.append(S5)
                
                #Update to time when leaving this state
                t = t + S5
                
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
                X.append(current_state)
                
                #Draw exponential random variable
                S6 = np.random.exponential(scale = 1/L[6])
                
                #Store this sojourn time in S list
                S.append(S6)
                
                #Update to time when leaving this state
                t = t + S6
                
                #Store jump time in T list
                T.append(t)
                
                #give new state, and add it to X list
                current_state = 3
    
                
            elif current_state == 7:
                X.append(current_state)
                #Draw exponential random variable
                S7 = np.random.exponential(scale = 1/L[7])
                
                #Store this sojourn time in S list
                S.append(S7)
                
                #Update to time when leaving this state
                t = t + S7
                
                #Store jump time in T list
                T.append(t)
                
                #give new state, and add it to X list
                if omega<=0.5:
                    current_state = 4
    
                else:
                    current_state = 8
    
                    
            elif current_state == 8:
                X.append(current_state)
                #Draw exponential random variable
                S8 = np.random.exponential(scale = 1/L[8])
                
                #Store this sojourn time in S list
                S.append(S8)
                
                #Update to time when leaving this state
                t = t + S8
                
                #Store jump time in T list
                T.append(t)
                
                #give new state, and add it to X list
                if omega<=0.5:
                    current_state = 5
    
                else:
                    current_state = 7
                    
            X = list(X)
            #print('The simulated MC is', X)
            it1 = it1 +1
        # plt.step(T,X)
        # plt.ylabel('state')
        # plt.xlabel('time')
        # plt.show()
        return X,T,S
        
# print(X)
# print(T)
# print(S)

y= Intruderpath()
