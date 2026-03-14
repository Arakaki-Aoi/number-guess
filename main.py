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
    return 0 < data < 11

# low or high check
def guess_hint(answer, guess):
    if guess > answer:
        return "Too high!"
    else:
        return "Too low!"

# Start the game
print("Game start!")

# Generate random number
random_number = random.randint(1, 10)
is_valid_input = False

# Get user input and validate
for game_count in range(3):
    while not is_valid_input:
        user_input_number = input("Enter an integer between 1 and 10: ")
        if int_validation_check(user_input_number):
            int_user_input_number = int(user_input_number)
            if range_validation_check(int_user_input_number):
                is_valid_input = True
            else:
                print("Please enter a number between 1 and 10.")
        else:
            print("Please enter a valid integer.")
    # Check the result
    if random_number == int_user_input_number:
        print("Correct! Great job!")
        break
    else:
        is_valid_input = False
        if game_count == 2:
            print("Game over! The number was", random_number)
        else:
            result = guess_hint(random_number, int_user_input_number)
            if 2 - game_count == 1:
                print(f"{result} Try again.\nYou have {2 - game_count} attempt left.")
            else:
                print(f"{result} Try again.\nYou have {2 - game_count} attempts left.")