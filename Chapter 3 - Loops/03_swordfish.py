# Password check program using continue and break in a loop

while True:  # Infinite loop for main program
    print('Who are you?')
    name = input('>')  # Get name input
    if name != 'Joe':  # If name isn't Joe
        continue  # Go back to start of loop

    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input('>')  # Get password input
    if password == 'swordfish':  # Correct password
        break  # Exit loop

print('Access granted.')  # Access granted message after loop
