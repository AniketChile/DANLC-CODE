# Taking two numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Swapping the numbers using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Printing the swapped values
print(f"After swapping: First number = {num1}, Second number = {num2}")

# ans :
# Enter the first number: 5
# Enter the second number: 10
# After swapping: First number = 10, Second number = 5