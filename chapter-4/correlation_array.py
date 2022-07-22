import numpy as np

a1 = np.array([1, 3, 0, 0.9, 1.2])
a2 = np.array([-1, 0.5, 0.2, 0.6, 5])
print(a1)
print(a2)
print("correlation value:")
print(np.correlate(a1, a2))
