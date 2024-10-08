# 2.Write a Python script to concatenate the following dictionaries to create a new one. 

# Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 

# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Define the dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary
merged_dict = {}

# Concatenate dictionaries using update
merged_dict.update(dic1)
merged_dict.update(dic2)
merged_dict.update(dic3)

# Print the result
print("Concatenated dictionary:", merged_dict)

# ans
# Concatenated dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}