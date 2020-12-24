import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import anderson
from scipy import stats
from scipy.stats import variation
from math import sqrt
import statistics
import random
#set number of simulations
n = 40

"""--------initialise lists and counters---------"""
# for c and d
a=0
totaldelay = 0
delaylist=[]
cofv=[]

for x in range(n):
    # get arrival times using a sorted uniform distribution
    arr = np.round(sorted(np.random.uniform(0, 120, 20)))
    # save the initial arrival times for delay comparison
    arr0 = arr
    print(arr0)
    i=0
    # delay arrivals if they are too close together
    while i in range(len(arr)):
        if arr[i-1] == arr[i]:
            arr[i] += 2
            arr = sorted(arr)
            i = 0
        elif arr[i-1] == arr[i] - 1:
            arr[i] += 1
            arr = sorted(arr)
            i = 0
        arr = sorted(arr)
        i += 1
    #print(arr)
# delay calculations

    a+=1
    delay=sum(arr-arr0)
    print(delay)
    delaylist.append(delay)
    totaldelay+=delay
    # print('totdel',totaldelay)
    avgtotaldelay=totaldelay/a
    # print('avg', avgtotaldelay)
#print(delaylist)
    b=[]
    for i in range(len(delaylist)):
        if delaylist[i] != 0:
            b.append(1)
print(len(b))