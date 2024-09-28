import random

secret_number = random.randint(1, 10)

print("I've picked a number between 1 and 10. Try to guess it!")

while True:
    user_input = input("What's your guess? ")

    try:
        player_guess = int(user_input)
    except ValueError:
        print("Oops! Please enter a valid whole number.")
        continue

    if player_guess < secret_number:
        print("Too low, try again!")
    elif player_guess > secret_number:
        print("Too high, try again!")
    else:
        print("Spot on! You got it!")
        break