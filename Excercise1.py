import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import anderson
from math import sqrt
import random
'''
eVTOLs arriving at a hub (20pcts)
At a vertiport, eVTOLs from 6 surrounding regions arrive. 
Between 9:30-11:30 in the morning, approximately 20 eVTOLs are 
expected to arrive at this hub. The arrival times of these eVTOLs 
are distributed uniformly U(9:30, 11:30). The probability that 
an arrival is from region i, i ∈ {1,2,...,6} is given in Table 1.

Region i       1     2    3    4     5      6
pRegion (i)  0.03   0.25  0.3  0.4   0.01   0.01

The eVTOLs land at the vertiport according to a FCFS (First-Come-First Serve) 
sequence. Each eVTOL requires 2min to land at the vertiport, i.e., the ]
minimum time between two consecutive landings is 2min. To ensure this minimum 
separation, incoming eVTOLs are delayed. Knowing that at 9:30 there are no 
eVTOLs at the vertiport, use Monte Carlo simulation to determine:
a) the probability that at least 6 eVTOLs arrive between 9:45-10:15.
b) the expected number of eVTOLs arriving from region i = 3 between 9:30- 11:30.
c) the total expected delay and the variance of the total delay during 9:30-11:30.
d) a 95% confidence interval of the total expected delay.
'''
#set number of simulations
n = 50000
# initialise
totaldelay = 0
a=0
probcount = 0
delaylist=[]
cofv=[]
xforplot=[]
from3count=0

for i in range(n):
    # get arrival times using a sorted uniform distribution
    arr = np.round(sorted(np.random.uniform(0, 120, 20)))
    arr0=arr
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

    #from region 3 calculations
    list=[0,1]
    fromreg3=random.choices(list, weights=(70,30), k=20)
    reg3count=sum(fromreg3)
    from3count+=reg3count

    # delay calculations
    a+=1
    delay=sum(arr-arr0)
    delaylist.append(delay)
    totaldelay+=delay
    #print('totdel',totaldelay)
    avgtotaldelay=totaldelay/a
    #print('avg', avgtotaldelay)
    for b in range(a):
        avar=(delaylist[b]-avgtotaldelay)**2
    var=avar/a
    stdev=sqrt(var)
    cofv.append(stdev/avgtotaldelay)
    xforplot.append(a)
    #var=(sum(delaylist[b]-avgtotaldelay for b in range(a)))
    #print('var',var)
    #print('cofv',cofv)

    # for a) 9.45-10.15 = 15-45min after 9.30
    count = 0
    for j in range(len(arr)):
        if 15 <= arr[j] <= 45:
            count += 1
    if count >= 6:
        probcount += 1
    # print(count)
#print(delaylist)
# probability of more than 6
print("a): prob", probcount/n)
# prob eVTOLs of region 3 between 9.30-11.30
# approx 20 from allover
from3 = 0.3 * 20
evtolsfrom3=from3count/n
print("b) evtolsfrom3",int(evtolsfrom3))
print("b) check", from3)
print("c) avg total delay", totaldelay/n)
print("c) var total delay", var)
result=anderson(delaylist)
print('Statistic: %.3f' % result.statistic)
p = 0
for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i], result.critical_values[i]
    if result.statistic < result.critical_values[i]:
        print('%.3f: %.3f, data looks normal (fail to reject H0: data is normal distributed)' % (sl, cv))
    else:
        print('%.3f: %.3f, data does not look normal (reject H0: data is normal distributed)' % (sl, cv))
# not normally distributed so we will use the central limit theorem
# how large must n be: stabilising coefficient of variance cofv
plt.plot(xforplot, cofv)
plt.xlabel('nr. of simulations')
plt.ylabel('coefficient of variation')
plt.show()
# xbar-s/sqrt(n)*z_(alpha/2), xbar+s/sqrt(n)*z_(alpha/2),
lb = totaldelay/n-stdev/sqrt(n)*1.96
ub = totaldelay/n+stdev/sqrt(n)*1.96
print("d) conf interval total delay", lb,ub)


