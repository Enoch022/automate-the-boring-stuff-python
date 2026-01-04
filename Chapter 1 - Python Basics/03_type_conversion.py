# Type conversion examples

print(str(29))
print(str(-3.14))
print(int('42'))
print(int('-99'))
print(int(1.25))
print(int(1.99))
print(float('3.14'))
print(float(10))

# Example with input
spam = input('Enter a number: ')
print(spam)  # always a string
spam = int(spam)
print(spam * 10 / 5)
