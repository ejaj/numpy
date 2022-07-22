import numpy as np

# arrange method
num_arr = np.arange(5, 11)
print(num_arr)
num_arr_step = np.arange(5, 11, 2)
print(num_arr_step)

# ones method
ones_array = np.ones(6)
print(ones_array)
ones_tow_d_array = np.ones((6, 4))
print(ones_tow_d_array)

# zeros method
zeros_array = np.zeros(6)
print(zeros_array)
zeros_two_d_array = np.zeros((6, 4))
print(zeros_two_d_array)

zeros_array_1 = np.zeros((3, 3))
print(zeros_array_1)
print("Extended Array")
zeros_extended_array = np.append(zeros_array_1, [[1, 2, 3]], axis=0)
print(zeros_extended_array)
print("Extended Array Column")
zeros_extended_array_colmun = np.append(zeros_array_1, [[1], [2], [3]], axis=1)
print(zeros_extended_array_colmun)


# eye method
eye_array = np.eye(5)
print(eye_array)

# random method
random_array = np.random.rand(4, 5)
print(random_array)
normal_random_array = np.random.randn(4, 5)
print(normal_random_array)
integer_random = np.random.randint(10, 50, 5)
print(integer_random)
