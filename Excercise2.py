
"""
=============================================================================
Assignment 1 Exercise 2
=============================================================================
"""

import pandas as pd
from scipy.stats import gamma
import matplotlib.pyplot as plt
import scipy
import math
import numpy as np
import statistics


#%%
"""
=============================================================================
Data preparation
=============================================================================
"""

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

"""
=============================================================================
Part a: Maximum likelihood estimation, finding alpha and beta. 
Variable names are self explanatory.
=============================================================================
"""

#Combine all brake dataframes into a single column, combining the data.
all_brakes_combined = pd.concat([brake_1, brake_2, brake_3, brake_4, brake_5, brake_6, brake_7, brake_8])

all_brakes_v_combined = brake_1_v + brake_2_v + brake_3_v + brake_4_v + brake_5_v + brake_6_v + brake_7_v + brake_8_v
#all_brakes_v_combined.sort()
#print(all_brakes_v_combined)

all_brakes_v_combined = pd.DataFrame(all_brakes_v_combined)

#Calculating the mean and variance   
x = all_brakes_v_combined

##Below are three different ways for finding alpha and beta
#alpha and beta computed by the method of moments. NOT USED!
mean = x.mean()
var  = x.var()
alpha_MOM = (mean**2)/var
beta_MOM  = mean / alpha_MOM
#print('Method of Moments', alpha_MOM, beta_MOM)


#alpha and beta computed by gamma.fit , which uses maximum likelihood method:
alpha_fit, mu_gamma, beta_fit = gamma.fit(x, floc=0)
#print('gamma.fit', alpha_fit, beta_fit)


#alpha and beta computed by implementation of an algorithmn to find the MLE (using the variable names from the assignment):
mean_y = x.mean()
log_mean_y = math.log(mean_y) #log(y_bar)

log_y = []
for i in range(len(x)):
    log_y.append(math.log(x[0][i]))
    i =+ 1
mean_log_y = statistics.mean(log_y) ##(log(y)_bar)

n = len(x)

log_likelihood_list = []

xforplot = np.arange(0.001, 1, 0.0001)
for alpha_i in xforplot:
    log_likelihood = n*(alpha_i -1)*mean_log_y -n*alpha_i - n*math.log(scipy.special.gamma(alpha_i)) \
        - n*alpha_i*log_mean_y + n*alpha_i*math.log(alpha_i)
    log_likelihood_list.append(log_likelihood)
    
max_log_likelihood = max(log_likelihood_list)
alpha_MLE = xforplot[log_likelihood_list.index(max_log_likelihood)]

beta_MLE  = mean_y[0]/alpha_MLE

print('MLE', 'alpha ' ,alpha_MLE, '  beta ' , beta_MLE)

plt.plot(xforplot, log_likelihood_list)
plt.xlabel('alpha')
plt.ylabel('log_likelihood')
plt.show()


#%%


"""
=============================================================================
Small intermezzo to visualize the found distribution.
=============================================================================
"""

#Create a plot with randomly generated datapoints from the found distribution.
alpha = alpha_MLE
beta = beta_MLE

generated_points = []

for i in range(10000):
    random_value_from_distribution = np.random.gamma(shape=alpha, scale=beta)
    generated_points.append(random_value_from_distribution)
    i = i + 1
    
generated_points.sort()
generated_points.reverse()
plt.plot(generated_points)
plt.xlabel('n')
plt.ylabel('Output gamma function')
plt.show()



"""
=============================================================================
Part a: monte carlo to find the expected number of flights before x_i>1
=============================================================================
"""
#Monte carlo, determining the mean time to failure.
number_of_cycles_before_failure_list = []
for i in range(1000):
    x_i = 0
    number_of_cycles_before_failure = 0
    while x_i < 1:
        number_of_cycles_before_failure = number_of_cycles_before_failure + 1
        random_value_from_distribution = np.random.gamma(shape=alpha, scale=beta)
        x_i = x_i + random_value_from_distribution
    number_of_cycles_before_failure_list.append(number_of_cycles_before_failure)    
    i = i + 1
    
