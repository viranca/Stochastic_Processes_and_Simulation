# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:04:53 2020

@author: theWissam
"""
import numpy as np
from scipy.linalg import solve

#This is the PI matrix
#The second column has been replaced by 1's
# When transposed, that becomes the second row
#which represents the sum(q)=1
P = np.array([[0,      1,  0,   1,    0,  0, 0, 0],
              [0,      1,  0.5,   0,    0.5,  0, 0 , 0],
              [0, 1, 0, 0, 0, 0.5, 0, 0],
              [1/3,      1,  0,   0,    1/3,  0, 1/3, 0],
              [0,      1,  0, 1/3,    0,  0,0, 1/3],
              [0,      1,  1,   0,    0,  0, 0 ,0],
              [0,1,0,0.5,0,0,0,0.5],
              [0,1,0,0,0.5,0,0.5,0]])

PT = P.transpose()

# subtract identity matrix to set up Ax=b <==> (A-I)x = 0
PTq = PT- np.identity(8)

#Make sure the identity subtraction does not 
#overwrite the second row being all 1s
PTq[1][1]=1

# b is all zeros, except the second term, 
#which is 1, for sum(q)=1
b = np.zeros((8,1))
b[1]=1
z= solve(PTq,b)
print(z)
