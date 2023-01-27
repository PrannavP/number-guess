import random

# Generating random number between 1 and 100
random_number = random.randint(1, 100)

# Asking the user for the number
user_guess = int(input("Guess a number between 1 and 100: "))

# Storing how many times did user guessed
user_guesses = 1

# looping until the user guesses the right answer
while user_guess != random_number:
    if user_guess > random_number:
        print("Too high... guess again")
    else:
        print("Too low... guess again")

    user_guess = int(input("Guess a number between 1 and 100: "))

    user_guesses += 1

# Congratulating the user after guessing the number
print(f"Congratulations! You guessed the number in {user_guesses} tries.")