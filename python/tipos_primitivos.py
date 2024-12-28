# Numbers to calculate the sum.

# Using int numbers
n1 = int(input('Type the first number and press enter: '))
n2 = int(input('Enter the second number and press enter: '))

# Using float numbers.
# n1 = float(input('Type the first number and press enter: '))
# n2 = float(input('Enter the second number and press enter: '))

# The sum calculate.
sumNumbers = (n1 + n2)

# Output.
print(f'The sum between {n1} + {n2} is {sumNumbers}') # Output with f-string.
print('The sum between {} + {} is {}'.format(n1, n2, sumNumbers)) # Output with format() function.

# To show the variable types.
print(type(n1))
print(type(n2))
print(type(sumNumbers))
