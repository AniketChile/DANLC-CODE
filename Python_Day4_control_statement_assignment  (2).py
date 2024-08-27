# Function to check if a person is eligible to vote
def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

# Take input from the user
age = input("Enter your age: ")

# Check if the input is a digit and convert it to an integer
if age.isdigit():
    age = int(age)
    # Print whether the person is eligible to vote
    print(check_voting_eligibility(age))
else:
    print("Please enter a valid age (integer).")


# ans:
# Enter your age: 10
# Not eligible to vote