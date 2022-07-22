import numpy as np

# my_array = np.array([2, 4, 8, 10, 12])
# print(my_array)
# print("std value:")
# print(np.std(my_array))

my_array = np.random.randint(1, 20, size=(3, 4))
print(my_array)
print("std-dev:")
print(np.std(my_array, axis=1))
print(np.std(my_array, axis=0))
