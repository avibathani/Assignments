import math

def get_unit_price(pizza_diameter_cm, pizza_price_euros):
    radius_m = (pizza_diameter_cm / 100) / 2  
    area_m2 = math.pi * (radius_m ** 2)  
    unit_price = pizza_price_euros / area_m2 
    return unit_price

def main():
    print("Enter details for the first pizza:")
    first_diameter = float(input("Diameter in centimeters: "))
    first_price = float(input("Price in euros: "))
    
    print("\nEnter details for the second pizza:")
    second_diameter = float(input("Diameter in centimeters: "))
    second_price = float(input("Price in euros: "))

    first_unit_price = get_unit_price(first_diameter, first_price)
    second_unit_price = get_unit_price(second_diameter, second_price)

    print(f"\nUnit price for the first pizza: {first_unit_price:.2f} euros per square meter.")
    print(f"Unit price for the second pizza: {second_unit_price:.2f} euros per square meter.")

    if first_unit_price < second_unit_price:
        print("The first pizza provides better value for money.")
    elif first_unit_price > second_unit_price:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")

if __name__ == "__main__":
    main()
