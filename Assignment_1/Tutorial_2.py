# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:23:19 2020

@author: wsm92
"""
import numpy as np
X = [0, 1, 2, 3, 4, 5, 6]


"""b) 
1: 0      0    1   0      0   0
2: 0      0    1   0      0   0
3: 0.25  0.25  0  0.25  0.25  0   
4: 0      0    1   0      0   0
5: 0      0    0.5 0      0   0.5
6: 0      0    0   0      1   0 """
current_room = X[1]

T4=[]
for i in range (1,1000):
    chain= []
    for t in range (1,3):
        n = np.random.uniform(0,1)
        if current_room == X[1]:
            if n<=1:
                current_room = X[3]
                
        elif current_room == X[2]:
            if n<=1:
                current_room = X[3]
                
        elif current_room == X[3]:
            if n<=0.25:
                current_room  = X[1]
            elif n<=0.5:
                current_room = X[2]
            elif n<=0.75:
                current_room = X[4]
            else:
                current_room = X[5]
                
        elif current_room == X[4]:
            if n<=1:
                current_room = X[3]
                
        elif current_room == X[5]:
            if n<=0.5:
                current_room = X[3]
            else:
                current_room = X[6]
                
        else:
            current_room = X[5]
            
        chain.append(current_room)
    T4.append(chain[1])


print(chain)
print(T4)
# occurences = [sum(T4 == 1), sum(T4==2), sum(T4==3), sum(T4==4), sum(T4==5), sum(T4==6)]
# print(occurences)