#print(number_of_cycles_before_failure_list)
print(' expected number of flights before x_i>1: ' , np.mean(number_of_cycles_before_failure_list))



#%%
"""
=============================================================================
Part b: Expected degradation after 50 flights (X_50) for 100, 10.000 and 1.000.000 runs
=============================================================================
"""

X_50_list = []
for MC_i in range(1000001): #monte carlo iterations
    x_i = 0.1
    for i in range(51):
        random_value_from_distribution = np.random.gamma(shape=alpha, scale=beta)
        x_i = x_i + random_value_from_distribution
    X_50_list.append(x_i)
    if MC_i == 100:
        print('100 simulations X_50 = ', statistics.mean(X_50_list))
    if MC_i == 10000:
        print('10000 simulations X_50 = ', statistics.mean(X_50_list))
    if MC_i == 1000000:
        print('1000000 simulations X_50 = ', statistics.mean(X_50_list))        

#%%

"""
=============================================================================
Some statistics and plots
=============================================================================
"""

X_50_list_100 = X_50_list[0:100]
X_50_list_10000 = X_50_list[0:10000]
X_50_list_1000000 = X_50_list[0:10000000]
print('100 simulations X_50 stdev = ', statistics.stdev(X_50_list_100))
print('100000 simulations X_50 stdev= ', statistics.stdev(X_50_list_10000))
print('1000000 simulations X_50 stdev= ', statistics.stdev(X_50_list_1000000))

plt.hist(X_50_list_100)
plt.xlabel('i')
plt.ylabel('x_50_i')
plt.show()

plt.hist(X_50_list_10000)
plt.ylabel('i')
plt.xlabel('x_50_i')
plt.show()

plt.hist(X_50_list_1000000)
plt.ylabel('i')
plt.xlabel('x_50_i')
plt.show()

plt.hist(X_50_list)
plt.ylabel('i')
plt.xlabel('x_50_i')
plt.show()

from statsmodels.graphics.gofplots import qqplot
X_50_list_df = pd.DataFrame(X_50_list)
qqplot(X_50_list_df, line='s')
plt.show()

#%%

"""
=============================================================================
Part C: Monte carlo 1000 flights experiment  
Variable names are self explanatory.
=============================================================================
"""

flight_cycle_counter_list = [] 
for MC_i in range(100000):
    x_i = 0
    flight_cycle_counter = 0
    while x_i < 1:
        flight_cycle_counter = flight_cycle_counter + 1
        random_value_from_distribution = np.random.gamma(shape=alpha, scale=beta)
        x_i = x_i + random_value_from_distribution
    flight_cycle_counter_list.append(flight_cycle_counter)    
    MC_i = MC_i + 1
    
#%% part one
for i in range(len(flight_cycle_counter_list)):
    if flight_cycle_counter_list[i] > 160:
        flight_cycle_counter_list[i] = 160

mean_flight_cycles_scheduled_and_unscheduled = statistics.mean(flight_cycle_counter_list)
print('mean_flight_cycles_scheduled_and_unscheduled: ' ,mean_flight_cycles_scheduled_and_unscheduled)

#%% part two

number_of_all_replacements = len(flight_cycle_counter_list)

unscheduled_replacement_list = []
for i in range(len(flight_cycle_counter_list)):
    if flight_cycle_counter_list[i] < 160:
        unscheduled_replacement_list.append(flight_cycle_counter_list[i])

number_of_unscheduled_replacements = len(unscheduled_replacement_list)

print('number_of_unscheduled_replacements',statistics.mean(unscheduled_replacement_list))

Ratio_unscheduled_over_all_replacements = number_of_unscheduled_replacements/number_of_all_replacements

print('Ratio_unscheduled_over_all_replacements: ', Ratio_unscheduled_over_all_replacements)












