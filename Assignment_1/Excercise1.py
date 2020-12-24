import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import anderson
from scipy import stats
from scipy.stats import variation
from math import sqrt
import statistics
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
n = 500

"""--------initialise lists and counters---------"""
#for question a)
d=0
probcount = 0
arrivalcount=[]
arrivals=0
cofvarr=[]
#for question b)
c=0
from3count=0
from3list=[]
cofv3=[]
# for question c) and d)
a=0
totaldelay = 0
delaylist=[]
cofv=[]

"""----------- start simulation ----------------"""
for x in range(n):
    # get arrival times using a sorted uniform distribution
    arr = np.round(sorted(np.random.uniform(0, 120, 20)))
    # save the initial arrival times for delay comparison
    arr0 = arr
    # delay arrivals if they are too close together
    i=0
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

    # for b) evtols arriving from region 3, probability = 0.3 -> weight 30
    list = [0,1]
    fromreg3 = random.choices(list, weights=(70,30), k=len(arr))
    # count the number of arrivals from reg3
    reg3count = sum(fromreg3)
    from3count += reg3count

    # calculate variance and standard deviation for from region3
    from3list.append(reg3count)
    c+=1
    varlist1 = []
    avgfromreg3=from3count/c
    for b in range(c):
        cvar = (from3list[b] - avgfromreg3) ** 2
        varlist1.append(cvar)
    var3 = sum(varlist1) / c
    stdev3 = sqrt(var3)
    cofv3.append(stdev3 / avgfromreg3)

    # delay calculations
    a+=1
    delay=sum(arr-arr0)
    #print(delay)
    delaylist.append(delay)
    totaldelay+=delay
    # print('totdel',totaldelay)
    avgtotaldelay=totaldelay/a
    # print('avg', avgtotaldelay)

    # calculate variance and standard deviation for delay
    varlist=[]
    for b in range(a):
        avar=(delaylist[b]-avgtotaldelay)**2
        varlist.append(avar)
    var=sum(varlist)/a
    stdev_delay=sqrt(var)
    #print('var',var)
    #print('stdev',stdev)
    # calculate coefficient of variance
    cofv.append(stdev_delay/(avgtotaldelay))

    #mean_inloop = statistics.mean(delaylist) # other way to calculate the moving average
    #print('mean_inloop', mean_inloop)
    #print('cofv',cofv)

    # for a) 9.45-10.15 = 15-45min after 9.30
    #count the number of arrivals between 9.45 and 10.15
    count = 0
    for j in range(len(arr)):
        if 15 <= arr[j] <= 45:
            count += 1
    # count when 6 or more arrivals between 9.45 and 10.15
    if count >= 6:
        probcount += 1
    # print(count)

    #calculating the cofv to determine number of simulations for the arrivals between 9.45 and 10.15
    arrivalcount.append(count)
    arrivals+=count
    d += 1
    varlistarr = []
    avgarr = arrivals / d
    for b in range(d):
        dvar = (arrivalcount[b] - avgarr) ** 2
        varlistarr.append(dvar)
    vararr = sum(varlist1) / c
    stdevarr = sqrt(vararr)
    cofvarr.append(stdevarr / avgarr)

"""----------------- plotting coefficients of variance and QQ plot + Anderson test for normality -----------------"""
# Normality check for delay data
# using the Q-Q plot
data_1 = sorted(delaylist)
data_2 = stats.norm.rvs(size=1000, random_state=1)
plt.style.use('seaborn-whitegrid')
fig, axes = plt.subplots(2, 2, figsize=(6, 4))
stats.probplot(data_1, dist=stats.norm, plot=axes[0, 0])
stats.probplot(data_2, dist=stats.norm, plot=axes[0, 1])
axes[0, 0].set_title('Delay against Normal Q-Q plot')
axes[0, 1].set_title('Normal Q-Q plot')
axes[1, 0].hist(data_1, density=True, bins='auto')
axes[1, 1].hist(data_2, density=True, bins='auto')
fig.tight_layout()

# or using Anderson Darling test
# result=anderson(delaylist)
# print('Statistic: %.3f' % result.statistic)
# p = 0
# for i in range(len(result.critical_values)):
#     sl, cv = result.significance_level[i], result.critical_values[i]
#     if result.statistic < result.critical_values[i]:
#         print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
#     else:
#         print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))


# not normally distributed so we will use the central limit theorem
# how large must n be? ->: stabilising coefficient of variance cofv
'''-----------cofv in plot--------------'''
# create x-values
x=[]
for i in range(len(delaylist)):
     x.append(i)
plt.plot(x, cofv) # coefficient fo variance for delay
#plt.plot(x,cofv3) # coefficient fo variance for arrivals from region 3
#plt.plot(x, cofvarr) # coefficient fo variance for arrivals between 9.45 and 10.15
plt.xlabel('nr. of simulations')
plt.ylabel('coefficient of variation')
plt.show()

#confidence interval
# xbar-s/sqrt(n)*z_(alpha/2), xbar+s/sqrt(n)*z_(alpha/2),
lb = totaldelay/n-stdev_delay/sqrt(n)*1.96
ub = totaldelay/n+stdev_delay/sqrt(n)*1.96
"""-------------print results---------------"""
# divide counter of simulations of 6 or more arrivals between 9.45 and 10.15 by total nr of simulations to get probability
print("a): prob", probcount/n)

# divide the totals arriving from 3 by the number of simulations
evtolsfrom3=from3count/n
print("b) evtols from region 3:",int(evtolsfrom3))
# sanity check: prob eVTOLs of region 3 between 9.30-11.30 times approx 20 arriving in total per sim
from3 = 0.3 * 20
#print("b) sanity check", from3)

#print(delaylist)
print("c) avg total delay", totaldelay/n)
# sanity check using built in function
mean = statistics.mean(delaylist)
print("mean delay", mean)
print("c) var total delay", var)
# sanity check using built in function
stdev_delay1=statistics.stdev(delaylist)
print(stdev_delay1, stdev_delay1**2)
print("d) conf interval total delay", lb,ub)
#print(delaylist)

