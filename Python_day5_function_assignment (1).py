# Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

# Division Function
def div(a, b):
    # Check if the divisor is not zero to avoid division by zero error
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

# Call the function and pass two numbers
result = div(10, 2)

# Display the result
print("The division result is:", result)

# ans
# The division result is: 5.0
