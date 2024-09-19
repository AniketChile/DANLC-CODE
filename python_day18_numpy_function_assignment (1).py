# 1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

# Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-4,-12])

import numpy as np

# Given temperature array
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, -4, -12])

# Find the indices for hot days (> 35 degrees)
hot_days_indices = np.where(temperatures > 35)

# Find the indices for cold days (< 5 degrees)
cold_days_indices = np.where(temperatures < 5)

# Find the indices for extreme temperatures (hot or cold days)
extreme_days_indices = np.where((temperatures > 35) | (temperatures < 5))

# Extract temperature values for hot, cold, and extreme days
hot_temperatures = temperatures[hot_days_indices]
cold_temperatures = temperatures[cold_days_indices]
extreme_temperatures = temperatures[extreme_days_indices]

# Print the results
print("Hot days temperatures (> 35°C):", hot_temperatures)
print("Cold days temperatures (< 5°C):", cold_temperatures)
print("Extreme temperatures (either hot or cold):", extreme_temperatures)




# ans
# Hot days temperatures (> 35°C): [36.8 38.7 37.2]
# Cold days temperatures (< 5°C): [ -4. -12.]
# Extreme temperatures (either hot or cold): [ 36.8  38.7  37.2  -4.  -12. ]

