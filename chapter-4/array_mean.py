import numpy as np

# my_array = np.array([2, 4, 8, 10, 12])
# print(my_array)
# print("mean:")
# print(np.mean(my_array))

# my_array = np.random.randint(1, 20, size=(2, 3))
# print(my_array)
# print("mean:")
# print(np.mean(my_array, axis=1))
# print(np.mean(my_array, axis=0))

# my_array = np.array([2, 4, 8, 10, 12])
# print(my_array)
# print("median:")
# print(np.median(my_array))

my_array = np.random.randint(1, 20, size=(3, 5))
print(my_array)
print("median:")
print(np.median(my_array, axis=1))
print(np.median(my_array, axis=0))
