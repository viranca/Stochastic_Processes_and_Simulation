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
