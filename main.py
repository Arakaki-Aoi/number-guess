import random 

# Validate integer input
def int_validation_check(data):
    try:
        int(data)
        return True
    except ValueError:
        return False

# Validate input range
def range_validation_check(data):
    return 0 < int(data) < 11
        
# Start the game
print("Game start!")

# Generate random number
random_number = random.randint(1, 10)

user_input_number = ""
error_check = False

# userinput & Validate
while not error_check:
    user_input_number = input("Enter an integer between 1 and 10: ")
    if int_validation_check(user_input_number):
        if range_validation_check(user_input_number):
            error_check = True
        else:
            print("Please enter a number between 1 and 10.")
    else:
        print("Please enter a valid integer.")

# Show result
if random_number == int(user_input_number):
    print("Correct! Great job!")
else:
    print("Wrong! Better luck next time.")