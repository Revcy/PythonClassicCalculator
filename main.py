print('Classic Calculator')
print('')

while True:
    func_choice = input('Select Function (+; -; *; /): ')
    num1, num2, = float(input('First Value: ')), float(input('Second Value: '))

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
    while True:
        quit_promt = input('You wanna exit? (Yes, No): ')
        if quit_promt in ['Yes', 'YES', 'yes']:
            quit_flag = True
            break
        elif quit_promt in ['No', 'NO', 'no']:
            quit_flag = False
            break
        else:
            print('Unknown input. Try again: ')
    if quit_flag:
        break
