import numpy as np
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
for i in range(10):
    arr = np.round(sorted(np.random.uniform(0, 120, 20)))

#print(arr)
    while i in range(len(arr) ):

        if arr[i-1] == arr[i]:
            arr[i] += 2
            arr=sorted(arr)
            i=0
        elif arr[i-1] == arr[i ] - 1:
            arr[i ] += 1
            arr=sorted(arr)
            i=0
        arr=sorted(arr)
        i+=1

    print(arr)