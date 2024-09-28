import random

def throw_dice(sides_count):
    return random.randint(1, sides_count)

def main():
    num_sides = int(input("How many sides does your dice have? "))
    target_value = int(input("What maximum value do you want to roll (e.g., 21 for a 21-sided die)? "))

    roll_history = []  
    current_throw = 0 
    
    while current_throw != target_value:
        current_throw = throw_dice(num_sides)
        roll_history.append(current_throw)
        print(f"You rolled a: {current_throw}")

    print(f"\nIt took {len(roll_history)} rolls to get a {target_value}.")
    print("All rolls:", roll_history)

if __name__ == "__main__":
    main()
