import numpy as np

print("one-dimensional array")
one_d_array = np.random.randint(1, 20, 10)
print(one_d_array)
print("\ntwo-dimensional array")
two_d_array = one_d_array.reshape(2, 5)
print(two_d_array)
