import random

random.seed(123)
max_trials = int(1e10)

def coin_toss():
    n = random.random()

    if n < 0.5:
        return 0 # -> tails
    else:
        return 1 # -> heads

def sim_petersburg(m):
    avg = 0
    for _ in range(m):
        for i in range(max_trials):
            if not coin_toss(): # tails is encountered
                avg += pow(2, i + 1)
                break
    return avg/m

print(sim_petersburg(100))
print(sim_petersburg(10000))
print(sim_petersburg(10000000))
