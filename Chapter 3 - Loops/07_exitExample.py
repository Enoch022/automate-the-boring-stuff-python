# Program demonstrates exiting a program early with sys.exit()

import sys  # Import sys module for sys.exit()

while True:  # Infinite loop
    print('Type exit to exit.')
    response = input('>')  # Get user input
    if response == 'exit':  # Check for exit command
        sys.exit()  # Exit program
    print('You typed ' + response + '.')  # Echo input
