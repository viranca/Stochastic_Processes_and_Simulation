"""
We consider a building with 8 distinct rooms (see Fig. 3). A drone flies inside the building,
checking one room at a time for 1 minute, then moves to a new, accessible, neighboring room with
equal probability. An intruder visits a room i, i ∈ {1, 2, ..., 8} for an amount of time exponentially distributed with
parameter

λi =  (i + 1)/8, then moves to a new, accessible, neighboring room with equal probability.
Derive analytically (use mathematical notation and write first the equations, then the numerical results):
a) Formulate the surveillance of the rooms by a drone as a discrete-time Markov chain {Xt} and the intruder visiting
the rooms as a continuous-time Markov chain {Yt}. Explain why your formulation is a
discrete/continuous time Markov chain and specify the defining elements (state space, transition matrix).
b) Determine pX5|X6,X3(7|4,5).
c) Determine pX1000,X1001(5,2) using the stationary distribution. Explain your
result.
d) Knowing that the intruder is at the beginning in room 3, i.e., Y0 = 3, determine
the probability that the intruder leaves room 3 in less than 0.9 minutes.
MC simulation. Please upload the code with the assignment.
Important for Python and Matlab: In order to sample a random variable from an exponential distribution with rate λ,
the Python and Matlab code should be given as input the mean 1/λ as shown below:
Python: x = numpy.random.exponential(scale=1/λ)
Matlab: x = exprnd(1/λ)
e) The drone always starts in room 8. The intruder starts in room 1. Simulate this system and determine the expected
time until the drone finds the intruder, i.e., they are in the same room at the same time. Plot the distribution of
the time when the drone finds the intruder and determine the variance of this time. Also show that the number of
simulations is large enough.
f) When the drone enters a room, it must stay there for at least 1 minute. You are tasked with developing a strategy for
the drone to visit the rooms, i.e., how should the drone visit the rooms, starting from room 8, such that it minimizes
the time to find an intruder. Assume the intruder enters the building at t = 0 with an equal probability of entering any
of the outside rooms by climbing through the window. You can consider adjusting the order in which the drone visits the
rooms and/or the time it spends in a room.
Note that the transition from one room to another is instantaneous, i.e., the drone and the intruder to not meet each
other while crossing a door at exactly the same time. Also, neither the drone, nor the intruder see through walls, i.e.,
the drone and the intruder see each other only when they are in the same room.
"""
'''
prob matrix drone
p_{x_{t+1}|x_{t}}
    [0      0   0   1   0       0       0   0]
    [0      0   .5  0   .5      0       0   0]
    [0      .5  0   0   0       .5      0   0]
    [1/3    0   0   0   1/3     0       1/3 0]
    [0      1/3 0   1/3 0       0       0   1/3]
    [0      0   0   0   0       1       0   0]   
    [0      0   0   0   .5      0       .5  0] 
    
'''