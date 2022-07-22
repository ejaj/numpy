import numpy as np

# array1 = np.array([10, 12, 14, 16, 18, 20])
# array2 = array1.copy()
# array2[1] = 20
# print(array1)
# print(array2)
array1 = np.array([10, 12, 14, 16, 18, 20])
array2 = array1.view()
array2[1] = 20
print(array1)
print(array2)
