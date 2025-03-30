import random
import matplotlib.pyplot as plt
import numpy as np

''' MODE 1 '''
def gen_X(U):
    return 2*np.sqrt(1 - U*U)

def gen_uniform_U():
    return random.random()

N = 100000
fav = 0
U_samples = []

for i in range(N):
    U = gen_uniform_U() 
    #if(0 <= U <= 0.5):
    #    fav += 1
    U_samples.append(U)

X_samples = []
for u in U_samples:
    X_samples.append(gen_X(u))
    if(gen_X(u) >= np.sqrt(3)):
        fav += 1

print("Fraction of chord length > sqrt(3) -> ", fav/N)
plt.hist(X_samples, bins=int(np.sqrt(N)))
plt.show()
