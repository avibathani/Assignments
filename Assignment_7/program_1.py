import random

def roll_the_dice():
    return random.randint(1, 6)

def main_program():
    current_roll = 0

    while current_roll != 6:
        current_roll = roll_the_dice()
        print(f"Dice shows: {current_roll}")

if __name__ == "__main__":
    main_program()
