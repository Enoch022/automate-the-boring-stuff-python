# Program asks for 'your name' using a break statement to exit

while True:  # Infinite loop
    print('Please type your name.')
    name = input('>')  # Get user input
    if name == 'your name':  # Check if input is correct
        break  # Exit loop

print('Thank you!')  # Print confirmation after loop
