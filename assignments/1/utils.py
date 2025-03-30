import random
from math import log

def bernoulli(p):
    """
    Simulates a Bernoulli trial.

    p -> Probability of success
    """
    n = random.random()  # Generate a uniform random variable sample in [0, 1]

    # Binning [0, 1] into two parts -> [0, p] and (p, 1]
    # Probability of [0, p] -> p
    # Probability of (p, 1] -> 1 - p
    if n < p:
        return 1  # Heads 
    else:
        return 0  # Tails

def uniform_to_bernoulli(uniform_rv, p):
    if 0 < uniform_rv < p: # bin with size p and 1 - p
        return 1
    else:
        return 0

def uniform_to_exp(uniform_rv, lam):
    if uniform_rv == 1: return 0
    return -log(1 - uniform_rv)/lam
