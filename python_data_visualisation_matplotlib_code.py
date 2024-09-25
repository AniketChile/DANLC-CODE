# 1. Install matplotlib  & you can use plt.plot() to create a line plot of given data

# x = [0, 5, 9, 10, 15, 20, 25] 

# y = [0, 1, 2, 3, 4, 5, 6]



import matplotlib.pyplot as plt  # Importing the matplotlib.pyplot module

# Given data for x and y
x = [0, 5, 9, 10, 15, 20, 25]  # X values
y = [0, 1, 2, 3, 4, 5, 6]      # Y values

# Create a line plot with blue color and circular markers
plt.plot(x, y, marker='o', linestyle='-', color='b')  

# Add labels for the x-axis and y-axis
plt.xlabel('X values')  # Label for the x-axis
plt.ylabel('Y values')  # Label for the y-axis

# Add a title to the plot
plt.title('Line Plot of Given Data')  # Title of the plot


# Show the plot
plt.show()  # Render the plot to the screen
