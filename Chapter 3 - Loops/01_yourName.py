# Program asks the user to type 'your name' until they do so correctly

name = ''  # Initialize name as empty string

# Loop continues until user types exactly 'your name'
while name != 'your name':
    print('Please type your name.')
    name = input('>')  # Get user input

print('Thank you!')  # Print confirmation once the correct name is entered
