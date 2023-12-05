import re    # Regular Expression for search

def Bangladesh_number(mobile_number):
    # Pattern for a valid Bangladesh mobile number
    pattern = r'^(\+8801|8801|01|008801)[1|3-9]{1}(\d){8}'
    if re.match(pattern, mobile_number): 
        return True
    else:
        return False

check = input("Enter the phone number: ")      # Get user input of USA phone number

if Bangladesh_number(check):       # it will search and matches as per pattern and display the result
    print("Phone number is valid.")
else:
    print("Phone number is invalid.")





    