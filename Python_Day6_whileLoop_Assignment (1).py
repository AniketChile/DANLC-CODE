# Write a python program to check whether a number is palindrome or not

def is_palindrome(number):
    # Convert the number to a string
    str_num = str(number)
    
    # Check if the string is the same when reversed
    return str_num == str_num[::-1]

# Input: Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

# ans
# Enter a number: 1001
# 1001 is a palindrome.