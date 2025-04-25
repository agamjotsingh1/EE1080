import random
import sys
import numpy as np
from math import log, exp, sqrt, pi
import matplotlib.pyplot as plt

# Set the seed for reproducibility
# random.seed(42)

def gen_samples(mode, n, N, param):
    if mode == 0:
        return np.random.binomial(n=1, p=param, size=(N, n)) # Binomial with n = 1
    elif mode == 1:
        return np.random.uniform(0, 1, size=(N, n))
    elif mode == 2:
        return np.random.exponential(scale=(1/param), size=(N, n)) # scale = 1/lambda
    else:
        return np.zeros((N, n))

    '''
    X = np.zeros((N, n));

    for i in range(N):
        for j in range(n):
            if mode == 0:
                X[i][j] = bernoulli_rv(param) 
            elif mode == 1:
                X[i][j] = random.uniform(0, 1)
            elif mode == 2:
                X[i][j] = exponential_rv(param) 

    return X
    '''

def gaussian_plot(mode, n, param):
    mean = 0 
    variance = 0

    if mode == 0:
        mean = param
        variance = param*(1 - param)/n

    elif mode == 1:
        mean = 1/2
        variance = (1/12)/n

    elif mode == 2:
        mean = 1/param
        variance = ((1/param)**2)/n

    print(mean, variance)

    def f(x):
        return np.exp(-(x - mean)**2/(2*variance))/(np.sqrt(2*np.pi*variance))

    offset = 2*n*variance if mode != 2 else n*variance/4
    x = np.arange(mean - offset, mean + offset, 0.001)
    y = f(x)

    return x, y

mode, n, N = [int(arg) for arg in sys.argv[1:4]]
param = float(sys.argv[4])
X = gen_samples(mode, n, N, param)
row_averages =  [sum(X[i])/n for i in range(N)]

if mode == 0: plt.hist(row_averages, density=True, alpha=0.75, color="skyblue", label="Row Average Histogram")
else: plt.hist(row_averages, density=True, bins = int(np.sqrt(N)), alpha=0.75, color="skyblue", label="Row Average Histogram")

x, y = gaussian_plot(mode, n, param)
plt.plot(x, y, color="black", label="Normal Plot")

plt.legend()
plt.xlabel("Samples")
plt.ylabel("Frequency")
if mode == 0: plt.title(f"Bernoulli Samples (p = {param})")
elif mode == 1: plt.title("Uniform Samples ([0, 1])")
elif mode == 2: plt.title(f"Exponential Samples ($\\lambda$ = {param})")
plt.show()
