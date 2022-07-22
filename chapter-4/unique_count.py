import numpy as np

my_array = np.array([5, 8, 7, 5, 9, 3, 7, 7, 1, 1, 8, 4, 6, 9, 7, 3])
# unique_items = np.unique(my_array)
# print(unique_items)
unique_items, counts = np.unique(my_array, return_counts=True)
# print(unique_items)
# print(counts)
# frequencies = np.asarray((unique_items, counts))
frequencies = np.asarray((unique_items, counts)).T
print(frequencies)
