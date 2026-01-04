print('Enter TB or GB for the advertised unit:')
unit = input('>')

if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity:')
advertised_capacity = float(input('>'))

real_capacity = str(round(advertised_capacity * discrepancy, 2))
print('The actual capacity is ' + real_capacity + ' ' + unit)
