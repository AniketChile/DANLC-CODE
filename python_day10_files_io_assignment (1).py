# Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
# ABC.txt 
# Hello, my name is Aniket!
# I'm from Mumbai

def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')  # end='' avoids adding an extra newline
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
read_file_line_by_line('ABC.txt')


# ans
# Hello, my name is Aniket!
# I'm from Mumbai