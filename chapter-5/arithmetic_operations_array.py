import numpy as np

nums = [10, 20, 30, 40, 50]
np_sqr = np.sqrt(nums)
np_log = np.log(nums)
np_exp = np.exp(nums)
np_sine = np.sin(nums)
np_cos = np.cos(nums)
# print(np_sqr)
# print(np_log)
# print(np_exp)
# print(np_sine)
# print(np_cos)
# A = np.random.randn(4, 5)
# B = np.random.randn(5, 4)
# Z = np.dot(A, B)
# print(Z)

# row1 = [10, 12, 13]
# row2 = [45, 32, 16]
# row3 = [45, 32, 16]
# nums_2d = np.array([row1, row2, row3])
# multiply = np.multiply(nums_2d, nums_2d)
# print(multiply)

row1 = [1, 2, 3]
row2 = [5, 2, 8]
row3 = [9, 1, 10]
nums_2d = np.array([row1, row2, row3])
inverse = np.linalg.inv(nums_2d)
determinant = np.linalg.det(nums_2d)
np_trace = np.trace(nums_2d)
print(inverse)
