# 1. give while loop example to print five numbers while condition is True
# 2. give else statement example with while loop
# 3. give an example of using if and break with while loop

# 1. give while loop example to print five numbers while condition is True
counter = 1
while counter < 6:
    print(counter)
    counter = counter + 1
print('--------------******--------------\n')

# 2. give else statement example with while loop
counter = 1
while counter < 6:
    print(counter)
    counter = counter + 1
else:
    print('counter is no longer < 6')
print('--------------******--------------\n')

# 3. give an example of using if and break with while loop
while True: 
  response = input('Would you like to continue (y/n): ')
  
  if response == 'n' or response == 'N':
    print('ok bye!')
    break