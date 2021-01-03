from matplotlib import pyplot as plt
import statistics
import numpy as np


#part B

#define input matrices A, B, C and V:
A = np.array([[1, 1],   
              [0, 1]])

B = np.array([[0.1],
              [0.5]])

C = np.array([1, 0])

V = np.array([0, 0])

#number of monte carlo iterations:
MC_n = 1000
t_list = []
for MC_i in range(MC_n):
    X_t = np.array([[0, 0], [0, 0]]) 
    Y_t = 0
    t = 0
    #constraint that checks and stops the time when Y_t is larger or equal to 1000.
    while Y_t < 1000: 
        #draw new random variables at every timestep t!
        e = np.random.normal(0, 0.1)     
        V[0] = np.random.normal(0, 1)
        V[1] = np.random.normal(0, 1)      
        
        #compute X_t+1 at every timestep t
        X_tplusone = A * X_t + B + V
        
        #compute Y_t at every timestep t        
        Y_t = C * X_t + e   
        Y_t = Y_t[0][0]
        
        #Move on to the next timestep t
        X_t = X_tplusone
        t = t + 1
    #add the result of this monte carlo iteration to the list of all the results
    t_list.append(t)

#print the average result over all the monte carlo iterations
print(statistics.mean(t_list))    




#%%

#Checking part A
V = np.array([0, 0])
X_3_1 = []
X_3_2 = []
X_3_3 = []
X_3_4 = []

for i in range(100000):
    X_t = np.array([0, 0]) 
    
    #add the timestep here:
    for t in range(5):
        #draw new random variables at every timestep t!
        V[0] = np.random.normal(0, 1)
        V[1] = np.random.normal(0, 1) 
        
        #compute X_t+1 at every timestep t
        X_tplusone = A * X_t + B + V
        
        #Move on to the next timestep t
        X_t = X_tplusone
        X_3_1.append(X_t[0][0])
        X_3_2.append(X_t[0][1])
        X_3_3.append(X_t[1][0])
        X_3_4.append(X_t[1][1])
   
        
print(statistics.mean(X_3_1))
print(statistics.mean(X_3_2))
print(statistics.mean(X_3_3))
print(statistics.mean(X_3_4))
#%%
print(A*A *B + A * B + B)

print(A * B + B)













