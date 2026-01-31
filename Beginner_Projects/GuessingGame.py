
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
import random
number_to_guess = random.randint(1, 100)
attempts = 0
while True: 
    user_guess = input("Make a guess: ")
    attempts += 1
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Please enter a valid number.")
        continue
    if user_guess < number_to_guess:
        print("Too low.")
    elif user_guess > number_to_guess:
        print("Too high.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break


