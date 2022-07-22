import numpy as np

# s = np.arange(1, 11)
# print(s)
# print(s[1])
# print(s[1:9])
# print(s[:5])
# print(s[5:])

row1 = [10, 12, 13]
row2 = [45, 32, 16]
row3 = [45, 32, 16]
nums_2d = np.array([row1, row2, row3])
print(nums_2d)
print(nums_2d[:2, :])
print(nums_2d[:, :2])
print(nums_2d[1:, 1:])
