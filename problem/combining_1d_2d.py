import numpy as np

num_1d = np.arange(5)
print("One dimensional array:")
print(num_1d)

num_2d = np.arange(10).reshape(2, 5)
print("\nTwo dimensional array:")
print(num_2d)
for a, b in np.nditer([num_1d, num_2d]):
    print("%d:%d" % (a, b), )

# num_2d = np.arange(21).reshape(3, 7)
# print("\nTwo dimensional array:")
# print(num_2d)
#
# for a, b in np.nditer([num_1d, num_2d]):
#     print("%d:%d" % (a, b), )


