inch_to_cm_fac = 2.54

while True:

    inches = float(input("Enter inches "))
    
    if inches < 0:
        print("Exiting the program due to minus value.")
        break
    
    centimeters = inches * inch_to_cm_fac
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters.")