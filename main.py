import random 

# Game settings
MIN_NUMBER = 1
MAX_NUMBER = 10
MAX_ATTEMPTS = 3

# Validate input range
def in_range(data):
    return MIN_NUMBER <= data <= MAX_NUMBER

# low or high check
def guess_hint(answer, guess):
    return "Too high!" if guess > answer else "Too low!"

# input and validate
def input_and_validate():
    while True:
        guess = input(f"Enter an integer between {MIN_NUMBER} and {MAX_NUMBER}: ")
        try:
            guess_number = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if in_range(guess_number):
            return guess_number
        print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")

def play_game():
    print("Game start!")
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    # Get user input and validate
    for attempt in range(MAX_ATTEMPTS):
        guess_number = input_and_validate()

        # Check the result
        if random_number == guess_number:
            print("Correct! Great job!")
            break
        remaining_attempts = MAX_ATTEMPTS - attempt - 1
        if remaining_attempts == 0:
            print("Game over! The number was", random_number)
        else:
            result = guess_hint(random_number, guess_number)
            if remaining_attempts == 1:
                print(f"{result} Try again.\nYou have {remaining_attempts} attempt left.")
            else:
                print(f"{result} Try again.\nYou have {remaining_attempts} attempts left.")

play_game()