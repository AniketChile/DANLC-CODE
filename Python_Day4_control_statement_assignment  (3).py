# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    else:
        return "Not a leap year"

# Take input from the user
year = int(input("Enter a year: "))

# Print whether the year is a leap year or not
print(is_leap_year(year))

# ans:
# Enter a year: 2016
# Leap year