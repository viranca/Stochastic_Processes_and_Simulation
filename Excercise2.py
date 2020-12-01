"""""
Consider an aircraft brake whose condition degrades after every flight cycles. 
Let Xi denote the degradation level of the brake after ith flight cycle. 
Xi = 0 implies that the brake has no degradation (is new). As soon as Xi ≥ 1, the 
degradation level of the brake exceeds a predefined threshold D = 1, the brake becomes 
inoperable and it must be replaced. After each flight cycle, the degradation level 
increases following the difference equation:
Xi+1 = Xi + ν
where ν is a random variable following a Gamma distribution with shape parameter 
α and scale parameter β, i.e., ν ∼ Gamma(α, β). The probability density function (pdf) of Gamma(α, β) is:

a) In the file data.csv you are given historical data on the degradation of same- type 8 brakes of an aircraft 
during 100 flight cycles. Figure 2 plots this data. Your brake is of the same type as the 8 brakes. 
You know that the brakes degrade following Gamma(α, β).
Estimate parameters α and β using the data in data.csv and a maximum likelihood estimator (MLE). 
In the data.csv file, each column corresponds to one brake. Assume that all brake follows Gamma(α,β) 
with the same parameters. MLE of a Gamma distribution is explained in Additional 
Document MLE for Assignment 1 (Brightspace → Assignment 1 → Additional Document MLE) and in Tutorial 2.
With the estimated α and β, use Monte Carlo simulation to determine the expected number of flight cycles 
that the component can make before Xi ≥ 1 (we call this the MeanTimeToFailure).

For the next exercises, use the parameters α = 0.3 and β = 0.02.
b) Determine the expected degradation level of a brake after 50 flight cycles, given that X0 = 0.1. 
Use Monte Carlo simulation with 100, 10.000, 1.000.000 simulation runs. Determine the confidence 
interval for these expected degrada- tion levels. What do you observe?
c) We replace the considered brake after it completes 160 flight cycles since its last replacement, 
i.e., scheduled replacement. If the brake becomes inop- erable after ith flight cycle (Xi ≥ 1), 
we replace the brake immediately, i.e., unscheduled replacement. Because an unscheduled replacement 
causes delays and extra maintenance cost, it is not desired. Use Monte Carlo simulations to determine 
the following properties: (1) the mean number of flight cycles com- pleted by a brake before it is 
replaced (both scheduled and unscheduled), (2) the ratio between the number of unscheduled replacements 
and the number of all replacements (both scheduled and unscheduled) during 1.000 flight cycles. 
Assume that we have a new brake at the beginning, i.e., X0 = 0.3

Hint for Python users:
• numpy.random.gamma(shape=α, scale=β) : to generate a random variable following the Gamma distribution.
• scipy.special.gamma(x) : to get the value of Gamma function Γ(x).
• pandas.read csv(open(file directory, ‘r’)).values : to read csv file.
"""""
import pandas as pd
from scipy.stats import gamma
import matplotlib.pyplot as plt
import scipy

import numpy as np


with open('data.csv', 'r') as f:
    df = pd.read_csv(f, sep=',', header=0)
    data = df

#%%
#Create seperate dataframes for each brake.
#And create a list of the v values for each brake, for each flight cycle.
brake_1 = data['Brake-1']
brake_1_v = []
for i in range(len(brake_1) - 1):
    v_i = brake_1[i + 1] - brake_1[i]
    brake_1_v.append(v_i)
    
brake_2 = data['Brake-2']
brake_2_v = []
for i in range(len(brake_2) - 1):
    v_i = brake_2[i + 1] - brake_2[i]
    brake_2_v.append(v_i)
    
brake_3 = data['Brake-3']
brake_3_v = []
for i in range(len(brake_3) - 1):
    v_i = brake_3[i + 1] - brake_3[i]
    brake_3_v.append(v_i)
    
brake_4 = data['Brake-4']
brake_4_v = []
for i in range(len(brake_4) - 1):
    v_i = brake_4[i + 1] - brake_4[i]
    brake_4_v.append(v_i)
    
brake_5 = data['Brake-5']
brake_5_v = []
for i in range(len(brake_5) - 1):
    v_i = brake_5[i + 1] - brake_5[i]
    brake_5_v.append(v_i)
    
brake_6 = data['Brake-6']
brake_6_v = []
for i in range(len(brake_6) - 1):
    v_i = brake_6[i + 1] - brake_6[i]
    brake_6_v.append(v_i)
    
brake_7 = data['Brake-7']
brake_7_v = []
for i in range(len(brake_7) - 1):
    v_i = brake_7[i + 1] - brake_7[i]
    brake_7_v.append(v_i)
    
brake_8 = data['Brake-8']
brake_8_v = []
for i in range(len(brake_8) - 1):
    v_i = brake_8[i + 1] - brake_8[i]
    brake_8_v.append(v_i)

#%%


#Combine all brake dataframes into a single column, combining the data.
all_brakes_combined = pd.concat([brake_1, brake_2, brake_3, brake_4, brake_5, brake_6, brake_7, brake_8])

all_brakes_v_combined = brake_1_v + brake_2_v + brake_3_v + brake_4_v + brake_5_v + brake_6_v + brake_7_v + brake_8_v
#all_brakes_v_combined.sort()
#print(all_brakes_v_combined)

all_brakes_v_combined = pd.DataFrame(all_brakes_v_combined)

#Calculating the mean and variance   
x = all_brakes_v_combined

#alpha and beta computed by the method of moments. NOT USED!
mean = x.mean()
var  = x.var()
alpha_MOM = (mean**2)/var
beta_MOM  = mean / alpha_MOM


#%%
#alpha and beta computed by gamma.fit , which uses maximum likelihood method:
alpha, mu_gamma, beta = gamma.fit(x, floc=0)

print( 'Alpha:', alpha, 'Beta:', beta) 
#print(alpha_MOM, beta_MOM)
# https://homepage.divms.uiowa.edu/~mbognar/applets/gamma.html


#Create a plot with randomly generated datapoints from the found distribution.
generated_points = []
for i in range(10000):
    random_value_from_distribution = np.random.gamma(shape=alpha, scale=beta)
    generated_points.append(random_value_from_distribution)
    i = i + 1
generated_points.sort()
plt.plot(generated_points)
plt.show()


#Monte carlo, determining the mean time to failure.
number_of_cycles_before_failure_list = []
for i in range(10000):
    x_i = 0
    number_of_cycles_before_failure = 0
    while x_i < 1:
        number_of_cycles_before_failure = number_of_cycles_before_failure + 1
        random_value_from_distribution = np.random.gamma(shape=alpha, scale=beta)
        x_i = x_i + random_value_from_distribution
    number_of_cycles_before_failure_list.append(number_of_cycles_before_failure)    
    i = i + 1
    
#print(number_of_cycles_before_failure_list)
print(np.mean(number_of_cycles_before_failure_list))





































