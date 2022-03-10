# Classic Calculator on Python 3

print('Classic Calculator')
print('')
func_choice = str(input('Select Function (+; -; *; /): '))
num1, num2, = float(input('First Value: ')), float(input('Second Value: '))

# Four math functions
if func_choice == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif func_choice == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif func_choice == '*':
    print(f'{num1} * {num2} = {num1 * num2}')
elif func_choice == '/':
    if num2 != 0:
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print("Math error: Don't split to zero")
else:
    print("Script error: Symbol operation not found")
