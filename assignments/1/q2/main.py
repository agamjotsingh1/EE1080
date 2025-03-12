from math import log, sqrt

def gen_bernoulli(uniform_rv, p):
    if 0 < uniform_rv < p: # bin with size p and 1 - p
        return 1
    else:
        return 0

def gen_exp(uniform_rv, lam):
    if uniform_rv == 1: return 0
    return -log(1 - uniform_rv)/lam

def gen_cdfx(uniform_rv):
    if 0<=uniform_rv<=1/3:
        return sqrt(3*uniform_rv)
    elif 2/3<=uniform_rv<=1:
        return 6*uniform_rv - 2
    else:
        return 0
