import re    # Regular Expression for search

def USA_phone_number(telephone_number):
    # Pattern for a valid USA telephone number with optional parentheses and dashes
    pattern = r'^\(?([2-9][0-9]{2})\)?[-. ]?([2-9][0-9]{2})[-. ]?([0-9]{4})$'
    if re.match(pattern, telephone_number): 
        return True
    else:
        return False

check = input("Enter a USA phone number: ")      # Get user input of USA phone number

if USA_phone_number(check):       # it will search and matches as per pattern and display the result
    print("Phone number is valid.")
else:
    print("Phone number is invalid.")

