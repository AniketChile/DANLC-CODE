# Function to find the largest of three integers
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Take input from the user as integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Print the largest number
largest = find_largest(num1, num2, num3)
print("The largest number is:", largest)

# ans:
# Enter the first number: 10
# Enter the second number: 15
# Enter the third number: 20
# The largest number is: 20