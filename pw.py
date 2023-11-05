# Importing the needed libraries
import secrets
import string
import random
import pyperclip
import time
import os

# Creates the loop
generate = True
while generate:
# Creating the "universe" of characters to be used by the program
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

# Asking the user which categories of characters should be used
    print("")
    print("")
    print(" ------------------------------------------------------------------------------------------- ")
    print(" ----------------------------- PYTHON BASED PASSWORD GENERATOR ----------------------------- ")
    print(" ----------------------------------------- BY JARV ----------------------------------------- ")
    print(" ------------------------------------------------------------------------------------------- ")
    print("")
    print("Let's define which types of characters you want the password to have.")
    print("Keep in mind that the strongest passwords will include all of these character types.")
    print("Select '1' for YES or '0' for NO !!!")
    print("")
    print("")
    use_letters = int(input("Do you want it to contain Letters?  (1 or 0): "))
    use_digits = int(input("How about Digits?  (1 or 0): "))
    use_special_chars = int(input("Perhaps Special Characters?  (1 or 0): "))

# Asking the user to define the desired password lenght
    password_lenght = int()
    while True:
        if password_lenght > 0:
            break
        else:
            password_lenght = int(input("Insert password lenght (The bigger the better): "))

# Verifies user's selection_list and runs the program accordingly
    if use_letters == 1 and use_digits == 1 and use_special_chars == 1:
        selection_list = letters + digits + special_chars

    elif use_letters == 0 and use_digits == 1 and use_special_chars == 1:
        selection_list = digits + special_chars

    elif use_letters == 1 and use_digits == 0 and use_special_chars == 1:
        selection_list = letters + special_chars

    elif use_letters == 1 and use_digits == 1 and use_special_chars == 0:
        selection_list = letters + digits

    elif use_letters == 0 and use_digits == 0 and use_special_chars == 1:
        selection_list = special_chars

    elif use_letters == 1 and use_digits == 0 and use_special_chars == 0:
        selection_list = letters

    elif use_letters == 0 and use_digits == 1 and use_special_chars == 0:
        selection_list = digits
    
    else:
        print("You didn't follow the provided instructions. Every character type will be used anyway.")
        selection_list = digits + letters + special_chars

# Take note on where the user will use the password
    where_used = input("Where will you use the password? (Leave in blank if you don't want to register that information in the generated .txt document): ")

# Where the magic happens
    password = ""
    for i in range(password_lenght):
        password += "".join(secrets.choice(selection_list))

# Start counting elapsed time 
    start_time = time.time()

# Outputs the generated password to a notepad in the same dir as the program
    with open("Password.txt", "a") as ff:
        print(password, " ---- ", where_used, file=ff)

# Copy the password to the user's clipboard
    pyperclip.copy(password)

# Stop counting the elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time
# Success message
    print("Everything ran successfully!")
    print(f"Time taken: {elapsed_time} seconds")
    print("")
    print("The generated password is VERY SAFE!")
    print("The password has been copied to your cliboard successfully.")
    print("")
# Ends the program or restarts the while generate loop
    restart = int(input("| Send 1 to restart the generator // Send 0 to close the generator |:  "))
    os.system("cls")
    if restart == 0:
        generate = False