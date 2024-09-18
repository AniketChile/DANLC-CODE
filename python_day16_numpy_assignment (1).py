# 1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives


import numpy as np

# Create arrays of 10 zeros, 10 ones, and 10 fives with integer data type
zeros_array = np.full(10, 0, dtype=int)
ones_array = np.full(10, 1, dtype=int)
fives_array = np.full(10, 5, dtype=int)

# Concatenate the arrays into one
final_array = np.concatenate((zeros_array, ones_array, fives_array))

# Print the final array
print(final_array)


# ans
# [0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 5 5 5 5 5 5 5 5 5 5]
