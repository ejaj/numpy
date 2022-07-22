import numpy as np

num_list = [10, 3, 4, 5, 6]
my_array = np.array(num_list)
print(type(my_array))

a = [12, 34, 45]
b = [45, 67, 78]
c = [80, 90, 97]
multi_d_array = np.array([a, b, c])
print(multi_d_array)
print(multi_d_array.shape)

my_array_string = np.array(["Red", "Green", "Orange"])
print(my_array_string)
print("After deletion")
# updated_array = np.delete(my_array_string, 1)
# print(updated_array)
updated_array = np.delete(my_array_string, [1, 2])
print(updated_array)

integer_random = np.random.randint(1, 11, size=(4, 5))
print(integer_random)
print("After deletion")
updated_array_mul_d = np.delete(integer_random, 1, axis=0)
print(updated_array_mul_d)

integer_random_col = np.random.randint(1, 11, size=(4, 5))
print(integer_random_col)
print("After deletion")
updated_array_mul_d_col = np.delete(integer_random, 1, axis=1)
print(updated_array_mul_d_col)
