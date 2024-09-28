correct_username = "Avnish0302"
correct_password = "Avnish@0203"

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        print("Incorrect username or password. Try again.")
        attempts += 1

if attempts == max_attempts:
    print("Access denied.")