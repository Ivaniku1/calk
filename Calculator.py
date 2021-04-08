num1 = int(input('Enter the first number: '))
action = (input('Select and enter an action:\n Addition + \n Subtraction - \n Multiplication * \n Division / '"\n You action: "))
num2 = int(input('Enter the second number: '))
mist = "Mistake"
if action == '+':
    print(f'{num1} + {num2} = ')
    print(num1 + num2)
    
elif action == '-':
    print(f'{num1} - {num2} = ')
    print(num1 - num2)

elif action == '*':
    print(f'{num1} * {num2} = ')
    print(num1 * num2)

elif action == '/':
    print(f'{num1} / {num2} = ')
    print(num1 / num2)

else:
    print('Action is missing')
input()
