# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:33:28 2020

@author: theWissam
"""
import numpy as np
P = np.array([[0,      0,  0,   1,    0,  0, 0, 0],
              [0,      0,  0.5,   0,    0.5,  0, 0 , 0],
              [0, 0.5, 0, 0, 0, 0.5, 0, 0],
              [1/3,      0,  0,   0,    1/3,  0, 1/3, 0],
              [0,      1/3,  0, 1/3,    0,  0,0, 1/3],
              [0,      0,  1,   0,    0,  0, 0 ,0],
              [0,0,0,0.5,0,0,0,0.5],
              [0,0,0,0,0.5,0,0.5,0]])
PT = P.transpose()

#---- Function that takes k as input and outputs the transposed matrix to the power of the given k.
def PTpowerk(k):
    if k == 2:
        PT2 = np.matmul(PT, PT) #PT^k when k=2
        return  PT2
    elif k == 3:
        PT2 = np.matmul(PT, PT)
        PT3 = np.matmul(PT2,PT) #PT^k when k=3
        return PT3
    elif k == 4:
        PT2 = np.matmul(PT, PT)
        PT3 = np.matmul(PT2,PT) #PT^k when k=3
        PT4 = np.matmul(PT3,PT) #PT^k when k=4
        return print(PT4)
    elif k == 5:
        PT2 = np.matmul(PT, PT)
        PT3 = np.matmul(PT2,PT) #PT^k when k=3
        PT4 = np.matmul(PT3,PT) #PT^k when k=4
        PT5 = np.matmul(PT4,PT) #PT^k when k=5
        return print(PT5)
    elif k == 6:
        PT2 = np.matmul(PT, PT)
        PT3 = np.matmul(PT2,PT) #PT^k when k=3
        PT4 = np.matmul(PT3,PT) #PT^k when k=4
        PT5 = np.matmul(PT4,PT) #PT^k when k=5
        PT6 = np.matmul(PT5,PT) #PT^k when k=6
        return print(PT6)


k2 = PTpowerk(2)
k3 = PTpowerk(3)

#-- position vector
P35 = np.array([0, 0, 0, 0, 1, 0, 0, 0])
P35 = P35.transpose()

#----- multiplying by the position vector for the final result
P1 = np.matmul(k2,P35)
P2 = np.matmul(k3,P35)

#---- we need the 7th term in P1 and 4th term in P2
print(P1)
print(P2)
