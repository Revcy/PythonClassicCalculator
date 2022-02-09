# Classic Calculator on Python 3
# Developer: github.com/Revcy
# First big practic project

print('Classic Calculator')
func_choice = str(input('Select Function (sum = +; dct = -; inc = *; spl = /): '))

# Four math functions
if func_choice == 'sum':
    num1, num2, = int(input('First Value: ')), int(input('Second Value: '))
    print(f'{num1} + {num2} = {num1 + num2}')

if func_choice == 'dct':
    num1, num2, = int(input('First Value: ')), int(input('Second Value: '))
    print(f'{num1} - {num2} = {num1 - num2}')

if func_choice == 'inc':
    num1, num2, = int(input('First Value: ')), int(input('Second Value: '))
    print(f'{num1} * {num2} = {num1 * num2}')

if func_choice == 'spl':
    num1, num2, = int(input('First Value: ')), int(input('Second Value: '))
    print(f'{num1} / {num2} = {num1 / num2}')


