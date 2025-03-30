import random
import matplotlib.pyplot as plt
import numpy as np

random.seed(123)

def I_to_dec(I):
    n = len(I)
    N = len(I[0])

    dec_I = []

    for j in range(N):
        bin_sum = 0
        for i in range(n):
            if(I[i][j]):
                bin_sum += 1 << i
        dec_I.append(bin_sum)

    return dec_I

def gen_U(n, N):
    U = [[random.random() for _ in range(N)] for _ in range(n)]
    return U

def gen_I(U, k):
    n = len(U)
    N = len(U[0])

    I = [[0 for _ in range(N)] for _ in range(n)]

    for j in range(N):
        for i in range(n):
            prev_sum = 0
            for a in range(i):
                prev_sum += I[a][j]

            I[i][j] = 1 if U[i][j] <= (k - prev_sum)/(n - i) else 0

    return I

def gen_subsets(n, k, N):
    U = gen_U(n, N)
    I = gen_I(U, k)
    return I_to_dec(I)


distri = gen_subsets(3, 2, 10000)
bins = np.arange(0, 8 + 1.5) - 0.5

# then you plot away
fig, ax = plt.subplots()
_ = ax.hist(distri, bins, rwidth=0.7)
ax.set_xticks(bins + 0.5)
#plt.hist(distri, bins = 8)
plt.show()
