import numpy as np

my_array = np.random.randint(1, 20, size=(3, 4))
print(my_array)
my_array.tofile('/Users/kazi/Projects/numpy/chapter-3.csv', sep=',')
np.savetxt('/Users/kazi/Projects/numpy/sdsd.csv', my_array, delimiter=",")
loaded_array = np.genfromtxt('/Users/kazi/Projects/numpy/my_css.csv', delimiter=',')

print(loaded_array)
