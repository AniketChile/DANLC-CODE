# 2. Write a Python program to remove duplicate characters of a given string.

#  Input = “String and String Function” Output: String and Function

def remove_duplicate_words(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Use a set to track seen words
    seen_words = set()
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the words in the list
    for word in words:
        # Add the word to the result if it hasn't been seen before
        if word not in seen_words:
            seen_words.add(word)
            result.append(word)
    
    # Join the words back into a single string
    return " ".join(result)

# Input string
input_string = "String and String Function"
output_string = remove_duplicate_words(input_string)
print(output_string)

# ans
# String and Function
