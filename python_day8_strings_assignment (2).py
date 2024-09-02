# Write a Python program to remove a newline in Python

#  String = "\nBest \nDeeptech \nPython \nTraining\n" 

# Given string with newlines
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters
string_without_newlines = string.replace("\n", " ")

# Optionally, strip leading/trailing whitespace (caused by leading/trailing newlines)
string_without_newlines = string_without_newlines.strip()

# Print the result
print(string_without_newlines)


# ans
# Best  Deeptech  Python  Training