# Classic Calculator on Python 3
# Developer: github.com/Revcy
# First big practice project

print('Classic Calculator')
print('')
func_choice = str(input('Select Function (+; -; *; /): '))

# Four math functions
if func_choice == '+':
    num1, num2, = int(input('First Value: ')), int(input('Second Value: '))
    print(f'{num1} + {num2} = {num1 + num2}')
elif func_choice == '-':
    num1, num2, = int(input('First Value: ')), int(input('Second Value: '))
    print(f'{num1} - {num2} = {num1 - num2}')
elif func_choice == '*':
    num1, num2, = int(input('First Value: ')), int(input('Second Value: '))
    print(f'{num1} * {num2} = {num1 * num2}')
elif func_choice == '/':
    num1, num2, = int(input('First Value: ')), int(input('Second Value: '))
    if num2 != 0:
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print("Math error: Don't split to zero")
else:
    print("Script error: Symbol operation not found")
