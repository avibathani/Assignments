def convert_gallons_to_liters(gallons_quantity):
    liters_quantity = gallons_quantity * 3.78541
    return liters_quantity

def main():
    while True:
        user_input = float(input("How many gallons do you have? (Enter a negative number to quit): "))
        
        if user_input < 0:
            print("Thanks for using the converter! Goodbye!")
            break
        
        converted_volume = convert_gallons_to_liters(user_input)
        
        print(f"{user_input:.2f} gallons is about {converted_volume:.2f} liters.")

if __name__ == "__main__":
    main()
