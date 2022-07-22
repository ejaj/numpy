import numpy as np

# print("original")
# my_array = np.random.randint(1, 20, 10)
# print(my_array)
# print("reversed")
# reversed_array = np.flipud(my_array)
# print(reversed_array)

print("original")
my_array = np.random.randint(1, 20, size=(3, 4))
print(my_array)
print("reversed")
reversed_array = np.fliplr(my_array)
print(reversed_array)
