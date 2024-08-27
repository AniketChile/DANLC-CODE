# Function to check if a number is positive, negative, or zero
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Take input from the user
number = float(input("Enter a number: "))

# Print whether the number is positive, negative, or zero
print(check_number(number))

# ans :
# Enter a number: -10
# Negative