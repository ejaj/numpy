from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
X, y = datasets.make_moons(100, noise=0.10)
x1 = X[:, 0]
x2 = X[:, 1]
plt.figure(figsize=(10, 7))
plt.scatter(x1, x2, c=y, cmap=plt.cm.coolwarm)
