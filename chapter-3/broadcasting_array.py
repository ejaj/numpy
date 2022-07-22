import numpy as np

# array1 = np.array([14, 25, 31])
# array2 = np.array([10])
#
# result = array1 + array2
# print(result)

# array_mul_d = np.random.randint(1, 20, size=(3, 4))
# print(array_mul_d)
# array_mul_d_2 = np.array([10])
# print("after bradcasting")
# result = array_mul_d + array_mul_d
#
# print(result)

# array1 = np.random.randint(1, 20, size=(3, 4))
# print(array1)
# array2 = np.array([5, 10, 20, 25])
# print("after bradcasting")
# result = array1 + array2
# print(result)

array1 = np.random.randint(1, 20, size=(3, 4))
print(array1)
array2 = np.array([[5], [10], [20]])
print("after bradcasting")
result = array1 + array2
print(result)
