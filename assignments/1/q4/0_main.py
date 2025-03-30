import random
import matplotlib.pyplot as plt
import numpy as np

''' MODE 0 '''
def gen_X(theta):
    return 2*abs(np.sin(theta))

def gen_uniform_theta():
    return random.random()*(np.pi)

N = 100000
fav = 0
theta_samples = []

for i in range(N):
    theta = gen_uniform_theta() 
    if(np.pi/3 < theta < 2*np.pi/3):
        fav += 1
    theta_samples.append(theta)

X_samples = [gen_X(theta) for theta in theta_samples]

print("Fraction of chord length > sqrt(3) -> ", fav/N)
plt.hist(X_samples, bins=int(np.sqrt(N)))
plt.show()
