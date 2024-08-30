# a python program finding the factorial of a given number using a while loop

def factorial(number):
    # Initialize the result to 1
    result = 1
    
    # Use a while loop to multiply the result by each number until number > 1
    while number > 1:
        result *= number
        number -= 1
    
    return result

# Input: Get a number from the user
number = int(input("Enter a number: "))

# Calculate the factorial
fact = factorial(number)

# Output the result
print(f"The factorial of {number} is {fact}.")

# ans
# Enter a number: 5
# The factorial of 5 is 120.
