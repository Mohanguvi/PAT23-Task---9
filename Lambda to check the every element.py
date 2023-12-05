# Get the user Input value
userInput = input("Enter the list of values by spaces: ")

# Convert the input value into list
userlist = userInput.split()

# Check the every element in the list is an integer or string
ElementCheck = lambda lst: all(isinstance(x, (int, str)) for x in lst)

# Get the result from the user list
result = ElementCheck(userlist)

# Display the result
print(result)

