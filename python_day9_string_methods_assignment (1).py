# 1. Write a Python program to Count all letters, digits, and special symbols from the given string

#  Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 3 Symbol = 4 

import string

def count_chars_digits_symbols(input_string):
    letters_count = 0
    digits_count = 0
    symbols_count = 0

    for char in input_string:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1
        elif char in string.punctuation:
            symbols_count += 1

    print(f"Chars = {letters_count}")
    print(f"Digits = {digits_count}")
    print(f"Symbols = {symbols_count}")

# Input string
input_string = "P@#yn26at^&i5ve"
count_chars_digits_symbols(input_string)

# ans
# Chars = 8
# Digits = 3
# Symbols = 4