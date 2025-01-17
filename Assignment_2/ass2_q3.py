'''
The degradation over time of a component (wearing) is given by:
Xt =βt+σBt,
where β is a constant for degradation drift,
σ is a diffusion coefficient,
and Bt is standard Brownian motion.
Consider X0 = 0.

Monte Carlo simulation: (please submit also the code)
d) Using β = 1 and σ = 2, estimate E[X5] and Var[X5].
Consider 10, 100, 10.000 simulation runs. What do you observe?
e) Using β = 1 and σ = 2,
plot the empirical distribution of X5 using both a histogram and a Dirac function.
'''
from matplotlib import pyplot as plt
import statistics
import numpy as np
import statsmodels.api as sm
from statsmodels.distributions.empirical_distribution import ECDF # only needed if you want to plot the empirical cdf

"------ constants and lists ------"
β=1 # degradation constant
σ=2 # diffusion coefficient
n=10 # number of simulations, change to 10, 100 or 10000 for comparison

allruns=[] # list containing values for X_5 of all runs/simulations
mov_avg=[] # list containing moving average of X_5 needed for coefficient of variation calculations
mov_stdev=[] # list containing moving standard deviation of X_5 needed for coefficient of variation calculations
cofv=[0] # list containing the coefficients of variation to determine how many runs are needed until X_5 converges

"------ start MC simulation -------"
for a in range(n):
    # find the Brownian B_t+1 by adding N(0, t_{i+1}-t_{i}) for each increment
    def Brownian(t):
        B=[0]
        for i in range(t):
            u = np.random.normal(0, 1)
            v = u*np.sqrt(i-(i-1))
            Bt=B[-1]+v
            B.append(Bt)
        return (B[-1])

    # compute X_t by adding the degradation and diffusion coeff*Brownian
    X=[0]
    for t in range(1,6):
        X.append(β*t+σ*Brownian(t))
    # print(X)

    # collect value of X_5 in 'all runs' list
    allruns.append(X[-1])

    # get moving average and standard deviation to calculate coefficient of variance after each simulation
    if a!=0:
        mov_avg.append(statistics.mean(allruns))
        mov_stdev.append(statistics.stdev(allruns))
        cofv1=mov_stdev[-1]/mov_avg[-1]
        cofv.append(cofv1)

# determine mean and variance
mean = statistics.mean(allruns)
stdev=statistics.stdev(allruns)
variance=stdev**2
print(mean)
print(variance)

"""------------- plotting the coefficient of variance ---------------"""
# x=[]
# for i in range(len(allruns)):
#      x.append(i)
# plt.plot(x, cofv)
# plt.xlabel('nr. of simulations')
# plt.ylabel('coefficient of variation')
# plt.show()
"""------------- plotting just the histograms ---------------"""
"""------------- will be combined later on -------------"""
# plt.hist(allruns, density=True, bins='auto')
# plt.xlabel('value of X_5')
# plt.ylabel('density')
# plt.show()

"""------------- plotting just the dirac impulses ---------------"""
"""------------- will be combined later on ---------"""
# ydirac=[]
# for i in range(len(allruns)):
#     ydirac.append(1)
# # # plotting dirac impulses
# # plt.stem(allruns,ydirac)
# # plt.show()
#
"""-------------- plotting combinations of histogram, dirac, kde ---------------------"""
"""-------------- will be plotted side by side later on -------------"""
# # plotting a histogram plus KDE plus stem
# kde = sm.nonparametric.KDEUnivariate(allruns)
# kde.fit() # Estimate the densities
# fig = plt.figure()#figsize=(10, 5)
# ax = fig.add_subplot(111)
# # Plot the histogram
# # ax.hist(allruns, bins=5, density=True, label='Histogram from samples',
# #         zorder=5, edgecolor='k', alpha=0.5)
# # Plot the impulses (for this also uncomment line 82-84)
# ax.stem(allruns,ydirac)
# # Plot the KDE as fitted using the default arguments
# ax.plot(kde.support, kde.density, lw=3, color = 'k', label='KDE from samples', zorder=10)
# plt.show()

""" -------- plotting histogram+KDE and dirac+KDE side by side ----------- """
plt.subplot(1, 2, 1)
kde = sm.nonparametric.KDEUnivariate(allruns)
kde.fit() # Estimate the densities

# Plot the histogram
plt.hist(allruns, bins=100, density=True, label='Histogram from samples',
        zorder=5, edgecolor='k', alpha=0.5)
# plot the KDE as fitted using the default arguments
plt.plot(kde.support, kde.density, lw=3, color = 'k', label='KDE from samples', zorder=10)
plt.xlabel('value of X_5')
plt.ylabel('Probability density')

plt.subplot(1, 2, 2)
# Plot the impulses
ydirac=[]
for i in range(len(allruns)):
    ydirac.append(1)
plt.stem(allruns,ydirac)
# Plot the KDE as fitted using the default arguments
plt.plot(kde.support, kde.density, lw=3, color = 'k', label='KDE from samples', zorder=10)
plt.xlabel('value of X_5')
plt.ylabel('Probability density and unit impulse')

plt.show()
