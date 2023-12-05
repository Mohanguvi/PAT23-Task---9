import re # Regex search pattern

def validate_password(password): # function class for the Validating the password
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_=+{};:\'",.<>?/\\|]).{16}$'  # pattern for the password
    if re.match(pattern, password):             # Check whether the passeord is matching as per the pattern or not
        return True
    else:
        return False

userInput = input("Enter the password: ")       # Get the password from the user

if validate_password(userInput):                # Display the result if the password is valid or not
    print("Password is valid.")
else:
    print("Password is invalid.")
