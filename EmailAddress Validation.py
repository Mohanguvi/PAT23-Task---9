import re # Regular Expression for search
pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,4}$" # Pattern for Email Address

userInput = input("Enter your email address: ")   # Get the user mail address

if re.search(pattern , userInput):   # search the pattern that matches in the pattern
    print(f"{userInput} is vaild.")  # display the result if the mail id is valid
else:
    print(f"{userInput} is invaild.") # display the result if the mail id is invalid