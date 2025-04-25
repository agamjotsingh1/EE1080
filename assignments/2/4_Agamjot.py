import numpy as np
import scipy.stats as stats
from scipy.linalg import eigh
import matplotlib.pyplot as plt

N = 1000

K = [[0.25, 0.3],
     [0.3, 1.0]]

M = np.array([0, 0])

X = stats.multivariate_normal.rvs(M, K, N)

eig_values, eig_vectors = eigh(K)

D = np.diag(eig_values[::-1])
U = eig_vectors[:, ::-1]

A = U@(np.sqrt(D))
S = np.random.normal(0, 1, size=(2, N))

X_samples = (A@S) + M[:, np.newaxis]

x1 = np.arange(-2.5, 2.5, 0.01)
x2 = np.arange(-3.5, 3.5, 0.01)
X1, X2 = np.meshgrid(x1, x2)
Xpos = np.empty(X1.shape + (2,))
Xpos[:, :, 0] = X1
Xpos[:, :, 1] = X2

F = stats.multivariate_normal.pdf(Xpos, M, K)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# First subplot for X
axs[0].scatter(X[:, 0], X[:, 1], color="lightcoral", alpha=0.4, marker="x")
axs[0].contour(x1, x2, F, cmap="viridis")
axs[0].set_title('Multivariate Normal Samples (Direct)')
axs[0].set_xlabel('y')
axs[0].set_ylabel('x')

# Second subplot for X_samples
axs[1].scatter(X_samples[0], X_samples[1], color="skyblue", alpha=0.75, marker="x")
axs[1].contour(x1, x2, F, cmap="plasma")
axs[1].set_title('Multivariate Normal Samples (Eigen Decomposition)')
axs[1].set_xlabel('y')
axs[1].set_ylabel('x')

plt.tight_layout()
plt.show()
