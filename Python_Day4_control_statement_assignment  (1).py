# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Take input from the user
try:
    num = int(input("Enter a number: "))
    # Print whether the number is even or odd
    print(check_even_odd(num))
except ValueError:
    print("Please enter a valid integer.")


# ans:
# Enter a number: 11
# Odd