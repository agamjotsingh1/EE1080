import random
import matplotlib.pyplot as plt
import numpy as np

''' MODE 2 '''
def gen_R(U):
    return np.sqrt(U)

def gen_Z(R):
    return 2*np.sqrt(1 - R*R)

def gen_uniform_U():
    return random.random()

N = 100000
fav = 0
U_samples = [gen_uniform_U() for _ in range(N)]

Z_samples = []
for u in U_samples:
    R = gen_R(u)
    Z = gen_Z(R)

    Z_samples.append(Z)
    if (Z >= np.sqrt(3)):
        fav += 1

print("Fraction of chord length >= sqrt(3) -> ", fav/N)
plt.hist(Z_samples, bins=int(np.sqrt(N)))
plt.show()
