import numpy as np

# my_array = np.array([2, 4, 8, 10, 12])
# print(my_array)
# print("min value:")
# print(np.amin(my_array))

# my_array = np.random.randint(1, 20, size=(3, 4))
# print(my_array)
# print("min:")
# print(np.amin(my_array, axis=1))
# print(np.amin(my_array, axis=0))

# my_array = np.array([2, 4, 8, 10, 12])
# print(my_array)
# print("max value:")
# print(np.amax(my_array))

my_array = np.random.randint(1, 20, size=(3, 4))
print(my_array)
print("max:")
print(np.amax(my_array, axis=1))
print(np.amax(my_array, axis=0))
