import sys
import numpy as np
from math import log, exp, sqrt, pi
import matplotlib.pyplot as plt

# Set the seed for reproducibility
np.random.seed(69)

def gen_sorted_sample_matrix(N):
    mat = np.random.uniform(0, 1, size=(N, 6))

    for i in range(N):
        mat[i] = np.sort(mat[i])

    return mat

def gen_X(N):
    mat = gen_sorted_sample_matrix(N)
    X = mat[:, 3]
    return X

def f_a(x):
    return 60*(x**3)*((1 - x)**2)

def f_b(x):
    return 30*(x**4)*(1 - x)

def plot_density_function(h = 0.001):
    x = np.arange(0, 1 + h, h)
    plt.plot(x, f_a(x), color="blue", label="$F_a(x)$")
    plt.plot(x, f_b(x), color="orange", label="$F_b(x)$")

def compare_densities(hist, bin_centers):
    mse_a = np.mean(np.square(hist - f_a(bin_centers)))
    mse_b = np.mean(np.square(hist - f_b(bin_centers)))
    if mse_a < mse_b:
        print("a")
    else:
        print("b")

N = int(sys.argv[1])
bin_edges = np.arange(0, 1 + 0.01, 0.01)

X = gen_X(N)

hist, bin_edges = np.histogram(X, density=True, bins=bin_edges)
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

compare_densities(hist, bin_centers)

plt.bar(bin_centers, hist, width=bin_edges[1] - bin_edges[0], alpha=0.75, color="skyblue", label="Histogram of X Samples")
plot_density_function()

plt.legend()
plt.xlabel("Samples")
plt.ylabel("Frequency")
plt.title("Comparison of Densities for X Samples")
plt.show()
