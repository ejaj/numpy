import numpy as np

# array1 = np.array([10, 12, 14, 16, 18, 20])
# np.savetxt("/Users/kazi/Projects/numpy/data.txt", array1)

loaded_array = np.load("/Users/kazi/Projects/numpy/chapter-3.npy")
loaded_array_text = np.loadtxt("/Users/kazi/Projects/numpy/data.txt")
print(loaded_array)
print(loaded_array_text)
