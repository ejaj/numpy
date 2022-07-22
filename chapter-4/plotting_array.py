import numpy as np
import matplotlib.pyplot as plt

import math

# x_vals = np.linspace(0, 20, 20)
# print(x_vals)
# y_vals = [math.sqrt(i) for i in x_vals]
# plt.plot(x_vals, y_vals)

# x_vals = np.linspace(0, 20, 20)
# y_vals = [math.sqrt(i) for i in x_vals]
# y2_vals = x_vals ** 3
#
# plt.xlabel('X Values')
# plt.ylabel('Y Values')
# plt.title('square Roots')
# plt.plot(x_vals, y_vals, 'r', label='square Root')
# plt.plot(x_vals, y2_vals, 'b', label='Cube')
# plt.legend(loc='upper center')

my_array = np.random.randint(1, 20, size=(4, 4))
print(my_array)
plt.imshow(my_array)
plt.show()
